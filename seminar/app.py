from flask import Flask, render_template, request, session, make_response, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from seminar.models import db, User
from seminar.forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = b'49d45b3a56115f41aadaca10825fd35ab95d1b95ddad1293b4806b51e53dc755'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


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
#     if request.method == 'POST':
#         username = request.form.get('username')
#         context = {'username': username}
#         response = redirect(url_for('hello', **context))
#         response.set_cookie('username', username)
#         return response
#     return render_template('register.html')


@app.route('/hello/<username>')
def hello(username):
    context = {'username': username}
    return render_template('hello.html', **context)


@app.route("/logout")
def logout():
    response = make_response(redirect("/register"))
    response.delete_cookie('username')
    return response


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("add-user")
def add_user():
    username = User(name='john', surname='ford', email="john@mail.ru")
    db.session.add(username)
    db.session.commit()
    print('user add in DB')


@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('register'))
    else:
        return render_template('register2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
