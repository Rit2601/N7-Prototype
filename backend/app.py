from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"

    from routes import bp
    app.register_blueprint(bp)

    return app

# ✅ IMPORTANT: Gunicorn needs a WSGI callable named `app`
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
