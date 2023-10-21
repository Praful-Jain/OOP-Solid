# Will analyze the data and return the result

class DataAnalyzer:

    def __init__(self, data):
        self.data = data

    def analyzer(self, column1, column2, column3):
        min_difference = float('inf')
        result = None
        for record in self.data:
            diff = abs(float(record[column1]) - float(record[column2]))
            if diff < min_difference:
                min_difference = diff
                result = record[column3]
        return result
