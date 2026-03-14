-- 1. Criando a tabela de Produção
CREATE TABLE producao_cookies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_cookie TEXT NOT NULL,
    quantidade_lote INTEGER,
    temperatura_forno REAL,
    data_fabricacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Inserindo dados reais de teste
INSERT INTO producao_cookies (tipo_cookie, quantidade_lote, temperatura_forno)
VALUES ('Chocolate Chip', 120, 180.5),
       ('Double Chocolate', 80, 175.0),
       ('Aveia e Mel', 50, 190.0);

-- 3. Query de Engenheiro: Ver apenas lotes grandes (> 60 unidades)
SELECT tipo_cookie, quantidade_lote 
FROM producao_cookies 
WHERE quantidade_lote > 60;