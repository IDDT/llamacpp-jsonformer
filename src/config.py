import os
import sys
import logging


# Logging.
logging.basicConfig(
    format='%(levelname)s:     %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
    level=logging.INFO,
    stream=sys.stdout,
    force=True
)


# Configs.
CONCURRENCY = max(1, int(os.getenv('CONCURRENCY', 1)))
logging.info(f'Concurrency is set to {CONCURRENCY}')


# Paths.
TEMP_DIR = 'temp'
BINARY_PATH = os.path.join(TEMP_DIR, 'binary')
MODEL_PATH = os.path.join(TEMP_DIR, 'model.bin')
