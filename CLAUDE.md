# AI Assistant Context Guide

This guide helps AI assistants navigate and maintain the project effectively.

## 📍 Context Locations

### Project Understanding

- **Vision & Roadmap**: `/plans/summary.md` - What we're building and why
- **Feature Specifications**: `/plans/epics/*/` - Detailed designs and task tracking

### AI-Specific Context

- **Technology Decisions**: `.llm_context/tech-stack.md` - Tech choices with reasoning
- **Project Structure**: `.llm_context/project-structure.md` - Current organization
- **Development Workflows**: `.llm_context/workflows.md` - How to approach common tasks

## 📝 Documentation Maintenance

When working on the project, update documentation as you go:

### After Implementing Features

- Mark tasks complete in epic `todo.md` files
- Add discoveries/complexities to epic `design.md` files

### After Technology Changes

- Update `.llm_context/tech-stack.md` with new decisions and reasoning
- Keep architectural changes reflected in relevant docs

### After Structural Changes

- Update `.llm_context/project-structure.md` if folder organization changes
- Ensure workflows remain current in `.llm_context/workflows.md`

## 💡 Navigation Tips

- **Don't assume locations** - use search tools to verify current structure
- **Human planning** lives in `/plans/` - focus on vision and roadmap
- **AI context** lives in `.llm_context/` - focus on technical guidance
- **Always preserve reasoning** - document the "why" behind decisions

Documentation is part of the deliverable - keep it current as you work.
