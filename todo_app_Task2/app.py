from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = ['Купить хлеб', 'Сделать уроки', 'Позвонить другу']

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form['task']
    if new_task:
        tasks.append(new_task)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
