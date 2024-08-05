import re
import unidecode
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# library of known words that don't add any description to a sentence
nltk.download('stopwords')
# lexical english database
nltk.download('wordnet')


def ingredient_parser(ingredients):
    # list of measures and common words to remove
    measures = ["oz", "ounces", "lbs", "lb", "pounds", "pound", "cups", "cup", "teaspoon", "tsp", "teaspoons", "tbsp", "tablespoon", "tablespoons", "ml", "l", "liter", "liters", "g", "grams", "kg", "kilograms"]
    common_words = ["round", "all-purpose", "peeled", "diced", "chopped", "sliced", "cut", "for garnish", "to taste", "as needed", "divided", "plus more", "plus", "new", "small", "large", "into", "preserved", "tsp", "to", "medium", "can", "finely", "oz", "pat", "other", "lb", "thinly", "for", "the", "fresh", "ripe", "shredded", "extra", "extra-virgin", "extra", "virgin", "fresh", "ripe", "shredded", "thinly", "finely", "whole", "crushed", "toasted", "coarsely", "preferably", "roughly", "halved", "ground", "for serving", "for brushing", "serve", "top removed", "for the cake pan", "preferably homemade", "teaspoon", "for the", "and about", "or scant", "minced", "or yellow", "or white", "or vegetable", "thick", "wedges", "piece", "coarsely", "halved crosswise", "thicker stalks", "packages", "preferably fresh", "handful of", "stick", "bunch", "packages", "roasted", "cooked", "reduced sodium", "rinsed until water runs clear", "seeded", "and", "chunk", "minced", "or", "freshly", "coarsely", "for serving", "cup", "fine", "inch dice", "drained", "ground", "shelled", "deveined", "accompaniment", "prepared", "according", "package", "instructions", "but", "without", "dry", "cubed", "a", "firmly", "packed", "at", "room", "temperature", "ingredient", "info", "you", "substitute", "mixed", "for", "the", "tablespoons", "cored", "evenly", "grated", "gran", "room temperature", "goodquality", "sturdy", "torn", "in", "half", "lengthwise", "seeded", "cups", "your", "bowl", "scrubbed", "chilled", "unsalted", "salted", "vegan", "thouroughly", "but", "not", "hot", "water", "such", "as", "grind", "old", "fashioned", "including", "oldfashioned", "dark", "unseasoned", "envelope", "activepan", "goodquality", "patted",  "serving", "optional", "piece", "dried", "extravirgin", "powder", "slice", "serving", "optional", "extract", "cube", "ounce", "melted", "granulated", "pitted", "ice", "rinsed", "strip", "peel", "bay", "inch", "quartered", "removed", "12inch", "flake", "stick", "unsweetened", "crosswise", "taste", "head", "quartered", "cube", "lightly", "plain", "stalk", "thin", "thawed", "beaten", "softened", "cider", "spray", "part", "food", "stock", "additional", "total", "see", "nonstick", "separated", "canned", "cold", "andor", "14inch", "one", "available", "drizzling", "bag", "equipment", "flaky", "kosher", "extra-virgin", "all-purpose", "heavy", "light", "sweet", "golden", "smoked", "raw", "bittersweet", "unsweetened", "lowsodium", "nonstick", "cold", "part", "optional", "serving", "piece", "slice", "cube", "sprig", "flake", "stick", "pinch", "strip", "quartered", "removed", "lightly", "plain", "thin", "thawed", "softened", "additional", "total", "one", "baby", "pure", "tender", "whole", "split", "unpeeled", "de", "frying", "whole-milk", "round", "stemmed", "skin", "skinless", "boneless", "trimmed", "crumbled", "beaten", "melted", "shredded", "dried", "frozen", "chopped", "sliced", "diced", "peeled", "minced", "grated", "zest", "juice", "garnish", "taste", "for brushing", "for serving", "for the cake pan", "for garnish", "to taste", "as needed", "divided", "plus more", "plus", "see note", "store bought", "reserved", "discarded", "supermarket", "allpurpose", "allpurposed"]
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # cleaning and splitting
    cleaned_ingredients = []
    for ingredient in ingredients:

        if "oil" in ingredient or "salt" in ingredient:
            continue

        # lowercase, no more punctuation, non-alpha, and numbers
        ingredient = re.sub(r"[^\w\s]|_", "", unidecode.unidecode(ingredient)).lower()
        ingredient = re.sub(r"[^\w\s]|_", "", ingredient).lower()
        # regex any numbers followed by this 
        ingredient = re.sub(r"\b(\d+[\d/]*|\d+\.\d+)\s*(oz|ounce|ounces|lbs|lb|pounds|pound|cups|cup|teaspoon|tsp|teaspoons|tbsp|tablespoon|tablespoons|ml|l|liter|liters|g|grams|kg|kilograms|inch|inches|inchthick)?\b", "", unidecode.unidecode(ingredient)).lower()


        # split and lemmatize
        words = [lemmatizer.lemmatize(word) for word in ingredient.split() if word not in stop_words and word not in measures and word not in common_words and not word.isdigit()]
        cleaned_ingredients.append(' '.join(words))
    return cleaned_ingredients

# now we get into the good stuff, let's vectorize :D
from sklearn.metrics.pairwise import cosine_similarity

# compute the cosine similarity between user ingredients and recipe ingredients
def recommend_recipes(user_ingredients, tfidf_matrix, tfidf_vectorizer):
    
    # only transform this data as this is the data we are using to query
    user_tfidf = tfidf_vectorizer.transform([' '.join(user_ingredients)])
    # compute cosine similarity scores - measures the cosine of the angle between two vectors (smaller angle means more similar)
    cos_sim_scores = cosine_similarity(user_tfidf, tfidf_matrix)
    print(cos_sim_scores)
    
    num_matches = 100
    # get indices of top num_matches and sort them ascending
    top_matches = cos_sim_scores[0].argsort()[-num_matches:][::-1]
    return top_matches


