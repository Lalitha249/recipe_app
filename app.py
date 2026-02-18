from flask import Flask,request,jsonify
from config import Config
from extensions import db
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
from models import Recipe  

@app.route('/')
def home():
    return "Recipe api is running"

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    query = Recipe.query.order_by(Recipe.rating.desc())
    total = query.count()
    recipes = query.offset((page - 1) * limit).limit(limit).all()
    data = []
    for r in recipes:
        data.append({
            "id": r.id,
            "title": r.title,
            "cuisine": r.cuisine,
            "rating": r.rating,
            "prep_time": r.prep_time,
            "cook_time": r.cook_time,
            "total_time": r.total_time,
            "description": r.description,
            "nutrients": r.nutrients,
            "serves": r.serves
        })

    return jsonify({
        "page": page,
        "limit": limit,
        "total": total,
        "data": data
    })

@app.route('/api/recipes/search')
def search_recipes():

    title = request.args.get('title')
    cuisine = request.args.get('cuisine')
    rating = request.args.get('rating')
    total_time = request.args.get('total_time')

    recipes = Recipe.query.all()
    result = []

    for r in recipes:
        if title:
            if not r.title or title.lower() not in r.title.lower():
                continue
        if cuisine:
            if not r.cuisine or cuisine.lower() != r.cuisine.lower():
                continue
        if rating:
            if not r.rating or r.rating < float(rating):
                continue
        if total_time:
            if not r.total_time or r.total_time > int(total_time):
                continue
        result.append({
            "id": r.id,
            "title": r.title,
            "cuisine": r.cuisine,
            "rating": r.rating,
            "total_time": r.total_time
        })

    return jsonify(result)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
