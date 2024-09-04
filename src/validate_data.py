import os
import sys
import requests
from settings import ROOT_DIRECTORY, OUTPUT_DIRECTORY
from tasks.toml_data import TomlData


if __name__ == "__main__":
    tomldata = TomlData(
        data_dir=ROOT_DIRECTORY, output_dir=OUTPUT_DIRECTORY, export=False
    )

    if len(tomldata.errors) == 0:
        sys.exit(0)

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    REPO_OWNER = os.getenv("REPO_OWNER")
    REPO_NAME = os.getenv("REPO_NAME")
    workflow_run_number = os.getenv("WORKFLOW_RUN_NUMBER")

    issue_title = f"Error on workflow run {workflow_run_number}"
    issue_body = "\n".join(tomldata.errors)

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": issue_title, "body": issue_body}

    response = requests.post(url, json=data, headers=headers, timeout=5)

    if response.status_code == 201:
        print("Issue created successfully.")
    else:
        print(f"Failed to create issue: {response.status_code}")
    print(response.json())
