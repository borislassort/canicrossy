from flaskwebgui import FlaskUI
from canicrossy.wsgi import application as app

if __name__ == "__main__":
    FlaskUI(app=app, server="django", fullscreen=False).run()