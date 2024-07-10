import pandas as pd
import pytest
from fastapi.testclient import TestClient

# Import the FastAPI app from the main module
from main import app

# Initialize the TestClient with the FastAPI app
client = TestClient(app)

# Fixture for providing the file path for upload
@pytest.fixture
def upload_file():
    return "./tests/data/test_data.csv"

# Fixture for mocking the save_file function in the utils.file_handler module
@pytest.fixture
def mock_save_file(mocker):
    return mocker.patch("utils.file_handler.save_file", return_value=None)

# Fixture for mocking the generate_balanced_clusters function in the greedy_algorithm.clustering module
@pytest.fixture
def mock_generate_balanced_clusters(mocker):
    return mocker.patch("greedy_algorithm.clustering.generate_balanced_clusters", return_value={
        "num_clusters": 3,
        "execution_time": 5,
        "avg_distance": 10,
        "calculated_day": 1,
        "clusters": [0, 1, 2]
    })

# Fixture for mocking the pandas.read_csv function to return a DataFrame with sample points
@pytest.fixture
def mock_points_file(mocker):
    points_df = pd.DataFrame({
        'LATITUDE': [1.0, 2.0, 3.0],
        'LONGITUDE': [4.0, 5.0, 6.0]
    })
    return mocker.patch("pandas.read_csv", return_value=points_df)

# Test the /upload route
def test_upload_file_route(upload_file, mock_save_file):
    # Open the test file and send a POST request to the /upload route
    with open(upload_file, "rb") as file:
        response = client.post(
            "/upload", files={"file": ("test_file.csv", file, "text/csv")})

    # Assert the response status code and JSON response
    assert response.status_code == 200
    assert response.json() == {
        "info": f"file 'test_file.csv' saved at 'storage/test_file.csv'", "file_location": "storage/test_file.csv"}

# Test the /optimization route
def test_run_optimization_route(mock_points_file, mock_generate_balanced_clusters):
    # Send a POST request to the /optimization route with sample data
    response = client.post("/optimization", json={"cluster_index": 0})

    # Assert the response status code and check for specific keys in the JSON response
    assert response.status_code == 200
    assert "initial_distance" in response.json()
    assert "path" in response.json()

# Test the /clustering route
def test_run_clustering_route(mock_generate_balanced_clusters):
    # Open the test file and send a POST request to the /clustering route
    with open("tests/data/test_data.csv", "rb") as file:
        response = client.post(
            "/clustering", files={"file": ("test_file.csv", file, "text/csv")})

    # Assert the response status code and check for specific keys in the JSON response
    assert response.status_code == 200
    assert "num_clusters" in response.json()
    assert "execution_time" in response.json()
    assert "avg_distance" in response.json()
    assert "calculated_day" in response.json()
    assert "clusters_file" in response.json()
    assert "points_file" in response.json()
