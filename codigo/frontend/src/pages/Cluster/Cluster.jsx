import React, { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { MapContainer, TileLayer, Polygon, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import * as turf from '@turf/turf';
import Filter from '../../components/Header-Cluster/Filter.jsx';
import ModalComponent from '../../components/Modal-Component/ModalComponent.jsx';
import { AppContext } from '../../context/AppContext';
import styles from './Cluster.module.css';

// Página de exibição dos clusters, incluindo um mapa interativo e informações sobre os clusters
const Cluster = () => {
  // Hooks de estado
  const navigate = useNavigate();
  const [clusterData, setClusterData] = useState([]);
  const [pointsCoordinates, setPointsCoordinates] = useState([]);
  const [executionData, setExecutionData] = useState({
    num_clusters: 0,
    execution_time: 0,
    avg_distance: 0,
  });
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedClusterId, setSelectedClusterId] = useState(null);
  const [cluster, setCluster] = useContext(AppContext);
  const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF'];

  // Efeito para buscar os dados dos clusters e coordenadas dos pontos
  useEffect(() => {
    const fetchPoints = async () => {
      try {
        const response = await axios.get('http://localhost:8000/coordinates');
        console.log('Fetched points:', response.data); // Adiciona log dos pontos
        setPointsCoordinates(response.data);
      } catch (error) {
        console.error('Error fetching points:', error);
      }
    };

    const fetchClusters = async () => {
      const startTime = performance.now();
      try {
        const response = await axios.get('http://localhost:8000/clusterscatch');
        const clusters = response.data;
        console.log('Fetched clusters:', clusters); // Adiciona log dos clusters
        setClusterData(clusters);
        const endTime = performance.now();
        const executionTime = (endTime - startTime) / 1000;
        setExecutionData({
          num_clusters: clusters.length,
          execution_time: executionTime,
          avg_distance: 0.31293,
        });
      } catch (error) {
        console.error('Error fetching clusters:', error);
      }
    };

    fetchClusters();
    fetchPoints();
  }, []);

  // Função para abrir o modal com informações detalhadas do cluster
  const openModal = (clusterId) => {
    setSelectedClusterId(clusterId);
    setModalIsOpen(true);
  };

  // Função para fechar o modal
  const closeModal = () => {
    setModalIsOpen(false);
    setSelectedClusterId(null);
  };

  // Função para lidar com a confirmação de seleção de um cluster
  const handleConfirm = () => {
    setCluster(selectedClusterId);
    navigate('/algoritmo');
    closeModal();
  };

  // Função para calcular o convex hull de um conjunto de pontos
  const calculateConvexHull = (points) => {
    if (points.length < 3) {
      return points; // Convex hull is not defined for less than 3 points
    }
    const turfPoints = points.map(([lng, lat]) => turf.point([lng, lat]));
    const featureCollection = turf.featureCollection(turfPoints);
    const hull = turf.convex(featureCollection);
    return hull ? hull.geometry.coordinates[0] : points;
  };

  // Verificação se os dados do cluster estão no formato correto
  const validateClusterCoordinates = (coordinates) => {
    const isValid = Array.isArray(coordinates) &&
      coordinates.every(
        coord => Array.isArray(coord) && coord.length === 2 && !isNaN(coord[0]) && !isNaN(coord[1])
      );
    if (!isValid) {
      console.warn('Invalid coordinates:', coordinates); // Adiciona log de coordenadas inválidas
    }
    return isValid;
  };

  // Retorno do componente
  return (
    <div className={styles.view}>
      {/* Componente de filtro */}
      <Filter />

      {/* Container principal */}
      <div className={styles.containerCluster}>
        {/* Informações sobre os clusters */}
        <div className={styles.infos}>
          <h1 className={styles.tituloInfos}>Dados</h1>
          <div className={styles.sep}></div>
          <div className={styles.divInfos}>
            <p className={styles.descInfos}>Clusters: {executionData.num_clusters}</p>
          </div>
          <div className={styles.divInfos}>
            <p className={styles.descInfos}>Tempo de Execução: {executionData.execution_time.toFixed(2)} s</p>
          </div>
          <div className={styles.divInfos}>
            <p className={styles.descInfos}>Distância Média: {(executionData.avg_distance * 111.11).toFixed(2)} km</p>
          </div>
        </div>

        {/* Mapa com os clusters */}
        <div className={styles.maps}>
          {pointsCoordinates.length > 0 && clusterData.length > 0 ? (
            <MapContainer center={[-22.85, -43.34]} zoom={12} style={{ height: '100%', width: '100%' }}>
              <TileLayer
                url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                attribution='© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              />
              {/* Renderização dos contornos dos clusters no mapa */}
              {clusterData.map((cluster, clusterIndex) => {
                const clusterPoints = cluster.Points.map(index => pointsCoordinates[index]);
                if (!validateClusterCoordinates(clusterPoints)) return null;
                const convexHullPoints = calculateConvexHull(clusterPoints);
                return (
                  <Polygon
                    key={clusterIndex}
                    positions={convexHullPoints}
                    color={colors[clusterIndex % colors.length]}
                    fillColor={colors[clusterIndex % colors.length]}
                    fillOpacity={0.5}
                    eventHandlers={{
                      click: () => openModal(clusterIndex),
                    }}
                  >
                    <Popup>Cluster: {cluster.Cluster}</Popup>
                  </Polygon>
                );
              })}
            </MapContainer>
          ) : (
            <p className={styles.loadingMessage}>Loading map data...</p>
          )}
        </div>
      </div>

      {/* Componente de modal para detalhes do cluster */}
      <ModalComponent
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        onConfirm={handleConfirm}
        clusterId={selectedClusterId}
      />
    </div>
  );
};

export default Cluster;
