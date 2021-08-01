"""Main CLI module"""

from dataclasses import dataclass
import click
from shared.conf import Config
from shared.log import Log


@dataclass
class SharedData:
    """Class to share data among the CLI instance"""

    conf: Config
    log: Log


@click.command()
@click.pass_obj
def configuration(shared: SharedData) -> None:
    """Shows the current configuration file being used."""
    click.echo(shared.conf)


@click.group(commands=[configuration])
@click.version_option(None, "--version", package_name="pyapi")
@click.pass_context
def main(context: click.Context) -> None:
    """Application CLI interface"""

    conf = Config()
    log = Log(conf.params["log"]["dir"], conf.params["log"]["cli_file"])
    context.obj = SharedData(conf, log)
