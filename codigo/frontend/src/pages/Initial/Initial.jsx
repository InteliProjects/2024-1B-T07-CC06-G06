import React, { useState } from 'react';
import axios from 'axios';
import logo from '../../assets/img/logo.png';
import styles from './Initial.module.css';
import { useNavigate } from 'react-router-dom';

const Initial = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setMessage('');
  };

  const handleFileRemove = () => {
    setFile(null);
    setMessage('');
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      setMessage('Por favor, selecione um arquivo.');
      return;
    }
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/cluster', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log('Info:', response.data);
      setMessage(`Sucesso: arquivo enviado. Redirecionando...`);
      localStorage.setItem('fileLocation', response.data.file_location);
      setTimeout(() => {
        navigate('/cluster');
      }, 3000);
    } catch (error) {
      console.log('Erro ao fazer upload:', error);
      setMessage('Erro ao fazer upload do arquivo.');
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <img src={logo} alt="Logo" className={styles.logo} />
        <p className={styles.description}>
        ESTA APLICAÇÃO TEM O OBJETIVO DE RECEBER DADOS EM FORMATO DE CSV E, ATRAVÉS DO ALGORITMO DESENVOLVIDO PELO GRUPO AEGEA, RETORNAR OS CLUSTERS QUE CONTÉM AS RESIDÊNCIAS E SUAS RESPECTIVAS ROTAS.
        </p>
        <form onSubmit={handleSubmit} className={styles.form}>
          <label className={styles.customFileUpload}>
            Selecionar Arquivo
            <input type="file" onChange={handleFileChange} />
          </label>
          {file && (
            <div className={styles.fileInfo}>
              <span>{file.name}</span>
              <button type="button" onClick={handleFileRemove}>Remover</button>
            </div>
          )}
          <button type="submit" className={styles.submitButton}>Enviar</button>
        </form>
        {message && <p className={styles.message}>{message}</p>}
      </div>
    </div>
  );
};

export default Initial;