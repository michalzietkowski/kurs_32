import csv

def load_csv_file(file):
    with open(file) as file:
        reader = csv.reader(file)
        data = []
        for line in reader:
            data.append(line)
        return data

def save_data_to_csv_file(file, data):
    with open(file, mode="w+") as file:
        writer = csv.writer(file)
        writer.writerows(data)

old_data = load_csv_file("test_data.csv")

save_data_to_csv_file("nowy_csv_plik.csv", old_data)