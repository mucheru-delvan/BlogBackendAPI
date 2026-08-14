Absolutely. Since this is your **BlogBackendAPI** project, the README should explain the project clearly while showing that you actually implemented the requirements—not just copy the original assignment.

# BlogBackendAPI

A RESTful API for a personal blogging platform built with **Python, Django REST Framework, and MySQL**.

The API provides the core CRUD operations required for managing blog posts, including creating, retrieving, updating, deleting, and searching posts.

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
* **Django REST Framework (DRF)**
* **MySQL**
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

Posts can be filtered using a search term.

```http
GET /posts/?term=tech
```

The search checks the:

* Title
* Content
* Category

For example, a search for `tech` returns posts where `tech` appears in one of those fields.

## HTTP Status Codes

The API uses standard HTTP status codes:

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
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mucheru-delvan/BlogBackendAPI.git
cd BlogBackendAPI
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If using `uv`:

```bash
uv sync
```

Or install the required packages manually:

```bash
pip install django djangorestframework mysqlclient
```

### 4. Configure the database

Create a MySQL database and configure the database credentials in `settings.py`.

Do **not** commit database passwords or other secrets to GitHub. Use environment variables for sensitive configuration.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Testing the API

You can test the API using tools such as:

* Postman
* cURL
* Django REST Framework's browsable API

Example:

```bash
curl http://127.0.0.1:8000/posts/
```

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
* Backend project structure

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
