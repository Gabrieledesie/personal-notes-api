Personal Notes API

This is a Django REST API hosted on PythonAnywhere. It lets users create and view notes and follow other users to share notes. It uses JWT for secure access.

About the Project

The API helps users save personal notes and connect with others by following them. It’s built with Django REST Framework and runs on PythonAnywhere. Users log in with a username and password to get a JWT token, then use it to create notes or follow others.

Features

- Log in with JWT to get an access token
- Create and list notes
- Follow other users by username
- List who you follow
- Secure endpoints with JWT
- Example requests and responses

Database Schema

User Table
- id: Integer, primary key, auto-increment
- username: String (150), unique
- email: String (254), unique
- password_hash: String, salted
- date_joined: DateTime, default now
- last_login: DateTime, can be null

Note Table
- id: Integer, primary key, auto-increment
- author: ForeignKey to User.id, deletes if user is deleted
- title: String (120), required
- content: Text, required
- created_at: DateTime, default now
- updated_at: DateTime, auto-updated

Follow Table
- id: Integer, primary key, auto-increment
- follower: ForeignKey to User.id
- following: ForeignKey to User.id
- created_at: DateTime, default now
- Unique: follower and following together must be unique

How to Install Locally

1. Clone the project:
   git clone https://github.com/Gabrieledesie/personal-notes-api.git
   cd personal-notes-api

2. Create and activate a virtual environment (use Python 3.10):
   python -m venv notes-venv310
   source notes-venv310/bin/activate  # Linux or PythonAnywhere
   source notes-venv310/Scripts/activate  # Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Start the server:
   python manage.py runserver

How to Deploy on PythonAnywhere

The API is live at https://gabrieledesie.pythonanywhere.com. To deploy:
1. Upload the project to PythonAnywhere.
2. Set up a virtual environment with Python 3.10.
3. Install requirements.txt.
4. Update the WSGI file and run migrations.

Project Files

- manage.py: Runs Django commands
- requirements.txt: Lists dependencies
- users/models.py: Defines User model
- notes/models.py: Defines Note model
- followers/models.py: Defines Follow model
- notes/views.py: Handles note API requests
- followers/views.py: Handles follower API requests
- notes/serializers.py: Formats note data
- followers/serializers.py: Formats follower data
- personal_notes_api.postman_collection.json: Postman tests

API Endpoints

Auth
- POST /api/token/: Get JWT token for login

Notes
- POST /api/notes/: Create a new note
- GET /api/notes/: List all notes

Followers
- POST /api/followers/: Follow a user
- GET /api/followers/: List followers

Example Requests and Responses

1. Get Access Token
Request:
POST https://gabrieledesie.pythonanywhere.com/api/token/
Content-Type: application/json
Authorization: Basic Gabrieledesie:Gabrieledesie
{
    "username": "Gabrieledesie",
    "password": "Gabby247"
}

Response:
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

2. Create Note
Request:
POST https://gabrieledesie.pythonanywhere.com/api/notes/
Content-Type: application/json
Authorization: Bearer <access_token>
{
    "title": "My First Note",
    "content": "This is a test note.",
    "author": 1
}

Response:
{
    "id": 5,
    "title": "My First Note",
    "content": "This is a test note.",
    "created_at": "2025-08-31T12:46:51.473317Z",
    "updated_at": "2025-08-31T12:46:51.473359Z",
    "author": 1
}

3. List Notes
Request:
GET https://gabrieledesie.pythonanywhere.com/api/notes/
Authorization: Bearer <access_token>

Response:
[
    {
        "id": 1,
        "title": "My First Note",
        "content": "This is a test note.",
        "created_at": "2025-08-31T11:20:47.833396Z",
        "updated_at": "2025-08-31T11:20:47.833439Z",
        "author": 1
    },
    ...
]

4. Follow User
Request:
POST https://gabrieledesie.pythonanywhere.com/api/followers/
Content-Type: application/json
Authorization: Bearer <access_token>
{
    "follower": "Gabrieledesie",
    "following": "gabrieledesie2"
}

Response:
{
    "follower": "Gabrieledesie",
    "following": "gabrieledesie2",
    "created_at": "2025-08-31T12:47:13.591020Z"
}

5. List Followers
Request:
GET https://gabrieledesie.pythonanywhere.com/api/followers/
Authorization: Bearer <access_token>

Response:
[
    {
        "follower": "Gabrieledesie",
        "following": "gabrieledesie2",
        "created_at": "2025-08-31T12:47:13.591020Z"
    }
]

Testing

I tested the API with Postman. I fixed issues like wrong URLs (e.g., /api/ instead of /api/notes/) and wrong field names in the follower serializer (e.g., used usernames instead of IDs). No bugs remain as of August 31, 2025.

Demo

I made a Loom video showing all endpoints working in Postman.

Contact

Reach me on GitHub: https://github.com/Gabrieledesie


Database Schema

User Table
+---------------------------------------------+
| User                                        |
+---------------------------------------------+
| id: Integer, PK, auto-increment             |
| username: String(150), unique               |
| email: String(254), unique                  |
| password_hash: String, salted               |
| date_joined: DateTime, default=now          |
| last_login: DateTime, nullable              |
+---------------------------------------------+
        |                        |
        |                        |
        | author                 | follower
        |                        |
        v                        v
Note Table                Follow Table
+---------------------------------------------+    +---------------------------------------------+
| Note                                        |    | Follow                                      |
+---------------------------------------------+    +---------------------------------------------+
| id: Integer, PK, auto-increment             |    | id: Integer, PK, auto-increment             |
| author: FK -> User.id, ON DELETE CASCADE    |    | follower: FK -> User.id                     |
| title: String(120), not null                |    | following: FK -> User.id                    |
| content: Text, not null                     |    | created_at: DateTime, default=now           |
| created_at: DateTime, default=now           |    | UNIQUE(follower, following)                 |
| updated_at: DateTime, auto-updated          |    +---------------------------------------------+
+---------------------------------------------+            ^
                                                          |
                                                          | following
                                                          |
                                                          User Table (above)

Key
- PK: Primary Key
- FK: Foreign Key
- UNIQUE: Unique constraint