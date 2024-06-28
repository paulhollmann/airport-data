import os
from views.stand import Stand

from utils.coordinate import parse_latitude, parse_longitude


class GrpDataReader:
    def __init__(self):
        self.airports = {}

    def process_stand_files(self, root_dir):
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    self.process_file(file_path)

        print("ICAO: Stand count")
        count = 0
        for airport, stands in self.airports.items():
            count += len(stands)
            print(f"{airport}: {len(stands)}")

        print("Total stand count: ", count)

        return self.airports

    def add_stand(self, stand: Stand):
        if stand.icao in self.airports:
            if not any(
                existing_stand.name == stand.name
                for existing_stand in self.airports[stand.icao]
            ):
                self.airports[stand.icao].append(stand)
        else:
            self.airports[stand.icao] = [stand]

    def process_file(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            lines = content.split("\n")

            for index, line in enumerate(lines):
                line = line.strip()

                # skip comments and empty lines
                if line.startswith("//") or line == "":
                    continue

                if line.startswith("STAND:"):
                    parts = line.split(":")

                    if len(parts) == 3:
                        _, icao, stand_name = parts
                        latitudes = []
                        longitudes = []
                        j = 1
                        while j + index < len(lines) and not lines[
                            index + j
                        ].startswith("STAND:"):
                            if lines[index + j].startswith("COORD:"):
                                _, lat_str, lon_str = lines[index + j].split(":")
                                latitudes.append(parse_latitude(lat_str))
                                longitudes.append(parse_longitude(lon_str))
                                j += 1

                            j += 1

                        self.add_stand(
                            Stand(
                                icao=icao,
                                name=stand_name,
                                lat=latitudes,
                                lon=longitudes,
                            )
                        )

                    elif len(parts) == 6:
                        _, icao, stand_name, lat_str, lon_str, _ = parts
                        self.add_stand(
                            Stand(
                                icao=icao,
                                name=stand_name,
                                lat=parse_latitude(lat_str),
                                lon=parse_longitude(lon_str),
                            )
                        )
