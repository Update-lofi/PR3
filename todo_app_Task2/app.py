from flask import Flask, render_template

app = Flask(__name__)

tasks = ['Купить хлеб', 'Сделать уроки', 'Позвонить другу']

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
