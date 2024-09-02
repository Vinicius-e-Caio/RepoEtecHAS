CREATE TABLE Escola (
    Id_escola NUMBER(5) PRIMARY KEY,
    email VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(12),
    nome VARCHAR(100),
    UNIQUE (Id_escola, email)
);

CREATE TABLE Disciplina (
    Id_disciplina NUMBER(5) PRIMARY KEY UNIQUE,
    nome VARCHAR(100),
    carga_horaria DATETIME,
    descricao VARCHAR(255),
    fk_Escola_Id_escola NUMBER(5)
);

CREATE TABLE Aluno (
    Id_Aluno NUMBER(5) PRIMARY KEY,
    email VARCHAR(100),
    telefone VARCHAR(12),
    endereco VARCHAR(255),
    fk_Disciplina_Id_disciplina NUMBER(5),
    fk_Escola_Id_escola NUMBER(5),
    UNIQUE (email, Id_Aluno)
  	notas VARCHAR(2),
    faltas NUMBER(3),
);

ALTER TABLE Aluno ADD CONSTRAINT FK_Aluno_2
    FOREIGN KEY (fk_Disciplina_Id_disciplina)
    REFERENCES Disciplina (Id_disciplina);
 
ALTER TABLE Aluno ADD CONSTRAINT FK_Aluno_3
    FOREIGN KEY (fk_Escola_Id_escola)
    REFERENCES Escola (Id_escola);

ALTER TABLE Disciplina ADD CONSTRAINT FK_Disciplina_2
    FOREIGN KEY (fk_Escola_Id_escola)
    REFERENCES Escola (Id_escola);
    
INSERT INTO Aluno (Id_Aluno, email, telefone, endereco, fk_Disciplina_Id_disciplina, fk_Escola_Id_escola) VALUES (1, 'aluno1@email.com', '1122334455', 'Rua A, 123', 101, 201,'B',3);
INSERT INTO Aluno (Id_Aluno, email, telefone, endereco, fk_Disciplina_Id_disciplina, fk_Escola_Id_escola) VALUES (2, 'aluno2@email.com', '2233445566', 'Rua B, 234', 102, 202,'R',9);
INSERT INTO Aluno (Id_Aluno, email, telefone, endereco, fk_Disciplina_Id_disciplina, fk_Escola_Id_escola) VALUES (3, 'aluno3@email.com', '3344556677', 'Rua C, 345', 103, 203,'I',15);

INSERT INTO Escola (Id_escola, email, endereco, telefone, nome) VALUES (201, 'escola1@email.com', 'Av. Principal, 456', '4455667788', 'Escola Primária');
INSERT INTO Escola (Id_escola, email, endereco, telefone, nome) VALUES (202, 'escola2@email.com', 'Av. Secundária, 567', '5566778899', 'Escola Secundária');
INSERT INTO Escola (Id_escola, email, endereco, telefone, nome) VALUES (203, 'escola3@email.com', 'Av. Terciária, 678', '6677889900', 'Escola Terciária');

INSERT INTO Disciplina (Id_disciplina, nome, carga_horaria, descricao, fk_Escola_Id_escola) VALUES (101, 'Matemática', TO_DATE('2024-01-01 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Estudo dos números', 201);
INSERT INTO Disciplina (Id_disciplina, nome, carga_horaria, descricao, fk_Escola_Id_escola) VALUES (102, 'História', TO_DATE('2024-01-01 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Estudo dos eventos passados', 202);
INSERT INTO Disciplina (Id_disciplina, nome, carga_horaria, descricao, fk_Escola_Id_escola) VALUES (103, 'Ciências', TO_DATE('2024-01-01 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Estudo da natureza', 203);
