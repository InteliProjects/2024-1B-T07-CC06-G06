import React from 'react';

// Importing CSS styles for the Filter component
import './FilterAlgoritmo.css';

// Functional component for the filter section
const Filter = ({ setInicio }) => {
    const handleSetInicio = () => {
        setInicio(true); // Chamando a função setInicio com o valor true
    };

    return (
        <header className="header">
          <div className="header-filters">
            <button className="filter-button-route" onClick={handleSetInicio}>Inicio da rota</button>
          </div>
        </header>
    );   
}

// Exporting Filter component
export default Filter;
