# Importando módulos necessários
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import csv

# Criando um roteador API
router = APIRouter()

# Caminho do arquivo de pontos
POINTS_FILE_PATH = 'storage/clusters.csv'

# Rota para obter clusters
@router.get("/clusterscatch", response_model=List[Dict[str, Any]])
async def get_clusters() -> List[Dict[str, Any]]:
    try:
        clusters = []

        # Abrindo o arquivo CSV e lendo os clusters
        with open(POINTS_FILE_PATH, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cluster_id = row['Cluster']
                points = eval(row['Data']) 
                clusters.append({"Cluster": cluster_id, "Points": points})

        return clusters
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
