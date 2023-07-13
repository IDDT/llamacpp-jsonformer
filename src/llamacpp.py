import subprocess
import logging
from .config import BINARY_PATH, MODEL_PATH


def infer(grammar:str, prompt:str='') -> str:
    try:
        out = subprocess.run([
            BINARY_PATH,
            '--model', MODEL_PATH,
            '--grammar', grammar,
            '--prompt', prompt
        ], capture_output=True, check=True, timeout=30)
    except subprocess.CalledProcessError as e:
        code, msg = e.returncode, e.stderr.decode('utf-8').replace('\n', ';')
        logging.error(f'llamacpp failed with code:{code} msg:{msg}')
    except Exception as e:
        logging.error(f'llamacpp failed with exc:{type(e)} msg:{str(e)}')
    else:
         return out.stdout.decode('utf-8')
    return ''
