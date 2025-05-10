import os, sys

class CustomException(Exception):
    def __inii__(self, error_message: Exception, error_details: sys):
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,error_details=error_details)
    
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys)->str:
        _,_, exec_tb = error_details.exc_info()
        
        try_block_line_number = exec_tb.tb_lineno
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        
        error_message = f"Error occured: {file_name} try block no: {try_block_line_number} exception block no: {exception_block_line_number} error message: {error_message}"
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
    
    