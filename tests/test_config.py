from app.calculator_config import Config


def test_config_defaults():
    assert isinstance(Config.LOG_DIR, str)
    assert isinstance(Config.HISTORY_DIR, str)
    assert isinstance(Config.MAX_HISTORY_SIZE, int)
    assert isinstance(Config.AUTO_SAVE, bool)
    assert isinstance(Config.PRECISION, int)
    assert isinstance(Config.MAX_INPUT_VALUE, float)