# Importing necessary modules
from fastapi import APIRouter, HTTPException
from typing import List, Tuple
import pandas as pd

# Creating an API router
router = APIRouter()

# Path to the points file
POINTS_FILE_PATH = 'storage/points_file.csv'

# Route to get coordinates
@router.get("/coordinates")
async def get_coordinates() -> List[Tuple[float, float]]:
    try:
        # Load the points CSV file
        points_df = pd.read_csv(POINTS_FILE_PATH)

        # Transform the DataFrame into a list of coordinate tuples (LATITUDE, LONGITUDE)
        coordinates = [(row['LATITUDE'], row['LONGITUDE']) for _, row in points_df.iterrows()]

        return coordinates
    except FileNotFoundError:
        # Return a 404 error if the file is not found
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        # Return a 500 internal server error for any other exceptions
        raise HTTPException(status_code=500, detail=str(e))
