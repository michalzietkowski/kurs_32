# import json
#
#
# def load_data_from_json_file(file):
#     with open(file) as file:
#         json.loads(file.read())
#
#
#
# load_data_from_json_file("example.json")
import os

print(os.getcwd())
os.chdir("..")
print(os.getcwd())
print(os.listdir())
