import requests
import folium

def get_geolocation(ip_address):
    # Fetch geolocation data using the IP address
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    return response.json()

def create_map(lat, lon):
    # Create a map centered at the given latitude and longitude
    geo_map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup='Your Location').add_to(geo_map)
    return geo_map

def main():
    # Get the user's IP address
    ip_address = requests.get('https://api64.ipify.org?format=json').json()['ip']
    
    # Fetch geolocation data
    location_data = get_geolocation(ip_address)

    if 'latitude' in location_data and 'longitude' in location_data:
        lat = location_data['latitude']
        lon = location_data['longitude']
        
        # Create and save the map
        geo_map = create_map(lat, lon)
        geo_map.save("geolocation_map.html")
        print(f"Map has been created and saved as 'geolocation_map.html'")
    else:
        print("Could not retrieve geolocation data.")

if __name__ == "__main__":
    main()