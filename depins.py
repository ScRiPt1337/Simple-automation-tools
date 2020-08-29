import aiofiles
import asyncio
import argparse
from cprint import *
import subprocess as procx
import sys


parser = argparse.ArgumentParser(description='This script will find all requerment modules and install them')
parser.add_argument('Filepath', metavar='File path', type=str, nargs='+',
                    help='Filepath to detect requerment')

args = parser.parse_args()
async def main(filename):
    packages = []
    command = []
    async with aiofiles.open(filename, mode='r') as f:
        async for linex in f:
            line = linex.strip()
            if line.startswith("from") or line.startswith("import"):
                nx = line.split(" ")[1]
                if "," in nx:
                    data = nx.split(",")
                    for xz in data:
                        packages.append(xz)
                else:
                    packages.append(nx)
        cprint.warn("Dependensis Found =>")
        execx = sys.executable
        for i in packages:
            command.append(f"{execx} -m  pip install {i}")
            cprint.ok(i)
        for i in command:
            cprint.ok(i)
            result = procx.run(i, shell=True, capture_output=True
                    )
            rex = result.stdout.decode()
            if rex == "":
                rex = result.stderr.decode()
                cprint.err(rex)
            else:
                cprint.info(rex)

file = args.Filepath[0]
cprint.info(file)    
asyncio.run(main(file))