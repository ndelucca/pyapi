"""CLI interface test module"""

import pytest
from typing import List
from click.testing import CliRunner
from cli import main

runner = CliRunner()

test_commands_params = [
    (main, None),
    (main, ["--help"]),
    (main, ["--version"]),
    (main, ["configuration", "--help"]),
    (main, ["configuration"]),
]


@pytest.mark.parametrize("method, params", test_commands_params)
def test_commands(method, params: List[str]):
    """Test base de ejecucion de comandos"""
    execution = runner.invoke(method, params)
    assert execution.exit_code == 0
