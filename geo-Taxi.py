import time
import random

def generate_random_geolocation():
    """Generate a random geolocation within a plausible range."""
    lat = random.uniform(-90.0, 90.0)
    lon = random.uniform(-180.0, 180.0)
    return lat, lon

def get_taxi_geolocations(num_taxis=5):
    """Get geolocations for a number of taxis."""
    taxis = []
    for _ in range(num_taxis):
        lat, lon = generate_random_geolocation()
        taxis.append({'latitude': lat, 'longitude': lon})
    return taxis

def main():
    """Main function to get geolocations every 90 seconds."""
    while True:
        taxi_geolocations = get_taxi_geolocations()
        print(f"Taxi geolocations at {time.strftime('%Y-%m-%d %H:%M:%S')}:")
        for idx, geo in enumerate(taxi_geolocations, start=1):
            print(f"  Taxi {idx}: Latitude {geo['latitude']}, Longitude {geo['longitude']}")
        print("\nNext update in 90 seconds...\n")
        time.sleep(90)

if __name__ == "__main__":
    main()
