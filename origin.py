import os
from datetime import datetime

current_dir = os.getcwd()
timestamp_now = datetime.now().strftime('tmp_%Y%m%d%H%M%S')
filename = f'{current_dir}/{timestamp_now}.py'


def mkfile(filename: str):
    with open(filename, 'w') as f:
        f.write('print("Hello, world")\n')


if __name__ == '__main__':
    mkfile(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        pyscript = f.read()
        exec(pyscript)
