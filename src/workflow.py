from tasks.export_stands import export_hp_csv
from tasks.read_grp_data import GrpDataReader


if __name__ == "__main__":
    ROOT_DIRECTORY = "data/"
    airports = GrpDataReader().process_stand_files(ROOT_DIRECTORY)

    export_hp_csv(airports, "api/")
