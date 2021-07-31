"""CLI interface test module"""

from cli import main, configuration
from click.testing import CliRunner

runner = CliRunner()


def test_main() -> None:
    execution = runner.invoke(main, ["--help"])
    assert execution.exit_code == 0


def test_configuration() -> None:
    execution = runner.invoke(configuration)
    assert execution.exit_code == 0
    assert type(execution.stdout) == str
