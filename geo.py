from geolocation.main import GoogleMaps

address = "Engvej 1"

google_maps = GoogleMaps(api_key='your_google_maps_key')

# Sender søgning til Google Maps
location = google_maps.search(location_address)

# Returnerer alle steder
print(location.all())


#Returnerer kun første lokation
my_location = location.first()

print(my_location.city)
print(my_location.route)
print(my_location.street_number)
print(my_location.postal_code)

for adminstrative_area in my_location.adminstrative_area:
    print("{}: {} ({})".format(adminstrative_area.area_type,
    adminstrative_area.name,
    adminstrative_area.short_name))

print(my_location.country)
print(my_location.country_shortcut)

print(my_location.formatted_address)

print(my_location.lat)
print(my_location.lng)

#Reverse geocode
lat = 40.70600088
lng = -74.0088189

my_location = google_maps.search(lat=lat, lng=lng).first()
