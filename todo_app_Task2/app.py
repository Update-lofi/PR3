from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Мой список дел</h1><p>Скоро здесь будут задачи</p>'

if __name__ == '__main__':
    app.run(debug=True)