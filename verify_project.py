import os

checklist = {
    "Phase 1 – Project Setup": {
        "Create project folder": True,
        "Initialize Git repository": True,
        "Create virtual environment": True,
        "Activate virtual environment": False,
        "Install Django": True,
        "Install required packages": True,
        "Initialize Django project": True,
        "Initialize Django app": True,
        "Configure settings.py": True,
        "Set up .gitignore": True
    },
    "Phase 2 – Core Features & Models": {
        "Create Note model with fields": True,
        "Apply migrations": True,
        "Create serializers": True,
        "Set up views": True,
        "Configure URLs": True,
        "Test API endpoints": True
    },
    "Phase 3 – Authentication & Permissions": {
        "Registration endpoint": True,
        "Login endpoint": True,
        "JWT refresh endpoint": True,
        "Configure permissions for Note endpoints": True,
        "Only authenticated users can modify notes": True,
        "Users can only access their own notes": True,
        "Test authentication endpoints and permissions": True
    },
    "Phase 4 – Testing": {
        "Write unit tests for auth endpoints": True,
        "Write unit tests for Notes CRUD endpoints": True,
        "Run tests": True,
        "Verify all tests pass": True,
        "Fix any failing tests": False
    },
    "Phase 5 – Documentation": {
        "Create project README": True,
        "Project description": True,
        "Features": True,
        "Installation instructions": True,
        "API endpoints documentation": True,
        "Example requests/responses": True,
        "Optional: ER diagram or models diagram": False
    },
    "Phase 6 – Deployment (PythonAnywhere)": {
        "ALLOWED_HOSTS updated in settings.py": False,
        "STATIC_ROOT configured in settings.py": False,
        "Requirements pinned": True,
        "Deploy project (PythonAnywhere)": True,
        "Open live URL": True,
        "Confirm API endpoints respond": True,
        "Confirm welcome page": True
    },
    "Phase 7 – Version Control": {
        "Commit changes regularly": True,
        "Push all commits to GitHub": True,
        "Ensure repository clean": True
    }
}

key_files = [
    "manage.py",
    "README.md",
    "requirements.txt",
    "notes/models.py",
    "notes/serializers.py",
    "notes/views.py",
    "notes/urls.py",
    "users/models.py",
    "users/views.py",
    "users/tests.py",
    "notes_api/settings.py",
    "notes_api/urls.py"
]

key_folders = [
    "notes",
    "users",
    "notes_api",
    "followers",
    "docs",
    "staticfiles"
]

print("\n====== Personal Notes API – Project Verification ======\n")

leftover_found = False
for phase, tasks in checklist.items():
    leftover = []
    for task, done in tasks.items():
        if not done:
            leftover.append(task)
    if leftover:
        leftover_found = True
        print(phase + " – LEFTOVER ITEMS:")
        for task in leftover:
            print("- " + task + " ⚠️")
        print()

missing_files = []
for f in key_files:
    if not os.path.exists(f):
        missing_files.append(f)

if missing_files:
    leftover_found = True
    print("Missing Key Files:")
    for f in missing_files:
        print("- " + f + " ⚠️")
    print()

missing_folders = []
for d in key_folders:
    if not os.path.exists(d):
        missing_folders.append(d)

if missing_folders:
    leftover_found = True
    print("Missing Key Folders:")
    for d in missing_folders:
        print("- " + d + " ⚠️")
    print()

if not leftover_found:
    print("No leftover items! All checklist items, key files, and folders are complete ✅\n")

print("COMPLETED ITEMS SUMMARY:")
for phase, tasks in checklist.items():
    count = 0
    for task, done in tasks.items():
        if done:
            count += 1
    print(phase + ": " + str(count) + " tasks ✅")

print("\nChecked key files: " + str(len(key_files) - len(missing_files)) + " exist ✅")
if missing_files:
    print("Missing key files: " + str(len(missing_files)) + " ⚠️")

print("Checked key folders: " + str(len(key_folders) - len(missing_folders)) + " exist ✅")
if missing_folders:
    print("Missing key folders: " + str(len(missing_folders)) + " ⚠️")

print("\n======================================================\n")
