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






