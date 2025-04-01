import asyncio, argparse

from aiopath import AsyncPath
from aioshutil import copyfile

parser = argparse.ArgumentParser(description="Sort files in folders")
parser.add_argument("indir", type=str, help="Initial directory with files")
parser.add_argument("outdir", type=str, help="Target directory")
args = parser.parse_args()
print(args)

indir_path = AsyncPath(args.indir)
outdir_path = AsyncPath(args.outdir)


async def read_folder(folder):
    pass


async def copy_file(file, folder):
    pass


async def main():
    await read_folder(indir_path)


if __name__ == "__main__":
    asyncio.run(main())
