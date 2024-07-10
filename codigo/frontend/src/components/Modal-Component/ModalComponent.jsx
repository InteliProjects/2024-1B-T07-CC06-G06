// Importando React e Modal do React Modal
import React from 'react';
import Modal from 'react-modal';
import styles from './ModalComponent.module.css';

// Componente do modal
const ModalComponent = ({ isOpen, onRequestClose, onConfirm, clusterId }) => (
    // Modal com props de controle de abertura e fechamento, estilos e acessibilidade
    <Modal
        isOpen={isOpen}
        onRequestClose={onRequestClose}
        className={styles.modalContent} 
        overlayClassName={styles.overlay}
        ariaHideApp={false} 
    >
        {/* Título do modal */}
        <h2 className={styles.title}>Confirmação</h2>
        {/* Mensagem com o ID do cluster */}
        <p>Deseja abrir o cluster: {clusterId} ?</p>
        {/* Botões de confirmação */}
        <div className={styles.modalButtons}> 
            {/* Botão para fechar o modal */}
            <button className={styles.buttonConfirm} onClick={onRequestClose}>Não</button>
            {/* Botão para confirmar a ação */}
            <button className={styles.buttonConfirm} onClick={onConfirm}>Sim</button>
        </div>
    </Modal>
);  

// Exportando o componente do modal
export default ModalComponent;
