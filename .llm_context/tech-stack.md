# Tech Stack Decisions

This document tracks technology choices for the reading app project. It's a living document that evolves as the project grows.

## Confirmed Decisions

### Backend
- **Framework**: FastAPI
  - Auto-generated OpenAPI docs
  - Built-in validation with Pydantic
  - Excellent performance
  
- **Database**: PostgreSQL with SQLAlchemy 2.0
  - PostgreSQL from day 1 (no SQLite migration needed)
  - SQLAlchemy for ORM with type hints
  - Alembic for migrations
  
- **API Design**: REST with OpenAPI
  - FastAPI generates OpenAPI spec automatically
  - Use orval to generate TypeScript types from OpenAPI
  - Simpler than GraphQL for file uploads
  
### Frontend
- **Framework**: React with TypeScript
  - Vite for build tooling (faster than Next.js)
  - Strict TypeScript configuration
  
- **UI Library**: Mantine
  - Comprehensive component library
  - Good TypeScript support
  - Built-in dark mode
  
- **State Management**: 
  - TanStack Query for server state
  - Zustand for client state (if needed)

### Type Safety
- **API Contract**: FastAPI → OpenAPI → orval → TypeScript
- **Validation**: Pydantic (backend) + Zod (frontend)

## Pending Decisions

### Document Viewers
- **PDF Options**:
  - react-pdf (React wrapper for PDF.js)
  - PDF.js direct integration
  - pdfjs-dist
  - *Decision criteria*: Performance, annotation support, mobile compatibility

- **EPUB Options**:
  - react-epub-viewer
  - epub.js
  - foliate-js
  - *Decision criteria*: Feature set, maintenance status

### File Storage
- **Phase 1**: Local filesystem
- **Phase 2**: S3-compatible storage (MinIO for self-hosting)
- **Phase 3**: Cloud storage (S3, GCS, or Azure)

### LLM Integration
- **Phase 1**: Direct OpenAI API
- **Later considerations**:
  - Anthropic Claude API
  - Local models (Ollama)
  - LangChain (only if needed for complex workflows)

### Deployment
- **Development**: Docker Compose
- **Self-hosting**: Docker + Caddy/Nginx
- **SaaS**: TBD (AWS, GCP, Railway, Fly.io)

## Rejected Options

### Why not GraphQL?
- Adds complexity for limited benefit in this use case
- File uploads are more complicated
- REST with OpenAPI gives us type safety already

### Why not Next.js?
- Don't need SSR for a reading app
- Vite is faster for development
- Simpler deployment for self-hosting

### Why not LangChain (initially)?
- Adds unnecessary abstraction for simple chat
- Direct API calls are clearer and more maintainable
- Can add later if we need advanced features

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-01-05 | FastAPI over Django | Better performance, modern Python, automatic OpenAPI |
| 2025-01-05 | PostgreSQL from start | Avoid migration pain, better for multi-user |
| 2025-01-05 | Mantine UI | Comprehensive components, good DX |
| 2025-01-05 | Direct LLM APIs | Simpler than LangChain for basic chat |