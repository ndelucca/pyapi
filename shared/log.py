"""Log handling module"""

import os
import logging
import click


class LogException(Exception):
    """Log Exception"""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class Log:
    """Log files handler class"""

    logfile: str
    logger: logging.Logger

    def __init__(self, logdir: str, logfile: str, level=logging.DEBUG):

        if not logfile:
            raise LogException("Can't create Log without logfile.")

        if not os.path.exists(logdir):
            try:
                os.makedirs(logdir, mode=0o777)
            except PermissionError:
                msg: str = f"Can't create {logdir} directories. Check permissions"
                raise LogException(msg) from None

        self.logfile = os.path.join(logdir, logfile)

        settings: dict = {
            "format": "%(asctime)s[%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "filename": self.logfile,
            "level": level,
        }

        try:
            logging.basicConfig(**settings)
        except PermissionError:
            msg: str = f"Can't create {self.logfile} file. Check permissions"
            raise LogException(msg) from None

        self.logger = logging.getLogger("")

    def __str__(self) -> str:
        return self.logfile

    def debug(self, msg: str, color: str = "blue", **kwargs) -> None:
        """Log message on Debug level log"""
        smsg = click.style(msg, fg=color, **kwargs)
        self.logger.debug(smsg)

    def info(self, msg: str, color: str = "white", **kwargs) -> None:
        """Log message on Info level log"""
        smsg = click.style(msg, fg=color, **kwargs)
        self.logger.info(smsg)

    def warning(self, msg: str, color: str = "yellow", **kwargs) -> None:
        """Log message on Warning level log"""
        smsg = click.style(msg, fg=color, **kwargs)
        self.logger.warning(smsg)

    def error(self, msg: str, color: str = "red", **kwargs) -> None:
        """Log message on Error level log"""
        smsg = click.style(msg, fg=color, **kwargs)
        self.logger.error(smsg)
