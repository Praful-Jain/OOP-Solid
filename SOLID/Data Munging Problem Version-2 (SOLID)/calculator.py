from data_analyzer import DataAnalyzer  # Import the DataAnalyzer class from the data_analyzer file

class Calculator:
    def __init__(self, data):
        self.data = data

    def calculate(self, column1, column2, column3):
        obj = DataAnalyzer(self.data)  # Create a DataAnalyzer class object and provide it with the data
        result = obj.analyzer(column1, column2, column3)  # Call the analyzer() function of the DataAnalyzer class to compute the result
        return result
