# Reading App Project Summary

## Vision
Build a modern reading application with LLM-powered document chat, evolving from personal use to a full SaaS platform.

## Core Features
1. **Document Reading**: Support for PDF, EPUB, and MOBI formats
2. **LLM Chat**: Ask questions about your documents
3. **Annotations**: Highlights, notes, and bookmarks
4. **Library Management**: Organize and search your documents

## Development Phases

### Phase 1: Local Application
- Single-user desktop/web app
- Local file storage
- Basic reading and annotation features
- LLM chat with documents

### Phase 2: Family & Friends Hosting
- Multi-user support
- Basic authentication
- Shared libraries
- Self-hosting documentation

### Phase 3: SaaS Platform
- Payment integration
- Usage tiers and limits
- Advanced security
- API access
- Mobile apps

## Architecture Overview
- **Backend**: Python FastAPI + PostgreSQL
- **Frontend**: React + TypeScript + Mantine
- **Type Safety**: OpenAPI → TypeScript generation
- **Storage**: Local → S3-compatible → Cloud
- **Deployment**: Docker → Self-hosted → Cloud platform

## Project Structure
```
/reading-app
├── backend/          # FastAPI application
├── frontend/         # React application  
├── plans/           # Project planning documents
│   ├── summary.md   # This file
│   ├── TECH_STACK.md # Technology decisions
│   └── epics/       # Detailed epic planning
├── docker/          # Docker configurations
└── CLAUDE.md        # AI assistant instructions
```

## Epic Breakdown

### Foundation & Setup
1. **Project Setup** - Package managers, Docker, initial structure
2. **Database Schema** - Core models, migrations, relationships

### Document Management
3. **Document Upload** - Upload flow, processing pipeline, status tracking
4. **Library Management** - CRUD operations, metadata, organization
5. **File Processing** - PDF/EPUB parsing, metadata extraction

### Reading Experience  
6. **PDF Viewer** - Rendering, navigation, performance
7. **EPUB Viewer** - Rendering, chapter navigation, styling
8. **Reading Progress** - Position tracking, sync, bookmarks

### Annotations
9. **Highlighting System** - Text selection, storage, rendering
10. **Notes & Comments** - Note creation, organization, export

### Search & Discovery
11. **Full-text Search** - Indexing, search UI, results
12. **Library Browse** - Filtering, sorting, collections

## Success Metrics
- **Phase 1**: Functional local app with core features
- **Phase 2**: Successfully hosting for 10+ users
- **Phase 3**: 100+ paying customers, 99.9% uptime

## Constraints & Principles
1. **Progressive Enhancement**: Each phase builds on the previous
2. **Type Safety**: Strong typing across frontend/backend boundary
3. **User Privacy**: Local-first approach, user owns their data
4. **Developer Experience**: Clear documentation, easy setup
5. **Cost Efficiency**: Self-hostable, reasonable cloud costs