# Epic 01: Project Setup

## Overview

Establish the foundational development environment, tooling, and project structure that will support the entire application lifecycle from local development through to SaaS deployment.

## Key Questions & Decisions

### Package Management

**Q: Which package managers should we use?**

**Backend (Python)**:

- Options: pip, poetry, uv
- **Decision**: `uv` - Fast, modern, handles virtual envs
- Rationale: Better performance than pip, simpler than poetry

**Frontend (JavaScript)**:

- Options: npm, yarn, pnpm, bun
- **Decision**: `pnpm` - Efficient disk usage, fast, reliable
- Rationale: Saves space with shared dependencies, good monorepo support

### Project Structure

**Q: How should we organize the codebase?**

**Decision**: Monorepo with clear separation

```
/reading-app
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core config
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   └── utils/        # Utilities
│   ├── alembic/          # DB migrations
│   ├── tests/
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom hooks
│   │   ├── pages/        # Page components
│   │   ├── services/     # API clients
│   │   ├── store/        # State management
│   │   └── utils/        # Utilities
│   ├── public/
│   └── package.json
├── docker/
├── Makefile              # Developer commands
└── docs/
```

### Development Environment

**Q: How do we ensure consistent dev environments?**

**Decision**: Docker for services, native for code

- PostgreSQL in Docker
- Redis in Docker (future)
- Python/Node run natively for better DX
- Docker Compose for orchestration

### Code Quality Tools

**Backend**:

- **Linting**: `ruff` (fast, replaces flake8/black/isort)
- **Type Checking**: `mypy` with strict mode
- **Testing**: `pytest` with coverage

**Frontend**:

- **Linting**: ESLint with strict config
- **Formatting**: Prettier
- **Type Checking**: TypeScript strict mode
- **Testing**: Vitest + React Testing Library

### API Development Workflow

**Q: How do we maintain type safety across the stack?**

**Decision**: OpenAPI-driven development

1. Define Pydantic models
2. FastAPI generates OpenAPI spec
3. `orval` generates TypeScript client
4. Types flow from backend to frontend

### Environment Configuration

**Q: How do we manage configuration?**

**Decision**:

- `.env` files for local development
- `pydantic-settings` for backend validation
- Vite env vars for frontend
- Docker env injection for deployment

Example backend config:

```python
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    STORAGE_PATH: Path = Path("./storage")
    MAX_UPLOAD_SIZE: int = 100 * 1024 * 1024  # 100MB
    
    class Config:
        env_file = ".env"
```

### Git Strategy

**Q: How do we structure commits and branches?**

**Decision**:

- Conventional commits for clear history
- Feature branches with PR reviews
- `main` branch protection
- Semantic versioning for releases

### Developer Tooling

**Q: How do we simplify developer commands?**

**Decision**: Use a Makefile as the primary interface

- Single entry point for all operations
- Self-documenting with `make help`
- Handles task dependencies
- Cross-platform with Make installed

Example targets:
```makefile
make dev          # Start full dev environment
make backend      # Start backend only
make frontend     # Start frontend only  
make db           # Start PostgreSQL container
make migrate      # Run database migrations
make types        # Generate TypeScript types from OpenAPI
make lint         # Run all linters
make test         # Run all tests
make clean        # Clean up containers and temp files
```

### Testing Strategy

**Q: How do we ensure quality from day one?**

**Decision**: Test categories

- **Unit tests**: Core logic, utilities
- **Integration tests**: API endpoints
- **E2E tests**: Critical user flows (later)
- **Type tests**: TypeScript type safety

### Documentation

**Q: What needs documenting?**

**Decision**: Minimal but essential docs

- README with quick start
- API documentation (auto from OpenAPI)
- Architecture decisions in `/docs`
- Inline code comments only when needed

### Security Baseline

**Q: What security measures from the start?**

**Decision**:

- CORS configuration
- Rate limiting (basic)
- Input validation (Pydantic)
- SQL injection prevention (SQLAlchemy)
- XSS prevention (React defaults)
- Dependency scanning (GitHub)

## Implementation Steps

1. **Initialize Repositories**
   - Git init with .gitignore
   - Create folder structure

2. **Backend Setup**
   - Initialize uv project
   - Install FastAPI + dependencies
   - Create basic app structure
   - Setup database connection
   - Add health check endpoint

3. **Frontend Setup**
   - Initialize Vite + React + TS
   - Install Mantine + core deps
   - Setup routing structure
   - Configure API client generation
   - Create base layout

4. **Docker Configuration**
   - PostgreSQL with init scripts
   - Docker Compose for services
   - Volume mounts for development
   - Environment variable handling

5. **Developer Tooling**
   - Create comprehensive Makefile
   - Setup all Make targets
   - Type generation workflow
   - Database migration commands
   - Linting/formatting setup

## Success Criteria

- [ ] Can start full dev environment with one command
- [ ] Changes to backend types appear in frontend
- [ ] Linting/formatting is automatic
- [ ] Tests can be run with simple commands
- [ ] New developers can start in < 10 minutes

## Future Considerations

- Monorepo tools (Nx, Turborepo) if needed
- Container optimization for deployment
- Multi-environment configuration
- Performance monitoring setup
- Log aggregation preparation
