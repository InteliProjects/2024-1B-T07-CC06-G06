# Importing necessary modules
from fastapi import APIRouter, HTTPException
import logging
from greedy_algorithm.pathing import betterGreedy, totalDist, Point
from services.optimize_service import optimize

# Creating an API router
router = APIRouter()

# Logger configuration
logging.basicConfig(level=logging.INFO)

# Route for running optimization
@router.post("/optimize")
async def run_optimization(cluster_index: int):
    try:
        # Logging information about the received cluster index
        logging.info(f"Received cluster_index: {cluster_index}")

        # Paths to the points and clusters files
        points_file = 'storage/points_file.csv'
        clusters_file = 'storage/clusters.csv'

        # Logging information about the files being used
        logging.info(f"Using points file: {points_file}")
        logging.info(f"Using clusters file: {clusters_file}")

        # Running the optimization and returning the result
        return optimize(cluster_index, clusters_file, points_file)

    except FileNotFoundError:
        # Return a 404 error if the file is not found
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        # Logging the error
        logging.error(f"An error occurred: {e}")
        # Return a 500 internal server error for any other exceptions
        raise HTTPException(status_code=500, detail=str(e))
