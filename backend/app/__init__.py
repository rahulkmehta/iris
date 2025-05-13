from flask import Flask, jsonify
from flask_cors import CORS
from app.routes import search_bp

def create_app():
    app = Flask(__name__)

    # Configure CORS
    CORS(
        app,
        origins=[
            "https://iris-1-jm40.onrender.com",
            "http://localhost:8080",
            "http://localhost:8081",
            "http://localhost:4173",
            "*.onrender.com"
        ],
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization", "Accept"],
        methods=["GET", "POST", "OPTIONS"]
    )

    # Register Blueprint
    app.register_blueprint(search_bp)

    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok", "message": "API is running"})

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found", "message": "The requested resource does not exist"}), 404

    @app.after_request
    def log_response(response):
        print(f"Response Status: {response.status}")
        print(f"Response Headers: {response.headers}")
        return response

    return app