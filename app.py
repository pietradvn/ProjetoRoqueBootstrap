from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
	return render_template("home.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
