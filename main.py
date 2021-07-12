from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "7ad2d8ahdo179ad2hd0awodnq2"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
