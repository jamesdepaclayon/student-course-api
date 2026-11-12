# Student Course API

A read-only REST API prototype built with Python and Flask for System Integration and Architecture.

## Endpoints
- `GET /api/health` - Check service status
- `GET /api/courses` - List all fictional courses
- `GET /api/courses/<id>` - Get a single course by ID (returns 404 if not found)

## Render Deployment Settings
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
