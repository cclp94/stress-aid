from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    str = a + b
    return "HHii!"

if __name__ == "__main__":
    app.run(debug=True)