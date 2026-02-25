from app.logger import CalculatorLogger


def test_logger_setup():
    logger = CalculatorLogger.setup_logger()
    assert logger is not None
    assert logger.name == "CalculatorLogger"