import csv


class FileHandler:
    def __init__(self, input_file, output_file, transformations):
        self.input_file = input_file
        self.output_file = output_file
        self.transformations = transformations
        self.matrix = self.load_data_from_input_file()

    def load_data_from_input_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for row in reader:
                temp_row = []
                for number in row:
                    temp_row.append(int(number))
                temp_matrix.append(temp_row)
        return temp_matrix

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

    def transform(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            print(transformation_list)
            operation_type = transformation_list[0]
            vector = transformation_list[1]
            index = int(transformation_list[2])
            number = int(transformation_list[3])
            # self.matrix[transformation_list[0]][transformation_list[1]] = transformation_list[2]
            if operation_type == "add":
                if vector == "row":
                    self.add_row(index, number)
                elif vector == "col":
                    self.add_col(index, number)
            elif operation_type == "mult":
                if vector == "row":
                    self.mult_row(index, number)
                elif vector == "col":
                    self.mult_col(index, number)


    def add_row(self, index, value):
        for position, item in enumerate(self.matrix[index]):
            self.matrix[index][position] += value

    def add_col(self, index, value):
        for row in self.matrix:
            row[index] += value

    def mult_row(self, index, value):
        for position, item in enumerate(self.matrix[index]):
            self.matrix[index][position] *= value

    def mult_col(self, index, value):
        for row in self.matrix:
            row[index] *= value


