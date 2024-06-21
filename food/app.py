from flask import Flask, render_template_string

app = Flask(__name__)

food_page = """
<!DOCTYPE html>
<html>
<head>
    <title><span style="color: #FF5733;">Food</span></title>
    <style>
        .food-image {
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
    <h1 style="color: #FF5733;">Food Microservice</h1>
    <p>Welcome to the <span style="color: #FF5733;">food microservice</span>!</p>
    <img src="https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg" alt="Food Image 1" class="food-image">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQua6_rUTN2ZqCO15sjF7Dh15wN14qqavSQbfK5C6aREvPKHq-RFnU3gJ7jh8nNa1pyV2g&usqp=CAU" alt="Food Image 2" class="food-image">
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
