import os

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS", None)
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD", None)

try:
    from local_settings import *  # noqa
except ImportError:
    pass
