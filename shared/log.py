import click
import os
import io
import logging


class LogException(Exception):
    """Log Exception"""

    def __init__(self, message):
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
                raise LogException(
                    f"Can't create {logdir} directories. Check permissions"
                )

        self.logfile = os.path.join(logdir, logfile)

        logging.basicConfig(
            format="%(asctime)s[%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename=self.logfile,
            level=level,
        )

        self.logger = logging.getLogger("")

    def __str__(self) -> str:
        return self.logfile

    def debug(self, msg, fg="blue") -> None:
        """Log message on Debug level log"""
        smsg = click.style(msg, fg=fg)
        self.logger.debug(smsg)

    def info(self, msg, fg="white") -> None:
        """Log message on Info level log"""
        smsg = click.style(msg, fg=fg)
        self.logger.info(smsg)

    def warning(self, msg, fg="yellow") -> None:
        """Log message on Warning level log"""
        smsg = click.style(msg, fg=fg)
        self.logger.warning(smsg)

    def error(self, msg, fg="red") -> None:
        """Log message on Error level log"""
        smsg = click.style(msg, fg=fg)
        self.logger.error(smsg)
