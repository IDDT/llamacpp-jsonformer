import os
import sys
import logging


# Logging.
logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
    level=logging.INFO,
    stream=sys.stdout,
    force=True
)


# Paths.
TEMP_DIR = 'temp'
BINARY_PATH = os.path.join(TEMP_DIR, 'binary')
MODEL_PATH = os.path.join(TEMP_DIR, 'model.bin')
