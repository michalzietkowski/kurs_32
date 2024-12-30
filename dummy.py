from itertools import islice

def read_large_log(file_path, start_line, end_line):
    with open(file_path, 'r') as log_file:
        # Pobierz tylko wybrane linie z dużego pliku logów
        for line in islice(log_file, start_line, end_line):
            print(line.strip())

# Przykład: czytanie linii 10-20 z ogromnego pliku logów
read_large_log("large_log_file.txt", 10, 20)
