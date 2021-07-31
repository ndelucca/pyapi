import click
from shared.conf import Config


@click.group()
@click.version_option(None, "--version")
@click.pass_context
def main(context):
    """Application CLI interface"""
    context.obj = Config()


@click.command()
@click.pass_obj
def configuration(conf):
    """Shows the current configuration file being used."""
    click.echo(conf)


main.add_command(configuration)
