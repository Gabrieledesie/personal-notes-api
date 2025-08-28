+------------------------------------------------+
|                      User                      |
+------------------------------------------------+
| id (PK, int, auto)                             |
| username (varchar(150), unique, indexed)       |
| email (varchar(254), unique, indexed)          |
| password_hash (char, salted)                   |
| date_joined (datetime, default=now)            |
| last_login (datetime, null)                    |
+------------------------------------------------+
      | |
      | +------------------+
      | |    Following-id  |
      | +------------------+
      | |                  |
+-----v-v------------------+
|      Follow              |
+--------------------------+
| id (PK, int, auto)       |
| follower_id (FK -> User.id, indexed) |
| following_id (FK -> User.id, indexed) |
| created_at (datetime, default=now) |
| UNIQUE (follower_id, following_id) |
| CHECK (follower_id != following_id) |
+--------------------------+
      ^
      |
      | +------------------+
      | |    Follower-id   |
      | +------------------+
      |
+------------------------------------------------+
|                      Note                      |
+------------------------------------------------+
| id (PK, int, auto)                             |
| author_id (FK -> User.id, indexed, ON DELETE CASCADE) |
| title (varchar(120), not null)                 |
| content (text, not null)                       |
| created_at (datetime, indexed, default=now)    |
| updated_at (datetime, auto)                    |
+------------------------------------------------+

+------------------------------------------------+
|                      Key                       |
+------------------------------------------------+
| PK = Primary Key                               |
| FK = Foreign Key                               |
| Unique = Unique constant                       |
+------------------------------------------------+

Phase 5 – Documentation

Create a file called README.md in the project folder


Project Title

Personal Notes API
A Django REST API to manage personal notes with users and followers


Project Description

Users can register and login

Users can create, read, update, delete notes

Users can follow and unfollow other users

API uses JWT for secure access


Features

User registration and login using JWT

Notes create, read, update, delete

Follow and unfollow system

Secure API endpoints

Example requests and responses


Installation

Clone the project
git clone https://github.com/Gabrieledesie/personal-notes-api.git

Go to project folder
cd personal-notes-api

Create and activate virtual environment
python -m venv notes-venv310
source notes-venv310/Scripts/activate (Windows)

Install dependencies
pip install -r requirements.txt

Run migrations
python manage.py makemigrations
python manage.py migrate

Start the server
python manage.py runserver

API Endpoints

Auth
POST /api/users/register/ → register a new user
POST /api/token/ → get JWT tokens
POST /api/token/refresh/ → refresh JWT token

Notes
GET /api/notes/ → list notes
POST /api/notes/ → create note
PUT /api/notes/{id}/ → update note
DELETE /api/notes/{id}/ → delete note

Followers
POST /api/followers/follow/ → follow a user
POST /api/followers/unfollow/ → unfollow a user

Example Request and Response

Example: Create Note

POST /api/notes/
{
"title": "My First Note",
"content": "ALX has thought me GRIT."
}

Response
{
"id": 1,
"title": "My First Note",
"content": "ALX has thought me GRIT.",
"author": 1,
"created_at": "2025-08-27T13:00:00Z",
"updated_at": "2025-08-27T13:00:00Z"
}