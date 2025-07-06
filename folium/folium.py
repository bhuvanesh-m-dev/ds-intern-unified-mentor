import folium
m = folium.Map(location=[13.0827, 80.2707], zoom_start=12)
folium.Marker(
    location=[13.0827, 80.2707],
    popup="Hello from Chennai!",
    tooltip="Click me"
).add_to(m)
m.save("mymap.html")
print("Map saved as mymap.html")
