📌 Recipe API
This project is a simple backend API built using Flask and SQLite.

It provides:
    Pagination support
    Sorting by rating
    Search functionality
    JSON API responses

⚙️ Technologies Used

Python
Flask
Flask-SQLAlchemy
SQLite

 How to Run the Project
    Clone the repository:
            git clone https://github.com/Lalitha249/recipe_app.git

   Navigate into project folder:
      cd recipe_app
     Create virtual environment:
        python -m venv venv
   Activate virtual environment:

Windows:
     venv\Scripts\activate


Install dependencies:
   pip install -r requirements.txt

Run the application:
     python app.py


The server will run at:

http://127.0.0.1:5000

📖 API Endpoints
1️⃣ Get Recipes (Pagination)
GET /api/recipes?page=1&limit=10


Returns paginated and sorted recipes.

2️⃣ Search Recipes
GET /api/recipes/search?title=peach&rating=4


Filters recipes based on:
title (partial match)
cuisine
rating
total_time

🗄 Database
The project uses SQLite database:
recipes.db
