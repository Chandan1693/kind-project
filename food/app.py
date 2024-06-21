from flask import Flask, render_template_string, url_for

app = Flask(__name__)

food_page = """
<!DOCTYPE html>
<html>
<head>
<<<<<<< HEAD
    <title><span style="color: #FF5733;">Food</span></title>
    <style>
=======
    <title><span style="color: #007bff;">Food</span></title>
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
        .food-image {
            max-width: 100%;
            height: auto;
            display: block;
<<<<<<< HEAD
            margin: 0 auto;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h1 style="color: #FF5733;">Food Microservice</h1>
    <p>Welcome to the <span style="color: #FF5733;">food microservice</span>!</p>
    <img src="{{ url_for('static', filename='food.jpg') }}" alt="Food Image" class="food-image">
    <a href="/" style="color: #FF5733;">Home</a>
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
    </style>
</head>
<body>
    <h1>Food Microservice</h1>
    <p>Welcome to the <span style="color: #007bff;">food microservice</span>!</p>
    <img src="{{ url_for('static', filename='food.jpg') }}" alt="Food Image" class="food-image">
    <br>
    <a href="/">Home</a>
>>>>>>> origin/build
</body>
</html>
"""

@app.route("/")
def home():
<<<<<<< HEAD
    return "<h1 style='color: #FF5733;'>Welcome to the <span style='color: #FF5733;'>Food Microservice!</span></h1>"
=======
    return "<h1>Welcome to the Food Microservice!</h1>"
>>>>>>> origin/build

@app.route("/food")
def food():
    return render_template_string(food_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
