import logging

"""Configuration"""
logging.basicConfig(filename="log_scope.txt.",level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(level=logging.INFO)

"""
Logging levels DESC
-------------------------
Level   :   numeric value

CRITICAL:   50
ERROR   :   40
WARNING :   30
INFO:   :   20
DABUG   :   10
NOTSET  :   0
-------------------------
"""

"""Logging examples"""
logging.info("This is info")

logging.warning("This is warning")

logging.debug("This is debug")
