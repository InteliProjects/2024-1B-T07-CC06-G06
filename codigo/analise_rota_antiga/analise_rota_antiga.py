import pandas as pd
import math

# Calculate the distance between two points
def length(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Load the dataset
directory = 'codigo\dataset\AMOSTRA_TOTAL.csv'
df = pd.read_csv(directory, delimiter=';')
points = df[['LATITUDE', 'LONGITUDE', 'CODIGO_ROTA', 'SEQUENCIA']].values

rotas = {}

# Group the points by route
for point in points:
    codigo_rota = point[2]
    if codigo_rota not in rotas:
        rotas[codigo_rota] = []
    rotas[codigo_rota].append(point)

print(rotas['87_105'])

# Sort the points in each route by sequence
for rota in rotas:
    rotas[rota] = sorted(rotas[rota], key=lambda x: x[3])

print('\n\nSORTED', rotas['87_105'])

totalDist=0

# Calculate the total distance for each route
for rota in rotas:
    rotaDist=0
    count=0
    for i in range(len(rotas[rota])-1):
        rotaDist+= length(rotas[rota][i], rotas[rota][i+1])
    rotaDist+= length(rotas[rota][-1], rotas[rota][0])
    totalDist+=rotaDist
    print('Rota:', rota, 'Distancia rota:', rotaDist)
    if rotaDist==0 or rotaDist==0.0 or rotaDist=='0' or rotaDist=='0.0':
        count+=1

# Print the total distance and the number of routes with distance 0
print('Distancia total:', totalDist)
print('Rotas com distancia 0:', count)