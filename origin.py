import os
from datetime import datetime

cwd = os.getcwd()
filename = f"{cwd}/{datetime.now().strftime('tmp_%Y%m%d%H%M%S')}.py"


def mkfile(filename: str):
    with open(filename, 'w') as f:
        f.write("print('Hello, world')\n")


if __name__ == '__main__':
    mkfile(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        pyscript = f.read()
        exec(pyscript)
