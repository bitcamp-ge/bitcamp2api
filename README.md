# Bitcamp2 API

A Backend for Bitcamp2.

## Features

- User registration and authentication
- Interactive courses, lessons, and quizzes
- Spaced repetition learning
- Mentorship through Discord
- Gamification

## Local Development

Follow these steps to set up your local development environment.

### Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)
- Django 3.2 or higher
- Django Rest Framework 3.12 or higher
- A Discord bot token (for mentorship features)

### Setup

1. Clone the repository

    ```bash
    git clone git@github.com:bitcamp-ge/bitcamp2api.git
    ```

2. Install the dependencies

    Navigate to the project directory and run:
    
    ```bash
    pip install -r requirements.txt
    ```

3. Apply the migrations

    ```bash
    python manage.py migrate
    ```

4. Start the server

    ```bash
    python manage.py runserver
    ```

    The application should now be running at `http://localhost:8000`.

## Documentation

API documentation is available at `http://localhost:8000/swagger` when the server is running.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
