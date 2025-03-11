import pandas as pd
import json
import math


def read_csv(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df

def read_json(file_path):
    df = pd.read_json(file_path)
    print(df.head())
    return df

# Formula to calculate the distance between two points on the earth's surface
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371   # Radius of the earth in kilometers

    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences between the latitudes and longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula

    # Helper variable that combines the latitude and longitude differences, makes calculations easier
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2

    # Allows us to convert a into an actual angular distance
    c = 2 * math.asin(math.sqrt(a))

    # Multiply the angular distance by the radius of the earth to get the distance in kilometers
    distance = c * R

    return distance

def find_pair(dataset1, dataset2):
    # Intialize a dictionary for closest pairs
    closest_pairs = {}

    # Compare each point in dataset1 with each point in datset2
    for index1, row1, in dataset1.iterrows():
        for index2, row2 in dataset2. iterrows():
            distance = haversine_distance(row1['latitude'], row1['longitude'], row2['latitude'], row2['longitude'])
            
            # If the distance is less than 0.1km (100m), add the pair to the closest pairs dictionary
            if distance < 0.1:
                closest_pairs[str(int(row1['id']))] = int(row2['id'])
    
    # Print the closest pairs, debugging purposes
    print(closest_pairs)

    # Convert the closest pairs dictionary to a json object
    json_output = json.dumps(closest_pairs)

    # Write the output to a file
    with open('closest_pairs.json', 'w') as file:
        file.write(json_output)
        
    return closest_pairs
                




if __name__ == "__main__":
    # Read the data from the csv and json files, and convert them to pandas dataframes
    csv_data = read_csv("SensorData1.csv")
    json_data = read_json("SensorData2.json")

    # Find the closest pairs between the two datasets
    find_pair(csv_data, json_data)






