# Project Structure

This document explains the current project organization and the reasoning behind it.

## Current Structure

```
reading_app_250705/
├── CLAUDE.md                    # AI navigation guide
├── .llm_context/               # AI-specific context
│   ├── tech-stack.md          # Technology decisions
│   ├── project-structure.md   # This file
│   └── workflows.md           # Common development tasks
├── plans/                      # Human planning documents
│   ├── summary.md             # Project vision & roadmap
│   └── epics/                 # Feature specifications
│       ├── 01-project-setup/
│       ├── 02-*/
│       └── 03-document-upload/
├── backend/                    # FastAPI application
│   ├── app/                   # Application package
│   │   ├── __init__.py        # FastAPI app factory (create_app)
│   │   ├── models/            # SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   └── base.py        # Base model with TimestampMixin
│   │   └── schemas/           # Pydantic schemas
│   │       └── __init__.py
│   ├── api/                   # API routes
│   │   └── v1/                # Version 1 API
│   ├── alembic/               # Database migrations
│   │   ├── versions/          # Migration files
│   │   ├── env.py             # Alembic environment (async configured)
│   │   └── alembic.ini        # Alembic configuration
│   ├── config.py              # Application configuration
│   ├── main.py                # Application entry point
│   └── pyproject.toml         # Python dependencies
├── frontend/                   # React application (when created)
└── docker/                     # Docker configurations (when created)
```

## Organization Principles

### Planning vs Context
- **`/plans/`**: Human-readable project planning and roadmaps
- **`.llm_context/`**: AI-specific context and guidance documents
- **`CLAUDE.md`**: Central navigation pointing to both

### Epic Organization
- Epics are numbered for execution order
- Each epic contains:
  - `design.md` - Feature specifications and requirements
  - `todo.md` - Implementation tasks and progress

### Code Organization (Future)
- **Backend**: Python FastAPI with clear module separation
- **Frontend**: React with TypeScript, component-based architecture
- **Docker**: Environment-specific configurations

## Current Status
Backend foundation is implemented with:
- FastAPI app with OpenAPI documentation
- SQLAlchemy 2.0 with async support
- Alembic migrations configured
- Basic error handling middleware
- API versioning structure (/api/v1/)

Frontend and Docker configurations remain to be implemented.