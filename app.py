from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Cloud! Lab01 – Phạm Thành Hưng – 2324802010047</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
