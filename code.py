from flask import Flask, render_template_string

app = Flask(__name__)

home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to My App</h1>
    <a href="/shop"><button>Shop</button></a>
    <a href="/account"><button>Account</button></a>
</body>
</html>
"""

shop_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Shop</title>
</head>
<body>
    <h1>Shop Page</h1>
    <p>Welcome to the shop page!</p>
    <a href="/"><button>Home</button></a>
</body>
</html>
"""

account_page = """
<!DOCTYPE html>
<html>
head>
    <title>Account</title>
</head>
<body>
    <h1>Account Page</h1>
    <p>Welcome to your account page!</p>
    <a href="/"><button>Home</button></a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(home_page)

@app.route("/shop")
def shop():
    return render_template_string(shop_page)

@app.route("/account")
def account():
    return render_template_string(account_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
