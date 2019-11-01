from os.path import realpath, dirname
from pathlib import Path
from dataclasses import dataclass

from loguru import logger

PROJECT_ROOT = Path(realpath(dirname(__file__))).joinpath('..', '..')


@dataclass
class DirectoryPath:
    CSV_DATA: Path = PROJECT_ROOT.joinpath('data')
    MODELS: Path = PROJECT_ROOT.joinpath('models')
    LOGS: Path = PROJECT_ROOT.joinpath('logs')

    def __post_init__(self):
        for _, v in self.__dict__.items():
            if not v.exists():
                v.mkdir()


DIRECTORY: DirectoryPath = DirectoryPath()
logger.add(DIRECTORY.LOGS.joinpath('{time}.log'))
