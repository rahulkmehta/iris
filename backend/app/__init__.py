from flask import Flask, jsonify
from flask_cors import CORS
from app.routes import search_bp  # Import the Blueprint

def create_app():
    app = Flask(__name__)

    # Configure CORS to allow requests from your frontend
    CORS(
        app,
        origins=[
            "https://iris-sigma-ebon.vercel.app",  # Production frontend
            "http://localhost:8080",               # Vite dev server
            "http://localhost:4173",               # Vite preview server
            "*.vercel.app"                         # Vercel preview deployments
        ],
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization", "Accept"],
        methods=["GET", "POST", "OPTIONS"]
    )

    # Register the search Blueprint
    app.register_blueprint(search_bp)

    @app.route("/api/health", methods=["GET"])
    def health_check():
        """Health check endpoint to verify the API is running"""
        return jsonify({"status": "ok", "message": "API is running"})

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found", "message": "The requested resource does not exist"}), 404

    return app