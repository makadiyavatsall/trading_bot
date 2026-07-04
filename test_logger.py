from bot.logging_config import setup_logger

logger = setup_logger(__name__)

logger.debug("Debug message")

logger.info("Application Started")

logger.warning("Low balance")

logger.error("Order Failed")