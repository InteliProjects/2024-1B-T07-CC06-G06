// Importando React, createContext e useState do React
import React, { createContext, useState } from 'react';

// Criando o contexto da aplicação
export const AppContext = createContext();

// Componente de provedor de contexto da aplicação
export const AppProvider = ({ children }) => {
  // Definindo estado para o cluster
  const [cluster, setCluster] = useState(null);

  // Retornando o provedor de contexto com o valor do estado do cluster
  return (
    <AppContext.Provider value={[cluster, setCluster]}>
      {children}
    </AppContext.Provider>
  );
};
