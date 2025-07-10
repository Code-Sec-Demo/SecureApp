from flask import request
import base64
import json

# Simulates a cache/session store of active users
USER_SESSIONS = {
    "abc123": {"id": 1, "username": "alice", "role": "user", "is_superuser": False},
    "admin42": {"id": 0, "username": "admin", "role": "admin", "is_superuser": True}
}

def is_authenticated(req):
    token = req.headers.get("X-Session-Token")
    if not token:
        return False
    return token in USER_SESSIONS

def current_user(req):
    token = req.headers.get("X-Session-Token")
    if not token:
        return {}
    return USER_SESSIONS.get(token, {})

def extract_user_from_cookie():
    try:
        cookie = request.cookies.get("user_info")
        if not cookie:
            return None
        decoded = base64.b64decode(cookie).decode()
        return json.loads(decoded)
    except Exception:
        return None
