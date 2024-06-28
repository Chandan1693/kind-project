from flask import Flask, render_template_string, url_for

app = Flask(__name__)

clothing_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Clothing</title>
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
        .clothing-image {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto; /* Adjusted margin */
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
    <h1>Clothing Microservice</h1>
    <p>Welcome to the <span style="color: #007bff;">clothing microservice</span>!</p>
    <img src="{{ url_for('static', filename='clothes.jpg') }}" alt="Clothing Image" class="clothing-image">
    <br>
    <a href="/">Home</a>
</body>
</html>
"""

@app.route("/clothing")
def home():
    return "<h1>Welcome to the Clothing Microservice!</h1>"

@app.route("/clothing")
def clothing():
    return render_template_string(clothing_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

