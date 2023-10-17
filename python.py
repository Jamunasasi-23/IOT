import random
import time
import datetime
import csv

class WaterConsumptionMeter:
    def _init_(self, location):
        self.location = location
        self.data = []

    def measure_water_usage(self):
        current_time = datetime.datetime.now()
        consumption = random.uniform(1.0, 10.0)  # Simulate consumption as a float value
        data_point = (current_time, consumption)
        self.data.append(data_point)
        return data_point

def save_data_to_csv(data, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow(item)

if _name_ == "_main_":
    location = "Your Location"
    meter = WaterConsumptionMeter(location)
    data_filename = "water_consumption_data.csv"

    while True:
        data_point = meter.measure_water_usage()
        save_data_to_csv([data_point], data_filename)
        print(f"Measured water consumption at {data_point[0]}: {data_point[1]:.2f} units")
        time.sleep(3600)  # Simulating hourly data collection

    # You can add data analysis and reporting code here.
