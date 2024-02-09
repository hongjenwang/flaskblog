#export FLASK_APP=flaskblog
#python3 -m flask run
#from project import app, db
#app.app_context().push()
#db.create_all()
from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
