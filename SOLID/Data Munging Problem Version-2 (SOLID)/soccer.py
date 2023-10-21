from calculator import Calculator   # Importing the Calculator class from the calculator file
from data_extractor import DataExtractor  # Importing the DataExtractor class from the data_extractor file


obj1 = DataExtractor('SOLID/soccer.dat')    # Creating a DataExtractor class object and passing the file location
match_data = obj1.reader_function(['Team', 'F', 'A'])   # Calling the reader_function() of the DataExtractor class to get data of required columns

obj2 = Calculator(match_data)   # Creating a Calculator class object and giving it the match_data
result = obj2.calculate('F', 'A', 'Team')   # Calling the calculate() function of the Calculator class to compute the result

# Printing the result
print(result)
