# BlogBackendAPI

A RESTful API for a personal blogging platform built with **Python, Django REST Framework, and MySQL**.

The API provides core CRUD operations for managing blog posts, including creating, retrieving, updating, deleting, and searching posts.

## Features

* Create a new blog post
* Retrieve a single blog post
* Retrieve all blog posts
* Update an existing blog post
* Delete a blog post
* Search/filter blog posts by title, content, or category
* Validate incoming request data
* Store blog posts and related data in a MySQL database

## Tech Stack

* **Python**
* **Django**
* **Django REST Framework**
* **MySQL**
* **uv** – Python package and project management
* **Git & GitHub**

## API Endpoints

| Method   | Endpoint                     | Description                  |
| -------- | ---------------------------- | ---------------------------- |
| `GET`    | `/posts/`                    | Get all blog posts           |
| `POST`   | `/posts/`                    | Create a new blog post       |
| `GET`    | `/posts/<id>/`               | Get a single blog post       |
| `PUT`    | `/posts/<id>/`               | Update a blog post           |
| `PATCH`  | `/posts/<id>/`               | Partially update a blog post |
| `DELETE` | `/posts/<id>/`               | Delete a blog post           |
| `GET`    | `/posts/?term=<search_term>` | Search blog posts            |

## Blog Post Structure

Each blog post contains:

```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2026-08-14T10:00:00Z",
  "updatedAt": "2026-08-14T10:00:00Z"
}
```

## Creating a Blog Post

### Request

```http
POST /posts/
```

### Request Body

```json
{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}
```

A successful request returns:

```http
201 Created
```

with the newly created blog post.

## Getting All Blog Posts

```http
GET /posts/
```

Returns a list of all blog posts.

```json
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "createdAt": "2026-08-14T10:00:00Z",
    "updatedAt": "2026-08-14T10:00:00Z"
  }
]
```

## Getting a Single Blog Post

```http
GET /posts/1/
```

Returns the blog post with the specified ID.

If the post does not exist:

```http
404 Not Found
```

## Updating a Blog Post

```http
PUT /posts/1/
```

### Request Body

```json
{
  "title": "My Updated Blog Post",
  "content": "This is the updated content.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}
```

A successful update returns:

```http
200 OK
```

## Deleting a Blog Post

```http
DELETE /posts/1/
```

A successful deletion returns:

```http
204 No Content
```

If the post does not exist:

```http
404 Not Found
```

## Searching Blog Posts

Posts can be filtered using a search term:

```http
GET /posts/?term=tech
```

The search checks the:

* Title
* Content
* Category

For example, searching for `tech` returns posts where `tech` appears in the title, content, or category.

## HTTP Status Codes

| Status Code       | Meaning                           |
| ----------------- | --------------------------------- |
| `200 OK`          | Request completed successfully    |
| `201 Created`     | Resource successfully created     |
| `204 No Content`  | Resource successfully deleted     |
| `400 Bad Request` | Invalid request data              |
| `404 Not Found`   | Requested resource does not exist |

## Project Structure

```text
BlogBackendAPI/
├── blog/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── blogAPI/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

This project uses **uv** for Python package and project management.

### 1. Clone the repository

```bash
git clone https://github.com/mucheru-delvan/BlogBackendAPI.git
cd BlogBackendAPI
```

### 2. Install uv

If you do not already have `uv` installed, follow the official installation instructions.

### 3. Install project dependencies

Run:

```bash
uv sync
```

`uv sync` creates the project's virtual environment and installs the dependencies defined in `pyproject.toml` using the versions recorded in `uv.lock`.

### 4. Activate the virtual environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Alternatively, you can run commands through uv without manually activating the environment:

```bash
uv run python manage.py runserver
```

### 5. Configure the database

Create a MySQL database and configure the database connection in your Django settings.

For example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_database_name",
        "USER": "your_database_user",
        "PASSWORD": "your_database_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

**Do not commit database passwords or other secrets to GitHub.** Use environment variables or a `.env` file for sensitive configuration.

### 6. Run migrations

```bash
uv run python manage.py migrate
```

### 7. Start the development server

```bash
uv run python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Testing the API

You can test the API using:

* Postman
* cURL
* Django REST Framework's browsable API

Example:

```bash
uv run python manage.py runserver
```

Then send:

```http
GET http://127.0.0.1:8000/posts/
```

## Dependency Management with uv

To add a new dependency:

```bash
uv add package-name
```

For example:

```bash
uv add djangorestframework
```

To add a development dependency:

```bash
uv add --dev package-name
```

To remove a dependency:

```bash
uv remove package-name
```

To update project dependencies:

```bash
uv lock
uv sync
```

The `pyproject.toml` file defines the project's dependencies, while `uv.lock` locks their exact versions for reproducible installations.

## Project Goal

This project was built to demonstrate practical understanding of:

* RESTful API design
* CRUD operations
* Django REST Framework
* HTTP methods
* HTTP status codes
* Serialization and validation
* Database relationships
* Querying and filtering
* API testing
* Python project and dependency management with uv

## Future Improvements

Possible improvements include:

* User authentication
* Authorization and permissions
* Pagination
* Advanced search
* API documentation with Swagger/OpenAPI
* Automated tests
* Rate limiting
* Deployment to a production server

## License

This project is for educational and portfolio purposes.
