import fiona
import os

os.makedirs("data/countries", exist_ok=True)

with fiona.open("data/world_countries.geojson") as src:
    for country in src:
        name = country["properties"]["NAME_ENGL"]
        print(f"Criando: {name}")

        with fiona.open(f"data/countries/{name}.geojson", "w", driver="GeoJSON", crs=src.crs, schema=src.schema) as dst:
            dst.write(country)
