from flask import Flask, render_template
from config import Config
from models import db, login_manager
from models.user import User
from models.resume import Resume
from models.audit import AuditLog
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.resume import resume_bp
from routes.admin import admin_bp
from routes.main import main_bp
import os
import logging
from logging.handlers import RotatingFileHandler

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Configure logs
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/resume_generator.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime) +s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('AI Resume Generator Startup')
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(resume_bp, url_prefix='/resume')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Custom error handlers
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500
        
    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    # Auto-create tables on startup
    with app.app_context():
        db.create_all()
        # Seed default admin user if not exists
        admin_email = app.config.get('ADMIN_EMAIL')
        if admin_email:
            admin = User.query.filter_by(email=admin_email).first()
            if not admin:
                admin_user = User(
                    name="System Admin",
                    email=admin_email,
                    role="admin"
                )
                admin_user.set_password(app.config.get('ADMIN_PASSWORD', 'admin123'))
                db.session.add(admin_user)
                db.session.commit()
                app.logger.info(f"Seeded default admin user: {admin_email}")
                
    return app

app = create_app()

if __name__ == '__main__':
    # Run the server locally
    app.run(host='0.0.0.0', port=5000, debug=True)
