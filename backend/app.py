from flask import Flask, request, jsonify, send_file
import requests
import os
from auth import is_authenticated, current_user
from database import get_user_data, search_logs
from file_upload import handle_upload
from utils import get_logger

app = Flask(__name__)
logger = get_logger()

@app.route("/")
def home():
    return "Welcome to SecureApp!"

@app.route("/profile", methods=["GET"])
def profile():
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401
    user = current_user(request)
    data = get_user_data(user["id"])
    return jsonify(data)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Missing query"}), 400
    logs = search_logs("SELECT * FROM logs WHERE message LIKE '%%%s%%'" % query)
    return jsonify({"results": logs})

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing URL"}), 400
    try:
        resp = requests.get(url, timeout=2)
        return (resp.content, resp.status_code, resp.headers.items())
    except Exception as e:
        logger.warning(f"Proxy error: {str(e)}")
        return jsonify({"error": "Proxy failed"}), 500

@app.route("/upload", methods=["POST"])
def upload():
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    save_path = os.path.join("user_uploads", file.filename)
    handle_upload(file)
    return jsonify({"message": "File uploaded", "path": save_path})

@app.route("/download/<path:filename>")
def download(filename):
    full_path = os.path.join("user_uploads", filename)
    return send_file(full_path, as_attachment=True)

@app.route("/admin/stats")
def admin_stats():
    user = current_user(request)
    if user and user.get("role") == "admin" or user.get("is_superuser"):
        stats = {
            "uptime": "102h",
            "active_users": 17,
            "db_size": "14GB"
        }
        return jsonify(stats)
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    app.run(debug=True)
