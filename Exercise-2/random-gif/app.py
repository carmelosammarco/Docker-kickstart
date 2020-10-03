from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of images
images = [
    "https://media.giphy.com/media/hqsrF8y3F8LYBkWWsU/giphy.gif",
    "https://media.giphy.com/media/l3q2ZC9IsbKpJDhdu/giphy.gif",
    "https://media.giphy.com/media/jq0XL7w1QrwbjYrdqv/giphy.gif",
    "https://media.giphy.com/media/Y0tLQ6EvxI1mvjuJPf/giphy.gif",
    "https://media.giphy.com/media/UUmpYgeWlTA5wRSFuT/giphy.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
