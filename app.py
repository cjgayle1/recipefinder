from flask import Flask, render_template, request, make_response
from better_finder import ingredient_parser, recommend_recipes
import pandas as pd
from flask_cors import CORS

from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "https://christopher-gayle.com"}})

# get normalized ingredients
df = pd.read_csv('recipes/normalized_ingredients.csv')


# vectorize the column with the preprocessed ingredients
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['NormalizedIngredients'])
print(tfidf_matrix.shape)

@app.after_request
def apply_referrer_policy(response):
    response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_ingredients = request.form['ingredients'].split(',')
    # found_recipes = search_recipes(user_ingredients, df)

    cleaned_user_ingredients = ingredient_parser(user_ingredients)
    top_recipes_indices = recommend_recipes(cleaned_user_ingredients, tfidf_matrix, tfidf_vectorizer)

    recommended_recipes = df.iloc[top_recipes_indices]
    recipes_list = recommended_recipes.to_dict('records')

    # pass recipes to template
    return render_template('results.html', recipes=recipes_list)

    # return render_template('results.html', recipes=found_recipes[:10])  # Display top 10 results

if __name__ == '__main__':
    app.run(debug=True)
