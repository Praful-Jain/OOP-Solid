# This program will extract the required data from given file

class DataExtractor:
    def __init__(self, file):
        self.file = file

    def reader_function(self, columns):
        final_data = []  # list of dictionaries

        with open(self.file) as f:
            lines = f.readlines()
            data = [line.strip().split() for line in lines]
            column = data[0]  # contains column names

            for line in data[1:]:
                record = {}  # e.g., {'Dy':___ , 'MxT':___ , 'MnT':___}
                for column_name in columns:
                    index = column.index(column_name)
                    record[column_name] = line[index]
                final_data.append(record)  # stores all records in final_data (list of dictionaries)

        return final_data
