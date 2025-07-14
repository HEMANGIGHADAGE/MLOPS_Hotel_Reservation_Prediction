from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def divide(a,b):
    try:
        result = a/b
        logger.info("dividing 2 numbers")
        return result
    except Exception as e:
        logger.error("Error occured")
        raise CustomException("Custom Error zero", sys)
    
if __name__ == "__main__":
    try:
        logger.info("execute")
        divide(5,10)
    except CustomException as e:
        logger.error(str(e))