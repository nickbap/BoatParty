from boatparty import create_app, db
from boatparty.models import GuestBookPost

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'GuestBookPost': GuestBookPost}


if __name__ == "__main__":
    app.run(debug=True)
