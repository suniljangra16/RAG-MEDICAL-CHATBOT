from logger import get_logger
from custom_exception import CustomException
import sys

logging=get_logger(__name__)

def add(a:int,b:int)->int:
    try:
        logging.info(f"Adding {a} and {b}")
        return a + b
    except Exception as e:
        logging.error(f"Error occurred while adding: {e}")
        raise CustomException(e, sys) from e
    
if __name__=="__main__":
        try:
            logging.info(f"program started")
            result = add(5,10)
            logging.info(f"result of addition is {result}")
        except CustomException as ce:
             logging.error(str(ce))

        finally:
             logging.info(f"program ended")
            