from flask import Flask, escape, request

app = Flask(__name__)

# HomePage Route
@app.route('/')
@app.route('/home')
def home():
    return "<h1>Yo World!</h1>"


@app.route('/about')
def about():
    return "<h1>About page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
