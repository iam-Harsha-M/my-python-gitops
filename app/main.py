from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Hello from Kubeadm on AWS!",
        "environment": os.getenv("ENV", "development")
    })

@app.route('/health')
def health():
    # Kubernetes uses this to check if the pod is alive
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
