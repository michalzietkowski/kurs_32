from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="michal_zietkowski_mz")
city = input("Podaj swoje miasto")
location = geolocator.geocode(city)
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)