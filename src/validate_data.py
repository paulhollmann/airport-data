from settings import ROOT_DIRECTORY, OUTPUT_DIRECTORY
from tasks.toml_data import TomlData


if __name__ == "__main__":
    TomlData(data_dir=ROOT_DIRECTORY, output_dir=OUTPUT_DIRECTORY, export=False)
