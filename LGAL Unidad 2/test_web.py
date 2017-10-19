from flask import Flask, render_template, request, redirect
from test_module import area, volumen

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Área de una esfera')


@app.route('/exec_are', methods=['GET', 'POST'])
def execute() -> 'html':
    y = float(request.form['y'])
    title = 'This is the equation\'s result'
    result = area(y)
    return render_template('result.html',
                           the_title=title,
                           the_y=y,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
