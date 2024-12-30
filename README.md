# Flask Microblog

This is a simple blog application built with Flask. Users can register, log in, create posts, follow other users, and view posts from users they follow.

## Features

- User registration and registration
- Create (can't not edit  or delete) posts
- Follow and unfollow other users
- View posts from followed users
- User profile pages
- Edit user profile

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/danghaidang04/microblog.git
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```sh
    set FLASK_APP=app
    set FLASK_ENV=development  # On Windows
    export FLASK_APP=app
    export FLASK_ENV=development  # On macOS/Linux
    ```

5. Initialize the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Run the application:
    ```sh
    flask run
    ```

## Usage

- Open your web browser and go to `http://127.0.0.1:5000/`.
- Register a new user account.
- Log in with your new account.
- Create posts, follow other users, and explore the application.

## Project Structure

- `app/` - Contains the main application code.
  - `models.py` - Database models.
  - `routes.py` - Application routes.
  - `forms.py` - Web forms.
  - `templates/` - HTML templates.
- `migrations/` - Database migration files.
- `venv/` - Virtual environment directory.
- `requirements.txt` - List of dependencies.


## License

This project is licensed under the MIT License.