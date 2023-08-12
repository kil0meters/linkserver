from flask import Flask, render_template
import os
import random

links = []

colors = [
    "rgb(60, 189, 176)",
    "rgb(190, 84, 60)",
    "rgb(190, 181, 60)",
    "rgb(190, 60, 92)",
    "rgb(121, 60, 190)",
]

# e.g. LINK1="Sonarr; https://google.com"

for key, value in os.environ.items():
    if key.startswith("LINK"):
        name, url = value.split("; ")
        links.append({"name": name, "url": url})

links.sort(key=lambda link: link["name"])

app = Flask(__name__)

@app.route("/")
def index():
    excluded_color = random.choice(colors)
    for link in links:
        new_color = random.choice(colors)
        while new_color == excluded_color:
            new_color = random.choice(colors)
        excluded_color = new_color

        link["color"] = new_color

    return render_template("index.html", data=links)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
