from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)


@app.route('/')
@app.route('/home')
def index():
    title = 'Home'
    return render_template('home.html', title=title)


@app.route('/about')
def about():
    title = 'About Us'
    return render_template('about.html', title=title)


@app.route('/details')
def details():
    title = 'Details'
    return render_template('details.html', title=title)


@app.route('/registry')
def registry():
    title = 'registry'
    return render_template('registry.html', title=title)


@app.route('/guest-book')
def guest_book():
    title = 'Guest Book'
    return render_template('guest_book.html', title=title)


@app.route('/rsvp')
def rsvp():
    title = 'RSVP'
    return render_template('rsvp.html', title=title)


@app.route('/base')
def base_test():
    """Temporary route for checking the base template."""
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
