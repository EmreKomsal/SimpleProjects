import pandas as pd

# Constants
DATA_PATH = "PythonProjects/SimpleProjects/DataProjects/Squirrel_Data/data.csv" # Path to the data file

def get_data(data_path):
    data = pd.read_csv(data_path)
    return data

def save_data(data, data_path):
    data.to_csv(data_path, index=False)
    
def get_fur_color(data):
    fur_color = data["Primary Fur Color"].unique()
    return fur_color

def get_fur_count(data):
    fur_count = data["Primary Fur Color"].value_counts()
    return fur_count

def main():
    data = get_data(DATA_PATH)
    print(data.head())
    print(data.columns)
    print(get_fur_color(data))
    print(get_fur_count(data))
    data_fur = get_fur_count(data)
    save_data(data_fur, "PythonProjects/SimpleProjects/DataProjects/Squirrel_Data/fur_count.csv")
    
if __name__ == "__main__":
    main()