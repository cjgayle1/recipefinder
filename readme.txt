Some interesting thoughts which the finder does not account for. Not sure if it will account for the difference between something like red pepper and black pepper or something like that.

I'm going to remove all instances of oil and salt cuz who doesn't have that if they are going to cook. I'm thinking that could potentially improve search by being more specific.

Potential limitation of this model:
if i have a list like: "egg", "bacon", "red bell pepper", "spinach" it will make it egg bacon red bell pepper spinach. This means that red bell and pepper will no longer be associated with one another rords together represent a single ingredient.
The model loses the context that these words together represent a single ingredien and this is a known limitation when using simple text processing methods like TF-IDF for ingredients lists but for this case I still believe that it will
outperform using an N-grams solution as explained here:

One way to mitigate this issue is to use n-grams with TfidfVectorizer. N-grams are combinations of adjacent words in your text, where n defines the number of words in the combination. For example, using 2-grams,
 "red bell pepper" could be represented as "red bell" and "bell pepper", helping to preserve some context between the words.
 