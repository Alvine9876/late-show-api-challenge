#  Late Show API

A RESTful Flask API for managing a late night TV show — with guest appearances, episode listings, JWT authentication, and PostgreSQL database support.


##  Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL
- Pipenv
- Postman (for testing)


## 🚀 Setup Instructions

### 1. Clone the repo & navigate into it

```bash
git clone https://github.com/Alvine9876/late-show-api-challenge
cd late-show-api-challenge
```
 Install dependencies
```bash
pipenv install
pipenv shell
```
Set environment variables (create .env)

DATABASE_URI=postgresql://postgres:<your_password>@localhost:5432/late_show_db
JWT_SECRET_KEY=supersecret

Create PostgreSQL database

## Initialize and migrate database
```bash

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
 Seed the database
```bash

python server/seed.py
```
## Auth Flow
Register 
Login

## Postman
Import challenge-4-lateshow.postman_collection.json into Postman.

Run through each route:
  -Register/login
  -Copy the token
  -Test protected routes with Authorization: Bearer <token>

