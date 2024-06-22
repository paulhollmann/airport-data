import os

from utils.coordinate import parse_latitude, parse_longitude


def process_file(file):
    airport_map = {}

    for line in file:
        line = line.strip()
        if line.startswith("STAND:"):
            parts = line.split(":")
            if len(parts) == 6:
                _, airport_icao, stand, lat, lon, _ = parts
                if airport_icao not in airport_map:
                    airport_map[airport_icao] = []
                airport_map[airport_icao].append(
                    {
                        "stand": stand,
                        "lat": parse_latitude(lat),
                        "lon": parse_longitude(lon),
                    }
                )

    return airport_map


def open_txt_files(root_dir):
    airport_map_combined = {}
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    airport_map = process_file(f)
                    # Merge the current airport_map into airport_map_combined
                    for icao, stands_info in airport_map.items():
                        if icao not in airport_map_combined:
                            airport_map_combined[icao] = []
                        airport_map_combined[icao].extend(stands_info)

    return airport_map_combined


ROOT_DIRECTORY = "data/"

airport_map = open_txt_files(ROOT_DIRECTORY)

# Print the resulting airport_map for verification
for icao, stands_info in airport_map.items():
    print(f"Airport ICAO: {icao}")
    for stand_info in stands_info:
        print(
            f"  Stand: {stand_info['stand']}, Coordinates: {stand_info['lat']}, {stand_info['lon']}"
        )
    print("-----------------------------")
