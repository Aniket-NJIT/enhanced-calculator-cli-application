from app.logger import CustomLogger

def test_logger_singleton():
    logger1 = CustomLogger()
    logger2 = CustomLogger()
    assert logger1 is logger2  # Ensures only one instance is ever created

def test_logger_methods():
    logger = CustomLogger()
    # As long as these don't throw exceptions, the basic wrapper is working.
    logger.info("Test info")
    logger.error("Test error")
    logger.warning("Test warning")
    logger.critical("Test critical")