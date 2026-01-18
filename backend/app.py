from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"

    from backend.routes import bp   # ✅ fixed import
    app.register_blueprint(bp)

    return app

# ✅ for gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
