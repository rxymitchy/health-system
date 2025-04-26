from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config 

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Bootstrap
    Bootstrap(app)

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app