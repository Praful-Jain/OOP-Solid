from calculator import Calculator  # Import the Calculator class from the calculator file
from data_extractor import DataExtractor  # Import the DataExtractor class from the data_extractor file

"""Procedure - 
1) Extract data using data_extractor program
2) Compute required result using the calculator program """

obj1 = DataExtractor('SOLID/weather.dat')  # Create a DataExtractor class object and pass the file location
weather_data = obj1.reader_function(['Dy', 'MxT', 'MnT'])  # Call the reader_function() of the DataExtractor class to get data of the required columns

obj2 = Calculator(weather_data)  # Create a Calculator class object and provide it with the weather_data
result = obj2.calculate('MxT', 'MnT', 'Dy')  # Call the calculate() function of the Calculator class to compute the result

print(result)
