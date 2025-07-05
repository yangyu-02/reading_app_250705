# Epic 01: Project Setup - TODO List

## Project Initialization
- [ ] **Create root project structure**
  - [ ] Initialize git repository
  - [ ] Create comprehensive .gitignore for Python, Node, IDEs
  - [ ] Create root README.md with project overview
  - [ ] Create LICENSE file (if applicable)
  - [ ] Setup base directory structure (backend/, frontend/, docker/)

- [ ] **Create Makefile**
  - [ ] Add help target with documentation
  - [ ] Add dev target to start full environment
  - [ ] Add individual service targets (backend, frontend, db)
  - [ ] Add utility targets (clean, lint, test, migrate)
  - [ ] Add .PHONY declarations for all targets

## Backend Setup
- [ ] **Initialize Python project**
  - [ ] Install uv package manager
  - [ ] Create backend/pyproject.toml with project metadata
  - [ ] Setup Python 3.11+ virtual environment
  - [ ] Create backend/.gitignore for Python specifics
  - [ ] Create backend/README.md with setup instructions

- [ ] **Install core dependencies**
  - [ ] FastAPI and uvicorn for web framework
  - [ ] SQLAlchemy 2.0+ and alembic for database
  - [ ] Pydantic and pydantic-settings for validation
  - [ ] asyncpg for async PostgreSQL
  - [ ] python-multipart for file uploads

- [ ] **Create FastAPI application structure**
  - [ ] Create backend/app/__init__.py
  - [ ] Create backend/app/main.py with FastAPI app
  - [ ] Create backend/app/core/config.py for settings
  - [ ] Create backend/app/core/database.py for DB setup
  - [ ] Create backend/app/api/deps.py for dependencies
  - [ ] Setup CORS middleware configuration

- [ ] **Setup database foundation**
  - [ ] Create backend/app/models/__init__.py
  - [ ] Create backend/app/models/base.py with SQLAlchemy base
  - [ ] Create backend/app/schemas/__init__.py
  - [ ] Initialize alembic with alembic init
  - [ ] Configure alembic.ini for async operation
  - [ ] Create first migration script

- [ ] **Implement basic endpoints**
  - [ ] Create health check endpoint (/health)
  - [ ] Create API versioning structure (/api/v1/)
  - [ ] Setup OpenAPI documentation
  - [ ] Create script to export OpenAPI spec
  - [ ] Add basic error handling middleware

- [ ] **Setup development tools**
  - [ ] Configure ruff for linting/formatting
  - [ ] Configure mypy for type checking
  - [ ] Setup pytest with async support
  - [ ] Create backend/tests/ directory structure
  - [ ] Add example test for health endpoint

## Frontend Setup
- [ ] **Initialize React project**
  - [ ] Create frontend with Vite (npm create vite@latest)
  - [ ] Choose React + TypeScript template
  - [ ] Install pnpm as package manager
  - [ ] Update to latest React 18.x
  - [ ] Create frontend/.gitignore

- [ ] **Configure TypeScript**
  - [ ] Enable strict mode in tsconfig.json
  - [ ] Setup path aliases (@/ for src/)
  - [ ] Configure ESLint with TypeScript rules
  - [ ] Setup Prettier for formatting
  - [ ] Add lint-staged configuration (without git hooks)

- [ ] **Install core dependencies**
  - [ ] Mantine UI v7.x and dependencies
  - [ ] React Router v6 for routing
  - [ ] TanStack Query for data fetching
  - [ ] Axios for HTTP client
  - [ ] orval for API client generation
  - [ ] dayjs for date handling

- [ ] **Setup project structure**
  - [ ] Create src/components/ for shared components
  - [ ] Create src/pages/ for route pages
  - [ ] Create src/hooks/ for custom hooks
  - [ ] Create src/services/ for API clients
  - [ ] Create src/utils/ for utilities
  - [ ] Create src/types/ for TypeScript types

- [ ] **Configure development environment**
  - [ ] Setup Vite proxy for backend API
  - [ ] Configure environment variables (.env)
  - [ ] Setup orval configuration
  - [ ] Create npm scripts for common tasks
  - [ ] Setup CSS/styling approach (CSS modules)

- [ ] **Create base application**
  - [ ] Setup Mantine provider with theme
  - [ ] Create base layout component
  - [ ] Setup React Router with routes
  - [ ] Create 404 page
  - [ ] Create loading/error boundaries
  - [ ] Implement basic responsive design

## Docker Configuration
- [ ] **Create Docker Compose setup**
  - [ ] Create docker-compose.yml in root
  - [ ] Configure PostgreSQL 16 service
  - [ ] Setup proper volumes for data persistence
  - [ ] Configure health checks
  - [ ] Set appropriate restart policies

- [ ] **Configure PostgreSQL**
  - [ ] Set default database name and credentials
  - [ ] Create init script for database setup
  - [ ] Configure connection pooling limits
  - [ ] Setup backup volume mount
  - [ ] Add pgAdmin service (optional, commented out)

- [ ] **Environment configuration**
  - [ ] Create .env.example with all variables
  - [ ] Document each environment variable
  - [ ] Setup different configs for dev/test
  - [ ] Ensure secrets are never committed
  - [ ] Create docker/.dockerignore

## Developer Experience
- [ ] **Complete Makefile targets**
  - [ ] `make install` - Install all dependencies
  - [ ] `make dev` - Start everything
  - [ ] `make backend` - Start backend only
  - [ ] `make frontend` - Start frontend only
  - [ ] `make db` - Start database only
  - [ ] `make migrate` - Run DB migrations
  - [ ] `make makemigrations` - Create new migration
  - [ ] `make types` - Generate TypeScript types
  - [ ] `make lint` - Run all linters
  - [ ] `make format` - Format all code
  - [ ] `make test` - Run all tests
  - [ ] `make test-backend` - Backend tests only
  - [ ] `make test-frontend` - Frontend tests only
  - [ ] `make clean` - Stop and remove containers
  - [ ] `make reset-db` - Reset database

- [ ] **Setup type generation workflow**
  - [ ] Create OpenAPI export script
  - [ ] Configure orval for TypeScript generation
  - [ ] Add Make target for type sync
  - [ ] Document the type flow
  - [ ] Create example of type usage

- [ ] **Create development documentation**
  - [ ] Write comprehensive README.md
  - [ ] Document all Make commands
  - [ ] Create CONTRIBUTING.md guide
  - [ ] Document project conventions
  - [ ] Add troubleshooting section

## Testing & Validation
- [ ] **Validate full setup**
  - [ ] Test fresh clone and setup
  - [ ] Verify all Make targets work
  - [ ] Test type generation flow
  - [ ] Ensure hot reload works
  - [ ] Test database migrations

- [ ] **Create initial tests**
  - [ ] Backend health check test
  - [ ] Frontend component render test
  - [ ] API client generation test
  - [ ] Database connection test
  - [ ] Environment variable loading test

## Documentation
- [ ] **Update project documentation**
  - [ ] Update CLAUDE.md with setup details
  - [ ] Create architecture diagram
  - [ ] Document technology decisions
  - [ ] Add examples for common tasks
  - [ ] Create onboarding checklist

## Final Checklist
- [ ] Project runs with single `make dev` command
- [ ] Type changes flow from backend to frontend
- [ ] Hot reload works for both frontend and backend
- [ ] All linters and formatters are configured
- [ ] Tests can be run easily
- [ ] New developer can start in < 10 minutes
- [ ] No hardcoded secrets or credentials
- [ ] All tools are documented