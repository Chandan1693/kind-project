from flask import Flask, render_template_string, url_for

app = Flask(__name__)

clothing_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Clothing</title>
    <style>
        .clothing-image {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h1>Clothing Microservice</h1>
    <p>Welcome to the clothing microservice!</p>
    <img src="{{ url_for('static', filename='clothing.jpg') }}" alt="Clothing Image" class="clothing-image">
    <a href="/">Home</a>
</body>
</html>
"""

@app.route("/")
def home():
    return "<h1>Welcome to the Clothing Microservice!</h1>"

@app.route("/clothing")
def clothing():
    return render_template_string(clothing_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
