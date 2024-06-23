from tasks.read_grp_data import GrpDataReader


if __name__ == "__main__":
    ROOT_DIRECTORY = "data/"
    GrpDataReader().process_stand_files(ROOT_DIRECTORY)
