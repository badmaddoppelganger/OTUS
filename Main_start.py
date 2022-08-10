from pathlib import Path

cwd = Path.cwd()
my_path = Path(cwd)
print(my_path.exists())
print(my_path)
print(my_path.joinpath('raw'))
