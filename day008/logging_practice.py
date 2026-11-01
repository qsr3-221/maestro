# import logging 
# logger=logging.getLogger(__name__)
# logger.info("Start")
# logger.error("Crash")
import logging 
logging.basicConfig(level=logging.INFO,filename="app.log")
logger=logging.getLogger(__name__)
logger.info("Start")
logger.warning("Warn")
logger.error("Crash")