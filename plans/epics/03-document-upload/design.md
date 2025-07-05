# Epic 03: Document Upload System

## Overview
Design and implement a robust document upload system that handles file uploads, processing, status tracking, and real-time progress updates. This system must be extensible to support future processing stages like OCR, indexing for search, and LLM preparation.

## Key Questions & Decisions

### Upload Status Tracking
**Q: How do we track upload progress through multiple stages?**

We need a state machine for document processing:
```
UPLOADING → UPLOADED → PROCESSING → READY_TO_READ → READY_FOR_CHAT
                     ↓
                  FAILED (with reason)
```

**Decision**: Use a `document_status` table with:
- Status enum
- Progress percentage
- Current processing step
- Error details if failed
- Timestamps for each state transition

### Real-time Updates
**Q: How do we communicate progress to the frontend?**

Options considered:
1. Polling - Simple but inefficient
2. WebSockets - Real-time but complex
3. Server-Sent Events (SSE) - One-way, perfect for progress

**Decision**: Use SSE for progress updates:
- Lightweight one-way communication
- Built-in reconnection
- Works well with REST API
- Easy to implement with FastAPI

### File Storage
**Q: Where and how do we store uploaded files?**

**Decision**: 
- Store files on disk with UUID names
- Keep original filename in database
- Structure: `/storage/documents/{year}/{month}/{uuid}.{ext}`
- Future: Easy migration to S3-compatible storage

### Processing Pipeline
**Q: How do we handle different processing stages?**

**Decision**: Background task queue with stages:
1. **Upload Stage**: File validation, virus scan (future)
2. **Processing Stage**: 
   - Extract metadata (title, author, page count)
   - Generate thumbnails
   - Extract text for search (future)
3. **Indexing Stage** (future): Prepare for LLM chat

Each stage updates the status and progress.

### Database Schema

```sql
-- Main document table
CREATE TABLE documents (
    id UUID PRIMARY KEY,
    title VARCHAR(500),
    author VARCHAR(500),
    filename VARCHAR(500) NOT NULL,
    file_path VARCHAR(1000) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size BIGINT NOT NULL,
    page_count INTEGER,
    thumbnail_path VARCHAR(1000),
    uploaded_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- Status tracking table
CREATE TABLE document_status (
    id UUID PRIMARY KEY,
    document_id UUID REFERENCES documents(id),
    status VARCHAR(50) NOT NULL, -- UPLOADING, UPLOADED, PROCESSING, etc
    progress INTEGER DEFAULT 0, -- 0-100
    current_step VARCHAR(200), -- "Extracting metadata", "Generating preview"
    error_message TEXT,
    created_at TIMESTAMP NOT NULL,
    
    -- Timestamps for each stage
    uploaded_at TIMESTAMP,
    processing_started_at TIMESTAMP,
    processing_completed_at TIMESTAMP,
    ready_to_read_at TIMESTAMP,
    ready_for_chat_at TIMESTAMP
);

-- Processing log for debugging
CREATE TABLE document_processing_log (
    id UUID PRIMARY KEY,
    document_id UUID REFERENCES documents(id),
    step VARCHAR(200),
    status VARCHAR(50),
    message TEXT,
    created_at TIMESTAMP NOT NULL
);
```

### API Design

**Upload Endpoint**:
```
POST /api/documents/upload
Content-Type: multipart/form-data

Response: {
    "document_id": "uuid",
    "status": "UPLOADING",
    "progress": 0
}
```

**Status Endpoint**:
```
GET /api/documents/{id}/status

Response: {
    "status": "PROCESSING",
    "progress": 45,
    "current_step": "Extracting metadata"
}
```

**Progress Stream**:
```
GET /api/documents/{id}/progress
Accept: text/event-stream

data: {"status": "PROCESSING", "progress": 45}
data: {"status": "PROCESSING", "progress": 60}
data: {"status": "READY_TO_READ", "progress": 100}
```

### Frontend Experience

1. **Upload UI**:
   - Drag & drop zone with visual feedback
   - File type validation before upload
   - Multiple file queue support
   - Individual progress bars

2. **Progress Tracking**:
   - Real-time progress bar
   - Current step description
   - Estimated time remaining
   - Cancel upload option

3. **Post-Upload**:
   - Automatic navigation to document on completion
   - Error recovery options
   - Retry failed uploads

### Error Handling

Types of errors:
- **File too large**: Check before upload
- **Invalid format**: Validate extension and MIME type
- **Processing failure**: Show specific error, allow retry
- **Network failure**: Auto-retry with exponential backoff

### Security Considerations

- File type validation (whitelist approach)
- File size limits (configurable)
- Virus scanning (future)
- Secure file storage (no direct access)
- Rate limiting per user

### Performance Optimization

- Chunked uploads for large files
- Resume interrupted uploads
- Background processing with queue
- Progress caching to reduce DB queries
- CDN for processed files (future)

### Future Extensibility

Design allows adding:
- OCR for scanned PDFs
- Full-text indexing
- LLM vector embeddings
- Multiple processing pipelines
- Batch uploads
- Cloud storage migration

## Implementation Plan

### Phase 1: Basic Upload
1. Create database schemas
2. Implement file upload endpoint
3. Basic status tracking
4. Simple progress polling

### Phase 2: Processing Pipeline
1. Background task system
2. Metadata extraction
3. Status state machine
4. Processing log

### Phase 3: Real-time Updates
1. SSE implementation
2. Frontend progress tracking
3. Error handling UI
4. Upload queue management

### Phase 4: Optimization
1. Chunked uploads
2. Resume capability
3. Performance monitoring
4. Security hardening

## Testing Strategy

- Unit tests for each processing stage
- Integration tests for full pipeline
- Load testing for concurrent uploads
- Error simulation testing
- Progress accuracy testing

## Monitoring

Track:
- Upload success rate
- Processing time per stage
- Error frequency by type
- Storage usage
- Queue depth