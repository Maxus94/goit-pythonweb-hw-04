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


async def read_folder(path: AsyncPath):
    if await path.is_dir():
        async for child in path.iterdir():
            await read_folder(child)
    else:
        await copy_file(outdir_path, path)


async def copy_file(path: AsyncPath, file_name: AsyncPath):
    if not await path.exists():
        try:
            await path.mkdir(parents=False, exist_ok=True)
        except:
            return "It is impossible to create this directory"

    try:
        [_, ext] = str(file_name.name).split(".")
    except:
        return f"Wrong file name {file_name.name}, without extension"
    dir_to_copy = AsyncPath(ext)
    directory = AsyncPath(str(path.name) + "/" + ext)

    # for p in path.iterdir:
    # print(path.iterdir())
    # yield (path.iterdir())

    # if dir_to_copy not in path.iterdir():
    #     try:
    #         await directory.mkdir(parents=False, exist_ok=True)
    #     except:
    #         return "It is impossible to create this directory"

    # try:
    #     copyfile(file_name, directory)
    # except:
    #     return f"It is not possible to copy {file_name} to {directory}"


async def main():
    await read_folder(indir_path)


if __name__ == "__main__":
    asyncio.run(main())
