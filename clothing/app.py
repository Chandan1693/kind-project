from flask import Flask, render_template_string, url_for

app = Flask(__name__)

clothing_page = """
<!DOCTYPE html>
<html>
<head>
<<<<<<< HEAD
    <title>Clothing</title>
    <style>
=======
    <title><span style="color: #007bff;">Clothing</span></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            text-align: center;
            padding: 40px;
        }
        h1 {
            color: #007bff;
            font-size: 2.5em;
        }
>>>>>>> origin/build
        .clothing-image {
            max-width: 100%;
            height: auto;
            display: block;
<<<<<<< HEAD
            margin: 0 auto;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
=======
            margin: 20px auto;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
            margin-top: 20px;
            display: inline-block;
            padding: 10px 20px;
            border: 2px solid #007bff;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        a:hover {
            background-color: #007bff;
            color: #fff;
        }
>>>>>>> origin/build
    </style>
</head>
<body>
    <h1>Clothing Microservice</h1>
<<<<<<< HEAD
    <p>Welcome to the clothing microservice!</p>
    <img src="{{ url_for('static', filename='clothing.jpg') }}" alt="Clothing Image" class="clothing-image">
=======
    <p>Welcome to the <span style="color: #007bff;">clothing microservice</span>!</p>
    <img src="{{ url_for('static', filename='clothes.jpg') }}" alt="Clothing Image" class="clothing-image">
    <br>
>>>>>>> origin/build
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
