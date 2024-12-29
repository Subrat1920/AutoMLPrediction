## The sys module in Python provides various function
## and variables that are used to manipulate different
## parts of the Python runtime environment.

import sys
import os
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    ## exc_tb will give all the details of the 
    ## error and exception occured in the program
    ## file, code line, and what is the error
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f'Error Occured in Python Script name [{file_name}] line number [{line_number}] and error message [{str(error)}]'

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


