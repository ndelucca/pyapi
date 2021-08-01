"""Configuration file handling module"""

import os
from configparser import ConfigParser
from typing import List


class ConfigException(Exception):
    """Configuration Exception"""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class Config:
    """Configuration file parser class"""

    filepath: str
    params: ConfigParser

    def __init__(
        self,
        filename: str = "app.cfg",
        filepaths: List[str] = [os.path.expanduser("~"), "./", "/var/www/"],
    ):
        self.filepath = self.__getfile(filename, filepaths)
        self.params = self.__parsefile(self.filepath)

    def __str__(self) -> str:
        out = f"File path: {self.filepath}\n"
        with open(self.filepath, "r") as content:
            out += content.read()
        return out

    @staticmethod
    def __getfile(filename: str, paths: List[str]) -> str:
        """Returns the first configuration file found"""
        for path in paths:
            filepath = os.path.join(path, filename)
            if os.path.exists(filepath):
                return filepath

        raise ConfigException("Could not find the configuration file.")

    @staticmethod
    def __parsefile(filepath: str) -> ConfigParser:
        """Returns a configured ConfigParser"""
        cfg = ConfigParser(strict=True)

        cfg.read(filepath)

        if cfg.has_section("log"):
            return cfg

        raise ConfigException("Invalid configuration file.")
