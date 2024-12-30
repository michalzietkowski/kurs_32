import os

import psutil

def memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024*1024)

def read_file_to_list(file_path):
    with open(file_path) as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data

def read_file_generator(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()


print(f"Zużycie pamięci przed wczytaniem do listy: {memory_usage()} MB")
data_list = read_file_to_list("test.txt")
print(f"Zużycie pamięci po wczytaniu do listy: {memory_usage()} MB")

del data_list

print(f"Użycie pamięci przed generatorem: {memory_usage()} MB")
generator = read_file_generator("test.txt")
print(f"Użycie danych po stworzeniu generatora: {memory_usage()} MB")

for line in generator:
    pass

print(f"Użycie danych po wygenerowaniu przez generator: {memory_usage()} MB")