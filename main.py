from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/flashcards')
def projects():
    return render_template("flashcard.html")

@app.route('/journal')
def writing():
    return render_template("reflect.html")

@app.route('/map')
def books():
    return render_template("map.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

