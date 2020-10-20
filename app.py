from flask import Flask
from flask import render_template
import json

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    with open('data/products.json') as f:
        data = json.load(f)

    return render_template('index.html', products=data)

# run the application
if __name__ == "__main__":
    app.run(debug=True)