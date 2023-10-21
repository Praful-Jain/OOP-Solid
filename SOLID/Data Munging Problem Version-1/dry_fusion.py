
file1 = 'SOLID/weather.dat'
file2 = 'SOLID/soccer.dat'

def reader_function(file):
    with open(file) as f:
        lines = f.readlines()
        data = [line.strip().split() for line in lines]
        return data
    
data_weather = reader_function(file1)
data_match = reader_function(file2)