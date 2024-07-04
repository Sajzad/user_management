# User Management API with DRF

This Django project demonstrates how to use custom middleware, permissions, and serializers to manage API access based on user roles. It also includes Swagger for API documentation.

## Features

- Custom authentication using tokens
- Custom middleware to log request details
- Different serializers and permissions based on HTTP methods
- Swagger for API documentation

## Setup

### Prerequisites

- Python 3.7+
- Pipenv

### Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install Dependencies**

    Use Pipenv to create a virtual environment and install the required packages.

    ```sh
    pipenv install
    pipenv shell
    ```

3. **Apply Migrations**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a Superuser**

    ```sh
    python manage.py createsuperuser
    ```

5. **Run the Development Server**

    ```sh
    python manage.py runserver
    ```
6. **Access the admin panel at**
   http://127.0.0.1:8000/admin/

6. **Usage**
   To make a request with a token:

   Access the Swagger documentation at:
    http://127.0.0.1:8000/swagger/
  OR
   curl -X 'GET' \
  'http://127.0.0.1:8000/API/users/' \
  -H 'accept: application/json' \
  -H 'authentication_token: your_token_here'

  Replace your_token_here with the actual token value.

