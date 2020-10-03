import json
import requests

def getData(url):
    r = requests.get(url)
    return r.json()

def convertData(data, msymbol="camera", msize="medium"):
    data_dict = []
    for d in data:
        lon = float(d.get("LONGITUDE"))
        lat = float(d.get("LATITUDE"))
        if d.get('LONGITUDE') and d.get("LATITUDE"):
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
                    "marker-color": "#001FCC",
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
    data = getData("https://raw.githubusercontent.com/carmelosammarco/Palermo-SF/master/utils/Palermo_turismo.json")
    writeToFile(convertData(data[:126]), filename="Turismo.geojson")
