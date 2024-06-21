from flask import Flask, render_template_string

app = Flask(__name__)

food_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Food</title>
</head>
<body>
    <h1>Food Microservice</h1>
    <p>Welcome to the food microservice!</p>
    <a href="/">Home</a>
</body>
</html>
"""

@app.route("/")
def home():
    return "Welcome to the Food Microservice!"

@app.route("/food")
def food():
    return render_template_string(food_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
