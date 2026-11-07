"""Send emails without blocking the request: a slow or blocked mail server must never break a form."""
import logging
import threading

logger = logging.getLogger(__name__)


def send_in_background(message):
    def run():
        try:
            message.send(fail_silently=False)
        except Exception:
            logger.exception("Email %r to %s failed", message.subject, message.to)

    threading.Thread(target=run, daemon=True).start()
