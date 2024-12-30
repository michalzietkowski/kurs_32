
import sys
from file_handler import TxtFileHandler

arguments = sys.argv
if arguments[1].endswith(".txt"):
    input_file_handler = TxtFileHandler(input_file=arguments[1], output_file=arguments[2], changes=arguments[3:])


input_file_handler.transform()
output_file_handler.matrix = input_file_handler.matrix
output_file_handler.save_data_to_output_file()

