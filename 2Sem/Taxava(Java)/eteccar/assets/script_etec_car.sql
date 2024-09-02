create database ETEC_CAR;
use ETEC_CAR;


CREATE TABLE TBL_MARCA (
  ID_MARCA BIGINT PRIMARY KEY IDENTITY,
  TX_NOME VARCHAR(50) NOT NULL
);


CREATE TABLE TBL_MODELO (
    ID_MODELO BIGINT PRIMARY KEY IDENTITY,
    TX_NOME VARCHAR(50) NOT NULL,
    NR_POTENCIA NUMERIC(8,2),
    ID_MARCA BIGINT NOT NULL,
    FOREIGN KEY (ID_MARCA) REFERENCES TBL_MARCA (ID_MARCA)
);


CREATE TABLE TBL_AUTOMOVEL
(
    ID_AUTOMOVEL      BIGINT PRIMARY KEY IDENTITY,
    NR_ANO_FABRICACAO INT         NOT NULL,
    NR_ANO_MODELO     INT         NOT NULL,
    TP_COMBUSTIVEL    VARCHAR(50) NOT NULL,
    NR_PRECO          NUMERIC(8,2),
    NR_KM_ATUAL       INT         NOT NULL,
    ID_MODELO         BIGINT      NOT NULL,
    FOREIGN KEY (ID_MODELO) REFERENCES TBL_MODELO (ID_MODELO)
);


CREATE TABLE TBL_ACESSORIO
(
    ID_ACESSORIO BIGINT PRIMARY KEY IDENTITY,
    TX_DESCRICAO VARCHAR(150) NOT NULL
);


CREATE TABLE TBL_REL_AUTOMOVEL_ACESSORIO
(
    ID_AUTOMOVEL BIGINT NOT NULL,
    ID_ACESSORIO BIGINT NOT NULL,
    FOREIGN KEY (ID_AUTOMOVEL) REFERENCES TBL_AUTOMOVEL (ID_AUTOMOVEL),
    FOREIGN KEY (ID_ACESSORIO) REFERENCES TBL_ACESSORIO (ID_ACESSORIO)
);


