import json


class FileHandler:
    def __init__(self, data_file, history_file):
        self.data_file = data_file
        self.history_file = history_file
        self.data = self.load_data_from_data_file()
        self.history = self.load_data_from_history_file()

    def load_data_from_data_file(self):
        with open(self.data_file) as file:
            return json.loads(file.read())

    def load_data_from_history_file(self):
        with open(self.history_file) as file:
            return json.loads(file.read())

    def save_data_to_data_file(self, balance, book_collection):
        with open(self.data_file, mode="w") as file:
            file.write(json.dumps({
                "saldo": balance,
                "ksiegozbior": book_collection
            }))

    def save_data_history_file(self, history):
        with open(self.history_file, mode="w") as file:
            file.write(json.dumps(history))

file_handler = FileHandler("dane_ksiegarni.json", "historia.json")