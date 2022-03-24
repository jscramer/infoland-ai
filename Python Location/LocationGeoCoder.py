import geocoder as geo
g = geo.ip('me')
print(g.latlng)
print(g)
