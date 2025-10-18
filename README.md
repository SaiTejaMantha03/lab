# Sri Sai Medical Center - Lab Management System

A Django-based web application for managing medical test bookings and status tracking.

## Features

- 🏥 Medical test booking system
- 📋 Test status tracking
- 👥 User management
- 📱 Responsive design
- 🎨 Modern UI with Bootstrap

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Navigate to the Django project:
   ```bash
   cd lab
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment on Render

This project is configured for easy deployment on Render.com:

1. Fork/clone this repository
2. Connect your GitHub repository to Render
3. Create a new Web Service on Render
4. Use the following settings:
   - **Build Command**: `./build.sh`
   - **Start Command**: `cd lab && gunicorn lab.wsgi:application`
   - **Environment**: Python 3
5. Add environment variables:
   - `SECRET_KEY`: Generate a secure secret key
   - `DEBUG`: Set to `false`
   - `ALLOWED_HOSTS`: Your render domain

## Project Structure

```
lab/
├── lab/                    # Main Django project
│   ├── lab/               # Project settings
│   ├── interface/         # Main app
│   │   ├── templates/     # HTML templates
│   │   ├── static/        # CSS, JS, images
│   │   ├── models.py      # Database models
│   │   ├── views.py       # View functions
│   │   └── urls.py        # URL patterns
│   └── manage.py          # Django management script
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
├── render.yaml           # Render configuration
└── README.md             # This file
```

## Available Tests

The system supports booking for various medical tests including:
- Blood Test
- Urinalysis
- X-ray
- CT Scan
- MRI
- Blood Pressure Measurement
- And many more...

## Technology Stack

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Render.com
- **Static Files**: WhiteNoise

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.