from os.path import realpath, dirname
from pathlib import Path
from dataclasses import dataclass

PROJECT_ROOT = Path(realpath(dirname(__file__))).joinpath('..', '..')


@dataclass
class DirectoryPath:
    CSV_DATA: Path = PROJECT_ROOT.joinpath('data')
    MODELS: Path = PROJECT_ROOT.joinpath('models')

    def __post_init__(self):
        for _, v in self.__dict__.items():
            if not v.exists():
                v.mkdir()


DIRECTORY: DirectoryPath = DirectoryPath()
