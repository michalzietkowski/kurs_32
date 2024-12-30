from abc import abstractmethod

import ABC

class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.matrix = None

    @abstractmethod
    def load_data_from_file(self):
        pass

    @abstractmethod
    def save_data_to_file(self):
        pass

    def transform(self):
        #logika z poprzedniej metody trasform
        pass


class JsonFileHandler(FileHandler):
    def load_data_from_file(self):
        pass

    def save_data_to_file(self):
        pass


class TxtFileHandler(FileHandler):
    def load_data_from_file(self):
        pass

    def save_data_to_file(self):
        pass
