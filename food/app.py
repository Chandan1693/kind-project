from flask import Flask, render_template_string

app = Flask(__name__)

food_page = """
<!DOCTYPE html>
<html>
<head>
    <title><span style="color: #FF5733;">Food</span></title>
</head>
<body>
    <h1 style="color: #FF5733;">Food Microservice</h1>
    <p>Welcome to the <span style="color: #FF5733;">food microservice</span>!</p>
    <a href="/" style="color: #FF5733;">Home</a>
</body>
</html>
"""

@app.route("/")
def home():
    return "<h1 style='color: #FF5733;'>Welcome to the <span style='color: #FF5733;'>Food Microservice!</span></h1>"

@app.route("/food")
def food():
    return render_template_string(food_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
