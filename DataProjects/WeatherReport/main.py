import csv

def get_data():
    with open('PythonProjects/SimpleProjects/DataProjects/WeatherReport/weather_data.csv') as data_file:
        print("Reading data from file with csv module")
        data = csv.reader(data_file)
        temperatures = []
        for row in data:
            if row[1] != 'temp':
                temperatures.append(int(row[1]))
        print(temperatures)

import pandas

def get_data_pandas(is_print=False):
    print("Reading data from file with pandas module")
    data = pandas.read_csv('PythonProjects/SimpleProjects/DataProjects/WeatherReport/weather_data.csv')
    if is_print:
        print(data['temp'])
    return data
    
if __name__ == '__main__':
    data = get_data_pandas()
    print(f"Avg Temp: {data['temp'].mean()}") # Average temperature
    print(f"Sum Temp: {data['temp'].sum()}") # Sum of temperature
    print(f"Max Temp: {data['temp'].max()}") # Maximum temperature
    
    print(data.columns) # Columns in the data
    
    print(f"{data['condition'][0]} is same with {data.condition[0]}") # Accessing columns in different ways
    
    print(f"Reaching data with condition: \n{data[data.day == 'Monday']}") # Accessing data with condition
    
    data_dict = {
        'students': ['Ali', 'Veli', 'Deli'],
        'scores': [76, 89, 98],
        'grades': ['A', 'B', 'A']
    }
    
    data_frame = pandas.DataFrame(data_dict)
    
    print(f"Data Frame: \n{data_frame}")
    
    print(f"Grade of Ali: {data_frame[data_frame.students == 'Ali'].grades.values[0]}")
    
    data_frame.to_csv('PythonProjects/SimpleProjects/DataProjects/WeatherReport/new_data.csv') # Writing data to a new file