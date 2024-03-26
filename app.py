from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Load your dataset here
kdramas_df = pd.read_csv('kdrama.csv')
# Assume all other preprocessing steps have been done here...

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Process the form data and return recommendations
        drama_name = request.form.get('drama_name')
        # Insert the logic of your recommendation function here
        # Use the drama_name to get recommendations
        recommendations = recommend_kdramas_interactive(drama_name)  # This needs to be adapted for web usage
        return render_template('results.html', recommendations=recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
