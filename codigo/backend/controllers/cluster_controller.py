from fastapi import APIRouter, HTTPException, UploadFile, File
from greedy_algorithm.clustering import generate_balanced_clusters
import pandas as pd
import os
import logging
from services.cluster_service import cluster
import tempfile

router = APIRouter()

# Configuração do logger
logging.basicConfig(level=logging.INFO)

@router.post("/cluster")
async def run_clustering_route(file: UploadFile = File(...)):
    try:
        # Criar um diretório temporário para salvar o arquivo
        with tempfile.TemporaryDirectory() as temp_dir:
            # Definir o caminho completo do arquivo temporário
            file_path = os.path.join(temp_dir, file.filename)

            # Salvar o arquivo enviado pelo usuário
            with open(file_path, 'wb') as f:
                f.write(file.file.read())

            logging.info(f"File saved at: {file_path}")

            # Verificar se o diretório 'storage' existe, senão, criar
            storage_dir = './storage'
            if not os.path.exists(storage_dir):
                os.makedirs(storage_dir)

            # Verificar se já existe um arquivo com o mesmo nome no diretório 'storage'
            final_file_path = os.path.join(storage_dir, file.filename)
            if os.path.exists(final_file_path):
                os.remove(final_file_path)
                logging.info(f"Old file removed: {final_file_path}")

            # Mover o arquivo temporário para o diretório 'storage'
            os.rename(file_path, final_file_path)

            logging.info(f"File moved to: {final_file_path}")

            # Load and validate the file content
            try:
                data = pd.read_csv(final_file_path, delimiter=';')
            except pd.errors.EmptyDataError:
                logging.error("No columns to parse from file")
                raise HTTPException(status_code=400, detail="No columns to parse from file")
            except pd.errors.ParserError:
                logging.error("Error parsing CSV file")
                raise HTTPException(status_code=400, detail="Error parsing CSV file")
            
            logging.info("CSV file successfully read")

            # Call the cluster function and handle its potential errors
            try:
                result = cluster(final_file_path, 22, 6, 5, 1.2)
            except Exception as e:
                logging.error(f"Error in clustering function: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Clustering function error: {str(e)}")

            return result

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
