from views import app
from models.database import db


# condition that handles the running of the flask application
if __name__ == '__main__':
    db.create_all()
    app.run()