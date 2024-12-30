import json


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file_path) as file:
            return json.loads(file.read())

    def save_data_to_file(self):
        with open(self.file_path) as file:
            file.write(json.dumps(self.data))

    def __setitem__(self, key, value):
        city = key[0]
        date = key[1]
        if not self.data.get(city):
            self.data[city] = {}
        self.data[city][date] = value

    def __getitem__(self, item):
        city = item[0]
        key = item[1]
        return self.data.get(city, {}).get(key)

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for city, info in self.data.items():
            for date, info_date in info.items():
                yield f"{city}: {date} - {info_date}"

