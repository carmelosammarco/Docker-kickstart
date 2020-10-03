import json
import requests

def getData(url):
    r = requests.get(url)
    return r.json()

def convertData(data, msymbol="restaurant", msize="medium"):
    data_dict = []
    for d in data:
        lon = float(d.get('longitude'))
        lat = float(d.get("latitude"))
        if d.get('longitude') and d.get("latitude"):
            data_dict.append({
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon,
                                    lat]
                },
                "type": "Feature",
                "properties": {
                    "name": d.get("name", ""),
                    "marker-symbol": msymbol,
                    "marker-size": msize,
                    "marker-color": "#CC0033",
                    "fooditems": d.get('fooditems', ""),
                    "address": d.get("address", "")
                }
            })
    return data_dict

def writeToFile(data, filename="data.geojson"):
    template = {
                "type": "FeatureCollection",
                "crs": {
                    "type": "name",
                    "properties": {
                      "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                    },
                },
                "features": data }
    with open(filename, "w") as f:
        json.dump(template, f, indent=2)
    print ("Geojson generated")

if __name__ == "__main__":
    data = getData("https://raw.githubusercontent.com/carmelosammarco/Palermo-SF/master/utils/Streetfood.json")
    writeToFile(convertData(data[:9]), filename="Streetfood.geojson")
