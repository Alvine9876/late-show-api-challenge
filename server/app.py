from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config



from dotenv import load_dotenv

load_dotenv()


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    from .controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)


    from .controllers.appearance_controller import appearance_bp
    from .controllers.episode_controller import episode_bp

    app.register_blueprint(appearance_bp)
    app.register_blueprint(episode_bp)
    from .controllers.guest_controller import guest_bp
    app.register_blueprint(guest_bp)



 
    return app
