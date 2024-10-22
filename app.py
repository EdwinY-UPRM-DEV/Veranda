from markupsafe import escape
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    name = request.cookies.get('name', 'Guest')
    return render_template('index.html', name=name)

@app.route("/gab",  methods=['GET', 'POST'])
def var_return():
    if request.method == 'POST':
        name = request.form.get('fname')
        response = make_response(redirect(url_for('var_return')))
        response.set_cookie('name', name)  # Store name in a cookie
        return response

    return render_template('return.html')

@app.route('/submit-name', methods=['POST'])
def hello():
    name = request.form['fname'] 
    return f"Hello, {escape(name)}!"


if __name__ == '__main__':
    app.run(debug=True)
