# Create logger.
from flask import session
def _get_session_id():
    session_key = "session_id"
    if not session.get(session_key):
        session[session_key] = secrets.token_urlsafe(16)
    return session.get(session_key)
def _record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    try:
        record.session_id = _get_session_id()
    except RuntimeError:
        record.session_id = "NO_ACTIVE_SESSION"
    return record
logging.basicConfig(format="%(session_id)s - %(message)s")
old_factory = logging.getLogRecordFactory()
logging.setLogRecordFactory(_record_factory)
