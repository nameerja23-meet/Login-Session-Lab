from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			login_session['name'] = request.form['name']
			login_session['age'] = request.form['age']
			login_session['quote'] = request.form['quote']
			return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', name=login_session['name'], quote = login_session['quote'], age = login_session['age'] ) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)