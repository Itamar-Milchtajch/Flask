from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "gohan",
        "title": "my real father ",
        "content_type": "secret",
        "content": "picolo",
        "date_posted" : "December 24, 2004"
    },
    {
        "author": "vegeta black",
        "title": "height",
        "content_type": "embarrassing",
        "content": "1.55",
        "date_posted" : "March 27, 2005"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",title="about")


if __name__ == "__main__":
    app.run()
