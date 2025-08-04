from logger import get_logger
import sys

class CustomException(Exception):
    def __init__(self,error_message:str,error_detail:sys):
        super().__init__(error_message)
        self.error_message=CustomException.get_detailed_error_message(error_message,error_detail)

    @staticmethod
    def get_detailed_error_message(error_message,error_detail:sys)->str:
        _,_,exc_tb=error_detail.exc.info()
        line_number=exc_tb.tb_lineno
        file_name=exc_tb.tb_frame.f_code.co_filename
        error_message=f"Error occurred in script:{file_name}at line number:{line_number} with message:{error_detail}"

        return error_message
                 