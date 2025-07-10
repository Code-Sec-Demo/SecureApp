import os
import mimetypes

UPLOAD_DIR = "user_uploads"

ALLOWED_EXTENSIONS = {"jpg", "png", "pdf", "txt"}

def _get_extension(filename):
    if "." not in filename:
        return ""
    return filename.rsplit(".", 1)[-1].lower()

def _validate_file(file):
    ext = _get_extension(file.filename)
    if ext not in ALLOWED_EXTENSIONS:
        return False
    mime, _ = mimetypes.guess_type(file.filename)
    return mime is not None

def handle_upload(file):
    if not file or not hasattr(file, "filename"):
        return False
    if not _validate_file(file):
        return False
    filename = file.filename
    dest = os.path.join(UPLOAD_DIR, filename)
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file.save(dest)
    return True
