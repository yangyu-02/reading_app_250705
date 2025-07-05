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
├── backend/                    # FastAPI application (when created)
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
This is an early-stage project. The structure will evolve as code is implemented, but the planning/context separation should remain stable.