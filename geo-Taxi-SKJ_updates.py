import random
import time
from geopy.geocoders import Nominatim

def generate_random_geolocation(city_name="New York"):
  """Generate a random geolocation within a plausible range around a city."""
  geolocator = Nominatim(user_agent="taxi_simulator")
  location = geolocator.geocode(city_name)
  latitude_delta = random.uniform(-0.1, 0.1)
  longitude_delta = random.uniform(-0.1, 0.1)
  latitude = location.latitude + latitude_delta
  longitude = location.longitude + longitude_delta
  return latitude, longitude

def get_taxi_geolocations(num_taxis=5, city_name="New York"):
  """Get geolocations for a specified number of taxis in a city."""
  taxis = []
  for i in range(num_taxis):
    lat, lon = generate_random_geolocation(city_name)
    taxis.append({'taxi_id': i+1, 'latitude': lat, 'longitude': lon})
  return taxis

def main():
  """Main function to get geolocations every 90 seconds, with options."""
  city_name = input("Enter city name (default: New York): ") or "New York"
  num_taxis = int(input("Enter number of taxis (default: 5): ") or 5)
  
  # Open the log file in 'a' (append) mode outside the loop for efficiency
  with open("taxi_locations.log", "a") as log_file:
    while True:
      taxi_geolocations = get_taxi_geolocations(num_taxis, city_name)
      
      # Print to console
      print(f"Taxi geolocations at {time.strftime('%Y-%m-%d %H:%M:%S')}: (City: {city_name})")
      for geo in taxi_geolocations:
        print(f"  Taxi {geo['taxi_id']}: Latitude {geo['latitude']}, Longitude {geo['longitude']}")

      # Print to log file (already opened outside the loop)
      log_file.write(f"Taxi geolocations at {time.strftime('%Y-%m-%d %H:%M:%S')}: (City: {city_name})\n")
      for geo in taxi_geolocations:
        log_file.write(f"  Taxi {geo['taxi_id']}: Latitude {geo['latitude']}, Longitude {geo['longitude']}\n")
      log_file.write("\nNext update in 90 seconds...\n\n")
      
      time.sleep(90)

if __name__ == "__main__":
  main()
