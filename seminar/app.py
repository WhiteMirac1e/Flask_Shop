from flask import Flask, render_template, request, session, make_response, redirect, url_for
from seminar.forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)


# app.config['SECRET_KEY'] = b'49d45b3a56115f41aadaca10825fd35ab95d1b95ddad1293b4806b51e53dc755'
# csrf = CSRFProtect(app)


@app.route('/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртка'}
    return render_template('jacket.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     response = make_response(render_template('hello.html'))
#     response.set_cookie('username', 'admin')
#     return response


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        context = {'username': username}
        response = redirect(url_for('hello', **context))
        response.set_cookie('username', username)
        return response
    return render_template('register.html')


@app.route('/hello/<username>')
def hello(username):
    context = {'username': username}
    return render_template('hello.html', **context)


@app.route("/logout")
def logout():
    response = make_response(redirect("/register"))
    response.delete_cookie('username')
    return response


if __name__ == '__main__':
    app.run(debug=True)
