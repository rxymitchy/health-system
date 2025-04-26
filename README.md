
# Health Information System

A comprehensive system for managing health programs and client records, with features for enrollment tracking and program management.

## Features

- **Client Management**
  - Register new clients with detailed profiles
  - Edit existing client information
  - Search clients by name, email, or phone
  - View complete client profiles

- **Program Management**
  - Create and manage health programs (TB, Malaria, HIV, etc.)
  - Track program enrollments
  - View active/inactive enrollments

- **Enrollment System**
  - Enroll clients in multiple programs
  - Track enrollment dates and status
  - Modify existing enrollments

## Technologies Used

- **Backend**:
  - Python 3.9+
  - Flask 2.0+
  - SQLAlchemy (ORM)
  - Flask-Migrate (database migrations)

- **Frontend**:
  - Bootstrap 5
  - Jinja2 templating
  - Font Awesome icons

- **Database**:
  - SQLite (development)
  - PostgreSQL (production-ready)

## Installation

### Prerequisites
- Python 3.9+
- pip
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/health-system.git
cd health-system
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
flask db upgrade
```

## Running the Application

### Development
```bash
flask run --debug
```
Access at: http://localhost:5000

### Production
For production deployment, consider using:
- Gunicorn or Waitress (WSGI server)
- Nginx or Apache (reverse proxy)
- PostgreSQL (database)

## Project Structure

```
health-system/
├── app/
│   ├── templates/          # HTML templates
│   ├── static/             # CSS/JS/images
│   ├── __init__.py         # Application factory
│   ├── models.py           # Database models
│   ├── routes.py           # Application routes
│   └── forms.py            # WTForms definitions
├── migrations/             # Database migrations
├── instance/               # Instance folder (database)
├── tests/                  # Test cases
├── .env.example            # Environment variables template
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/clients` | GET | List all clients |
| `/api/clients` | POST | Create new client |
| `/api/clients/<id>` | GET | Get client details |
| `/api/programs` | GET | List all programs |
| `/api/programs` | POST | Create new program |

## Screenshots

<!-- Add actual screenshots later -->
- **Home Dashboard**: Overview of programs and clients
- **Client Management**: Add/edit client information
- **Program Enrollment**: Manage client enrollments

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, contact:  
[Your Name] - [lucianamitchell19@gmail.com]  
Project Link: [https://github.com/yourusername/health-system](https://github.com/yourusername/health-system)
```
