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

    def process_file(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            blocks = content.split("\n\n")
            # FIXME: works only when stands are properly separated by newlines, most of them are but about 1,7% (34) are not

            for block in blocks:
                stand: Stand = self.process_block(block)
                if stand:
                    if stand.icao in self.airports:
                        self.airports[stand.icao].append(stand)
                    else:
                        self.airports[stand.icao] = [stand]

    def process_block(self, block) -> Stand:
        lines = block.strip().split("\n")

        icao = None
        stand = None
        lat = []
        lon = []

        for line in lines:
            line = line.strip()

            # skip comments
            if line.startswith("//"):
                continue

            if line.startswith("STAND:"):
                data = self.process_stand_line(line)
                if isinstance(data, Stand):
                    return data
                if isinstance(data, tuple):
                    icao = data[0]
                    stand = data[1]

            if line.startswith("COORD:"):
                latitude, longitude = self.process_coord_line(line)
                lat.append(latitude)
                lon.append(longitude)

        if icao and stand and len(lat) > 0 and len(lon) > 0:
            return Stand(icao=icao, stand=stand, lat=lat, lon=lon)

    def process_stand_line(self, line):
        parts = line.split(":")
        if len(parts) == 6:
            _, icao, stand, lat, lon, _ = parts[:6]
            return Stand(
                icao=icao,
                stand=stand,
                lat=parse_latitude(lat),
                lon=parse_longitude(lon),
            )

        if len(parts) == 3:
            _, icao, stand = parts[:3]
            return icao, stand

    def process_coord_line(self, line):
        _, lat, lon = line.split(":")
        return parse_latitude(lat), parse_longitude(lon)
