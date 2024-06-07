# Capstone_Tax_Geo_Location

## Technical Documentation for Taxi Geolocation Simulator

**1. Introduction**

This document describes a Python script that simulates the generation and periodic retrieval of taxi geolocations. The script can be used for testing or demonstration purposes where taxi locations are needed.

**2. Dependencies**

The script relies on the following Python libraries:

* `random`: Used for generating random numbers.
* `time`: Used for getting the current time and sleep functionality.

**3. Functionality**

The script provides two main functions:

* **generate_random_geolocation()**: This function generates a random latitude and longitude within a plausible range (-90 to 90 for latitude and -180 to 180 for longitude).
* **get_taxi_geolocations(num_taxis=5)**: This function creates a list of dictionaries containing the geolocations for a specified number of taxis (default is 5). Each dictionary has the following keys:
    * `latitude`: The randomly generated latitude value.
    * `longitude`: The randomly generated longitude value.

The script also includes a `main` function that continuously retrieves and prints the taxi geolocations. Here's a breakdown of the main function:

* **Infinite Loop**: The `main` function utilizes a `while True` loop to continuously perform the following actions:
    * **Generate Taxi Geolocations**: It calls the `get_taxi_geolocations` function to generate a fresh list of taxi locations.
    * **Print Geolocations**: It iterates through the list of taxi locations and prints the taxi number, latitude, and longitude for each taxi. It uses `time.strftime` to format the current timestamp for the printout.
    * **Wait for Next Update**: It calls `time.sleep(90)` to pause the script for 90 seconds before retrieving taxi locations again.

**4. Usage**

1. Save the script as a Python file (e.g., `taxi_geolocation_simulator.py`).
2. Run the script from the command line using `python taxi_geolocation_simulator.py`.

This will start the simulation, and the script will continuously print taxi geolocations every 90 seconds.

**5. Explanation of Key Parts**

* **`random.uniform(a, b)`**: This function from the `random` library generates a random floating-point number between the values `a` (inclusive) and `b` (exclusive). It's used to create realistic latitude and longitude values within a specific range.
* **`time.strftime('%Y-%m-%d %H:%M:%S')`**: This function from the `time` library formats the current date and time according to the specified format string. The provided format string represents year-month-day, hours-minutes-seconds.

**6. Conclusion**

This Python script provides a basic simulation for generating and retrieving taxi geolocations. It can be a helpful tool for testing or demonstration purposes where taxi location data is required. The script can be further extended to incorporate additional features, such as storing the generated locations in a file or database.