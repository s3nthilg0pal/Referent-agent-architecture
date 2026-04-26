from agent_reference_arch.cli import main


def test_main_returns_zero(capsys):
    assert main() == 0
    captured = capsys.readouterr()
    assert "agent_reference_arch is ready" in captured.out
