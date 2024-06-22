import unittest
import os


def run_tests():
    """
    This functions runs all unit tests inside of /src/tests/ and subfolders"""

    # Get the absolute path of the directory containing this script (src/)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate up one directory to the project root
    project_root = os.path.dirname(script_dir)

    # Construct the path to the tests/ directory under src/
    tests_dir = os.path.join(project_root, "src", "tests")

    # Discover and run tests in the src/tests/ directory and its subdirectories
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(
        start_dir=tests_dir, pattern="test_*.py", top_level_dir=project_root
    )
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)


if __name__ == "__main__":
    run_tests()
