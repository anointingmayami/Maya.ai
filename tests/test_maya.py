import os
import shutil
import pytest
from click.testing import CliRunner
from maya_cli.maya_cli.cli import maya
from maya_cli.maya_cli.project_generator import PROJECT_STRUCTURE

TEST_PROJECT_NAME = "test_ai_project"

def project_exists(base_path, structure):
    """ Recursively checks if a project's folder structure exists. """
    for folder, sub_structure in structure.items():
        folder_path = os.path.join(base_path, folder)
        if not os.path.isdir(folder_path):
            return False
        if isinstance(sub_structure, dict) and not project_exists(folder_path, sub_structure):
            return False
    return True

@pytest.fixture(scope="function")
def cli_runner():
    """ Provides a Click test runner instance. """
    return CliRunner()

@pytest.fixture(scope="function", autouse=True)
def clean_test_project():
    """ Ensures test project is deleted before and after each test. """
    yield  # Run the test
    if os.path.exists(TEST_PROJECT_NAME):
        shutil.rmtree(TEST_PROJECT_NAME, ignore_errors=True)

def test_create_project(cli_runner):
    """ Tests project creation using the CLI command. """
    result = cli_runner.invoke(maya, ["create", TEST_PROJECT_NAME])
    
    assert result.exit_code == 0, f"Unexpected CLI exit code: {result.exit_code}"
    assert f"✅ AI project '{TEST_PROJECT_NAME}' created successfully!" in result.output
    assert project_exists(TEST_PROJECT_NAME, PROJECT_STRUCTURE), "Project structure mismatch."

def test_create_existing_project(cli_runner):
    """ Tests handling of duplicate project creation. """
    os.makedirs(TEST_PROJECT_NAME, exist_ok=True)
    
    result = cli_runner.invoke(maya, ["create", TEST_PROJECT_NAME])
    
    assert result.exit_code == 0, f"Unexpected CLI exit code: {result.exit_code}"
    assert f"Error: Project '{TEST_PROJECT_NAME}' already exists." in result.output
