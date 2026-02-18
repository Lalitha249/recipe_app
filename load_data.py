import json
from app import app
from extensions import db
from models import Recipe

with app.app_context():
    if Recipe.query.first():
        print("Data already exists. Skipping insert.")
    else:
        with open("US_recipes_null.json", "r") as file:
            data = json.load(file)

        for key in data:
            item = data[key]

            recipe = Recipe(
                cuisine=item.get('cuisine'),
                title=item.get('title'),
                rating=item.get('rating'),
                prep_time=item.get('prep_time'),
                cook_time=item.get('cook_time'),
                total_time=item.get('total_time'),
                description=item.get('description'),
                nutrients=item.get('nutrients'),
                serves=item.get('serves')
            )

            db.session.add(recipe)

        db.session.commit()
        print("Data loaded successfully")
