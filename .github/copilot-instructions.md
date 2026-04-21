---
description: "Workspace instructions for OctoFit Tracker — a full-stack fitness app built with React, Django, and MongoDB. Use when developing or enhancing OctoFit Tracker features."
---

# OctoFit Tracker Workspace Instructions

## Project Overview

**OctoFit Tracker** is a fitness tracking application designed to help students at Mergington High School monitor and compete in physical activities. Built with modern web technologies, it combines gamification with educational goals.

**Tech Stack:**
- **Frontend:** React.js (JavaScript/TypeScript)
- **Backend:** Python Django with REST API
- **Database:** MongoDB with Django ORM
- **Environment:** GitHub Codespaces

**Key Features:**
- User authentication and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

---

## Quick Navigation

| Area | Reference | Applies To |
|------|-----------|-----------|
| Project Setup | [octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md) | Initial setup, virtual environments, dependencies |
| Django Backend | [octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md) | `octofit-tracker/backend/**` files |
| React Frontend | [octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md) | `octofit-tracker/frontend/**` files |

**Prompts:**
- [create-django-project.prompt.md](.github/prompts/create-django-project.prompt.md) — Set up a new Django project structure
- [init-populate-octofit_db.prompt.md](.github/prompts/init-populate-octofit_db.prompt.md) — Initialize and populate the database

---

## Essential Configuration

### Port Forwarding (GitHub Codespaces)

These ports are forwarded for OctoFit Tracker development:

| Port | Visibility | Service | Usage |
|------|------------|---------|-------|
| **3000** | Public | Frontend (React) | Development server |
| **8000** | Public | Backend (Django) | API endpoints |
| **27017** | Private | MongoDB | Database (internal only) |

⚠️ **Never modify or add additional port forwards without discussion.**

### Directory Structure

```
octofit-tracker/
├── backend/
│   ├── venv/                 # Python virtual environment
│   ├── octofit_tracker/      # Django project root
│   └── requirements.txt      # Python dependencies
└── frontend/
    └── src/                  # React source code
```

### Terminal Commands

**When running commands, never change directories.** Instead, point to the target directory:

```bash
# ✅ GOOD: Point to directory without changing cwd
source octofit-tracker/backend/venv/bin/activate && python {target_dir}/manage.py runserver

# ❌ BAD: Changing directories
cd octofit-tracker/backend && python manage.py runserver
```

This ensures reliable terminal sessions and prevents context loss in agent mode.

---

## Development Workflow

### Backend (Django)

1. Activate virtual environment: `source octofit-tracker/backend/venv/bin/activate`
2. Run migrations: `python octofit-tracker/backend/octofit_tracker/manage.py migrate`
3. Start dev server: `python octofit-tracker/backend/octofit_tracker/manage.py runserver 0.0.0.0:8000`

**Database:** Always use Django's ORM—never execute direct MongoDB scripts.

### Frontend (React)

1. Navigate to frontend: `cd octofit-tracker/frontend`
2. Install dependencies: `npm install` (if not already done)
3. Start dev server: `npm start` (runs on port 3000)

### Database (MongoDB)

- Verify MongoDB is running: `ps aux | grep mongod`
- MongoDB official package: `mongodb-org`
- MongoDB client tool: `mongosh`
- **Important:** Manage database structure via Django, not direct scripts

---

## Common Patterns & Conventions

### Virtual Environment Management

- Use `python3 -m venv octofit-tracker/backend/venv` to create
- Activation: `source octofit-tracker/backend/venv/bin/activate`
- Dependencies: Install from `requirements.txt` via `pip install -r`

### Code Organization

- Backend models and views follow Django conventions in `octofit_tracker/`
- Frontend components organized in React structure
- Cross-cutting concerns documented in respective instructions

### Testing

- Backend tests use Django's test framework
- Frontend tests use Jest or React Testing Library
- Run tests before committing changes

---

## Troubleshooting Reference

| Issue | Solution |
|-------|----------|
| **"Command not found: mongod"** | Ensure `mongodb-org` service is started; check with `ps aux \| grep mongod` |
| **"ModuleNotFoundError" in Python** | Activate venv and verify dependencies: `pip list` |
| **Port 3000/8000 already in use** | Kill process: `lsof -ti:PORT \| xargs kill -9` |
| **Django migration errors** | Clear and reapply: `python manage.py migrate` |
| **Node dependencies issues** | Clear cache: `npm cache clean --force && npm install` |

---

## Phase-Based Development

### Phase 1: Setup & Infrastructure
- Follow [octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md)
- Complete environment initialization
- Verify all ports are forwarded

### Phase 2: Backend Development
- Refer to [octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md)
- Create models, views, and API endpoints
- Use `/create-django-project.prompt.md` for scaffolding

### Phase 3: Frontend Development
- Refer to [octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md)
- Build components and user interfaces
- Connect to backend via REST API

### Phase 4: Integration & Testing
- Test full-stack workflows
- Use `/init-populate-octofit_db.prompt.md` for test data

---

## Agent Mode Best Practices

When using GitHub Copilot agent mode with this project:

1. **Use specific instructions** — Always reference the relevant `.instructions.md` file for your context
2. **Avoid directory changes** — Point to paths instead of using `cd`
3. **Verify ports** — Ensure only the three specified ports are used
4. **Use Django ORM** — All database operations through Django models
5. **Link documentation** — Reference specific sections rather than repeating guidance

---

## Support & Next Steps

For detailed guidance on specific areas:

- **Setting up the project?** → Read [octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md)
- **Building backend features?** → Read [octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md)
- **Building frontend features?** → Read [octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md)
- **Need a scaffolding prompt?** → Use [`/create-django-project`](.github/prompts/create-django-project.prompt.md) or [`/init-populate-octofit_db`](.github/prompts/init-populate-octofit_db.prompt.md)

---

## Related Resources

- [OctoFit Story & Project Context](docs/octofit_story.md)
- [GitHub Copilot Chat Documentation](https://docs.github.com/en/copilot/how-tos/use-chat/)
- [Django REST Framework Guide](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [MongoDB Documentation](https://docs.mongodb.com/)
