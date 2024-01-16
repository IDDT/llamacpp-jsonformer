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
N_PROCS = max(1, (os.cpu_count() or 2) // 2)
CONCURRENCY = max(1, int(os.getenv('CONCURRENCY', 1)))
logging.info(f'Concurrency is set to {CONCURRENCY}')


# Paths.
TEMP_DIR = 'temp'
BINARY_PATH = os.path.join(TEMP_DIR, 'main')
MODEL_PATH = os.path.join(TEMP_DIR, 'model.gguf')
