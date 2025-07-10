import logging
import uuid
import time

audit_log = []

def get_logger():
    logger = logging.getLogger("secureapp")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def log_sensitive_operation(user, action, details):
    logger = get_logger()
    logger.info(f"{user['username']} performed {action}: {details}")
    audit_log.append((time.time(), user["id"], action, details))

def generate_request_id():
    return uuid.uuid4().hex

def has_recent_action(user_id, action, window_sec=5):
    now = time.time()
    recent = [entry for entry in audit_log if entry[1] == user_id and entry[2] == action and now - entry[0] < window_sec]
    return len(recent) > 0
