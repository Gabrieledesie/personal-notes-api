My Pseudo Code for My Capstone project

 Setup & Boilerplate

Step 1: Start my Django project
- I will create a new Django project called notes_api
- Inside it, I will create three apps: users, notes, and followers

Step 2: Install required libraries
- I need Django REST Framework (DRF) for building APIs
- I need SimpleJWT for JWT authentication
- I need drf-yasg to automatically generate Swagger API documentation
- I need psycopg2-binary in case I use PostgreSQL

Step 3: Connect apps to Django
- I will add 'rest_framework', 'rest_framework_simplejwt', 'drf_yasg' to INSTALLED_APPS
- I will also add my own apps: 'users', 'notes', 'followers'

Step 4: Configure REST Framework
- I will set REST_FRAMEWORK in settings.py
- I will tell it to use JWTAuthentication for all API endpoints


User Registration & Auth

Step 1: Make my User model
- I want users to log in with email, so I will extend Django's AbstractUser
- I will make email a required and unique field
- I will tell Django to use my custom User model in settings.py with AUTH_USER_MODEL

Step 2: Make serializers for user actions
- Create a serializer to register a new user
- Create a serializer to log in and get a JWT token
- Create a serializer to refresh the token when it expires
- Create a serializer to show the current user info (me)

Step 3: Connect JWT authentication
- I will use SimpleJWT to handle token creation and verification
- Add authentication classes to Django REST Framework settings
- Make sure my API endpoints only allow authenticated users where needed


Notes CRUD

Goal: I want users to be able to create, read, update, and delete their notes

Steps I followed

Create a Note model and link it to the User model

Add fields for the note: title, content, created_at, updated_at


Make API endpoints so users can: list all notes, create a new note, get a single note, update a note, and delete a note


Create a Note model for my app
Connect the Note model to the User model
Add fields for title, content, created_at, updated_at
Build API endpoints to: list all notes, create a note, view a note, update a note, delete a note

Follow/Unfollow
Users can follow/unfollow others and see followers/following lists.

define a Follow model that links a follower to a user they follow
make sure the same follower-following pair cannot be duplicated
add API endpoints for following and unfollowing users
add API endpoints to view a user’s followers and who they are following

POST /api/users/{id}/follow/ to follow a user
DELETE /api/users/{id}/follow/ to unfollow a user
GET /api/users/{id}/followers/ to list all followers of a user
GET /api/users/{id}/following/ to list all users someone is following

Feed
Show notes from users the current user follows.

Algorithm / Steps
get current user
get list of users current user follows
query notes where author is in that list
order notes by created_at descending
apply pagination to results
return notes as API response

Testing
description of your testing plan

I will create tests to check if my app is working well.
The tests will be inside tests.py in each app.
I will test 4 things:

Auth (register, login, refresh token)

Notes (create, read, update, delete)

Follow/Unfollow

Feed endpoint

Authentication Test and Pseudo code

make a test user
test register endpoint
test login endpoint
test token refresh




