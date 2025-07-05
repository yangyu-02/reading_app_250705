# Development Workflows

Common development tasks and how to approach them in this project.

## Adding a New Feature

1. **Check for existing epic**: Look in `/plans/epics/` for feature specifications
2. **Review design**: Read the `design.md` for requirements and approach
3. **Check dependencies**: Review `.llm_context/tech-stack.md` for technology constraints
4. **Follow patterns**: Look at existing code for similar implementations
5. **Update documentation**: Mark tasks complete in `todo.md`, add complexities to `design.md`

## Making Technology Decisions

1. **Check existing choices**: Review `.llm_context/tech-stack.md` first
2. **Document reasoning**: Add new decisions with "why" explanations
3. **Consider all phases**: Will this work for local/self-hosted/SaaS?
4. **Keep it simple**: Prefer direct solutions over complex abstractions

## Creating New Epics

1. **Follow numbering**: Continue sequence in `/plans/epics/`
2. **Create structure**: Add `design.md` and `todo.md` files
3. **Link to summary**: Ensure it aligns with `/plans/summary.md`
4. **Break down tasks**: Make todo items specific and actionable

## Code Organization

### Backend Development
- Use FastAPI patterns established in the project
- Maintain Pydantic models for type safety
- Follow existing module structure

### Frontend Development  
- Use React with TypeScript strict mode
- Follow Mantine component patterns
- Maintain type safety with backend APIs

### Database Changes
- Use SQLAlchemy patterns
- Create migrations for schema changes
- Document model relationships

## Testing Strategy

1. **Check existing patterns**: Look for test files and scripts
2. **Don't assume frameworks**: Verify testing setup before writing tests
3. **Test at appropriate levels**: Unit, integration, and E2E as needed

## Documentation Updates

After implementing features, update:
- Epic `todo.md` files (mark tasks complete)
- Epic `design.md` files (add discovered complexities)
- `.llm_context/tech-stack.md` (new technology decisions)
- `/plans/summary.md` (if architecture changes)

## Common Gotchas

- Don't assume file locations - use search tools
- Always check current project structure before making assumptions
- Verify technology choices in tech-stack.md before adding dependencies
- Keep the human/AI context separation clear