"""Simple Flask application for testing DevSecOps Agent deployments"""

from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Get version from environment or use default
VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "test")

@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        "name": "test-devsecops-app",
        "version": VERSION,
        "environment": ENVIRONMENT,
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "version": VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/api/data')
def get_data():
    """Sample API endpoint"""
    return jsonify({
        "data": "test data",
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/api/version')
def get_version():
    """Version endpoint"""
    return jsonify({
        "version": VERSION,
        "environment": ENVIRONMENT,
        "build_time": os.getenv("BUILD_TIME", "unknown")
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
