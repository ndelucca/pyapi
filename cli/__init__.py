import click
from shared.conf import Config
from shared.log import Log


class SharedData:
    """Class to share data among the CLI instance"""

    conf: Config
    log: Log

    def __init__(self):
        self.conf = Config()
        self.log = Log(
            self.conf.params["log"]["dir"], self.conf.params["log"]["cli_file"]
        )


@click.group()
@click.version_option(None, "--version")
@click.pass_context
def main(context: click.Context) -> None:
    """Application CLI interface"""

    context.obj = SharedData()


@click.command()
@click.pass_obj
def configuration(shared: SharedData) -> None:
    """Shows the current configuration file being used."""
    click.echo(shared.conf)


main.add_command(configuration)
