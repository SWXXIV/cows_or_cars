# from flask import Flask
# from flask_wtf import FLa
#
# app = Flask(__name__)
#
# @app.route("/calc")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
#
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        foods = request.form.getlist('food[]')
        quantities = request.form.getlist('quantity[]')

        # You can now process the foods and quantities as needed
        for food, quantity in zip(foods, quantities):
            print(f"Food: {food}, Quantity: {quantity}")

        return "Form submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)

