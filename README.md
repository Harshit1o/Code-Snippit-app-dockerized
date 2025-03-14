# Code Snippet Expiry System

A Django-based web application that allows users to share code snippets with automatic expiration functionality. Built with a beautiful dark purple theme and modern UI.

## Features

- 🎨 Beautiful dark mode UI with purple theme
- ⏰ Automatic snippet expiration (1 hour, 1 day, 1 week)
- 🔥 Syntax highlighting for multiple programming languages
- 🚀 RESTful API for programmatic access
- 🐳 Docker support for easy deployment
- 🔄 Automatic cleanup of expired snippets

## Quick Start

### Local Development

1. Clone the repository:
```bash
git clone git@github.com:Harshit1o/Code-Snippit-app-dockerized.git
cd code-expiry
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

### Docker Setup

1. Build and run using Docker:
```bash
docker-compose up --build
```

2. Access the application at http://localhost:8080

## API Endpoints

- `POST /api/snippets/`: Create a new snippet
- `GET /api/snippets/`: List all active snippets
- `GET /api/snippets/<id>/`: Get specific snippet
- `DELETE /api/snippets/<id>/`: Delete a snippet

## Environment Variables

Create a `.env` file with the following variables:

```env
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DOCKER_PORT=8080
```

## Project Structure

```
code_expiry/
├── code_expiry/          # Project settings
├── snippets/             # Main application
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── views.py         # Views
│   └── urls.py          # URL routing
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
└── docker-compose.yml  # Docker compose file
```

## Tech Stack

- Python 3.11
- Django 5.0.2
- Django REST Framework
- SQLite (default database)
- Docker
- HTML/CSS/JavaScript
- Prism.js for syntax highlighting 
