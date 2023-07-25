import subprocess
import asyncio
import logging
import time
from .config import BINARY_PATH, MODEL_PATH, CONCURRENCY


semaphore = asyncio.Semaphore(CONCURRENCY)


def infer(grammar:str, prompt:str='') -> str:
    start_time = time.time()
    try:
        out = subprocess.run([
            BINARY_PATH,
            '--model', MODEL_PATH,
            '--grammar', grammar,
            '--prompt', prompt,
            '--threads', '4'
        ], capture_output=True, check=True, timeout=60)
    except subprocess.CalledProcessError as e:
        code, msg = e.returncode, e.stderr.decode('utf-8').replace('\n', ';')
        logging.error(f'llamacpp failed with code:{code} msg:{msg}')
    except Exception as e:
        logging.error(f'llamacpp failed with exc:{type(e)} msg:{str(e)}')
    else:
        logging.info(f'Inferred in {time.time() - start_time:.2f}s')
        return out.stdout.decode('utf-8')
    return ''


async def infer_async(*args, **kwargs):
    async with semaphore:
        return await asyncio.to_thread(infer, *args, **kwargs)
