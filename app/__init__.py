from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index ():
        return render_template('index.html')

    from app.faculty import faculty_bp
    app.register_blueprint(faculty_bp)

    return app    
