import React, { useEffect, useState, useRef, useContext } from 'react';
import axios from 'axios';
import Filter from '../../components/Filter-algorithm/Filter';
import styles from './Algorithms.module.css';
import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { AppContext } from '../../context/AppContext';

// Função para criar ícone personalizado para os marcadores
const createCustomIcon = (index, routeLength) => {
  let className = styles.customMarker;

  if (index === 0) {
    className = `${className} ${styles.firstMarker}`;
  }

  if (index === routeLength - 1) {
    className = `${className} ${styles.lastMarker}`;
  }

  return L.divIcon({
    className: className,
    html: `<div>${index}</div>`,
  });
};

const Algorithms = () => {
  // Hooks de estado
  const [distInicial, setDistInicial] = useState(0);
  const [points, setPoints] = useState([]);
  const [route, setRoute] = useState([]);
  const [executionTime, setExecutionTime] = useState(null);
  const [inicioClicado, setInicioClicado] = useState(false);
  const [selectedGroup, setSelectedGroup] = useState(null);
  const mapRef = useRef(null);
  const [cluster] = useContext(AppContext); 

  // Efeito para buscar os resultados da otimização e os pontos
  useEffect(() => {
    const startTime = performance.now();

    const fetchOptimizationResult = async () => {
      try {
        const response = await axios.post(`http://localhost:8000/optimize?cluster_index=${cluster}`, {});
        const endTime = performance.now();
        setExecutionTime((endTime - startTime) / 1000);
        setDistInicial(response.data.initial_distance);
        setRoute(response.data.path.split(' ').map(Number));
      } catch (error) {
        console.error('Error fetching optimization result:', error.response?.data || error.message);
      }
    };

    // Função para buscar os pontos no backend
    const fetchPoints = async () => {
      try {
        const response = await axios.get('http://localhost:8000/coordinates');
        setPoints(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchOptimizationResult();
    fetchPoints();
  }, [cluster]); 

  // Função para lidar com o clique na linha da tabela
  const handleRowClick = (group) => {
    setSelectedGroup(group);
  };

  // Dividindo os pontos em grupos de 22
  const routePoints = route.map(index => points[index]).filter(point => point !== undefined);
  const groupedPoints = [];
  for (let i = 0; i < routePoints.length; i += Math.ceil(routePoints.length / 22)) {
    groupedPoints.push(routePoints.slice(i, i + Math.ceil(routePoints.length / 22)));
  }

  // Efeito para ajustar a visualização do mapa quando o início é clicado
  useEffect(() => {
    if (inicioClicado && routePoints.length > 0) {
      const map = mapRef.current;
      map.setView(routePoints[0], 15);
      setInicioClicado(false);
    }
  }, [inicioClicado, routePoints]);

  // Retorno do componente
  return (
    <div className={styles.view}>
      {/* Componente de filtro */}
      <Filter setInicio={setInicioClicado} />
      <div className={styles.containerCluster}>
        <div className={styles.maps}>
          {/* Mapa com os marcadores e a rota */}
          <MapContainer ref={mapRef} center={[-22.85, -43.34]} zoom={12} style={{ height: '100%', width: '100%' }}>
            <TileLayer
              url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
              attribution='© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            />
            {selectedGroup && selectedGroup.map((point, index) => (
              <Marker key={index} position={point} icon={createCustomIcon(index, selectedGroup.length)}>
                <Popup>
                  Ponto {index}
                </Popup>
              </Marker>
            ))}
            <Polyline positions={selectedGroup || routePoints} color="red" weight={2} dashArray="5,10" />
            {selectedGroup === null && routePoints.length > 0 && (
              <>
                <Marker position={routePoints[0]} icon={createCustomIcon(0, routePoints.length)}>
                  <Popup>Início</Popup>
                </Marker>
                <Marker position={routePoints[routePoints.length - 1]} icon={createCustomIcon(routePoints.length - 1, routePoints.length)}>
                  <Popup>Fim</Popup>
                </Marker>
              </>
            )}
          </MapContainer>
        </div>
        <div className={styles.infos}>
          {/* Tabela com informações sobre as rotas */}
          <h1 className={styles.tituloInfos}>Dados</h1>
          <div className={styles.sep}></div>
          <table>
            <thead>
              <tr>
                <th>Rota</th>
                <th>Tempo de Execução (s)</th>
                <th>Distância (km)</th>
              </tr>
            </thead>
            <tbody>
              <tr onClick={() => handleRowClick(null)}>
                <td>{`Todos os pontos`}</td>
                <td>{executionTime !== null ? executionTime.toFixed(3) : 'Calculando...'}</td>
                <td>{(distInicial * 111.11).toFixed(3)}</td>
              </tr>
              {groupedPoints.map((group, index) => (
                <tr key={index} onClick={() => handleRowClick(group)}>
                  <td>{`Dia ${index + 1}`}</td>
                  <td>{executionTime !== null ? executionTime.toFixed(3) : 'Calculando...'}</td>
                  <td>{((distInicial * 111.11)/22).toFixed(3)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Algorithms;
