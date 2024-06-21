from flask import Flask, render_template_string

app = Flask(__name__)

clothing_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Clothing</title>
</head>
<body>
    <h1>Clothing Microservice</h1>
    <p>Welcome to the clothing microservice!</p>
    <a href="/">Home</a>
</body>
</html>
"""

@app.route("/")
def home():
    return "Welcome to the Clothing Microservice!"

@app.route("/clothing")
def clothing():
    return render_template_string(clothing_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
