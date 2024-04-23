from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('base.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept1'])
        print(request.form['accept2'])
        print(request.form['accept3'])
        print(request.form['accept4'])
        print(request.form['accept5'])
        print(request.form['accept6'])
        print(request.form['accept7'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')