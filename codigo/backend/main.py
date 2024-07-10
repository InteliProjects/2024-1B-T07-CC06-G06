# Importing FastAPI and CORS middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importing the route controllers
from controllers import cluster_controller, optimize_controller, coordinates_controller, clusters_catch_controller

# Creating the FastAPI instance
app = FastAPI()

# Configuring allowed origins for CORS
origins = [
    "http://localhost:5173",  
]

# Adding CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowing only the listed origins
    allow_credentials=True,  # Allowing credentials from origin
    allow_methods=["*"],  # Allowing all HTTP methods
    allow_headers=["*"],  # Allowing all headers
)

# Including the routes for the endpoints
app.include_router(cluster_controller.router, tags=["cluster"])  # Routes related to clusters
app.include_router(optimize_controller.router, tags=["optimize"])  # Routes related to optimization
app.include_router(coordinates_controller.router, tags=["coordinates"])  # Routes related to coordinates
app.include_router(clusters_catch_controller.router, tags=["clusters_catch"])  # Routes related to cluster capture
