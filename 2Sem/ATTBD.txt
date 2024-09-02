CREATE TABLE Cliente(
    cod_cliente		numeric(4)	CONSTRAINT cod_cliePK PRIMARY KEY,
    nome_clie  		varchar(20)	CONSTRAINT nome_clieNM NOT NULL,
    endereco		varchar(30),
    cidade 			varchar(15),
    cep				char(8),
    uf				char(2),
    cnpj			char(16),
    ie				char(12)   
);

CREATE TABLE Vendedor(
    cod_ven			numeric(4)  CONSTRAINT cod_venPK PRIMARY KEY,
    nome_ven		varchar(20) CONSTRAINT nome_venNM NOT NULL,
    salario_fixo	numeric(10,2),
    comissao		char(1)
);

CREATE TABLE Produto(
    cod_prod  		numeric(4) CONSTRAINT cod_prodPK PRIMARY KEY,
    unidade   		varchar(3),
    descricao 		varchar(20),
    val_unit  		numeric(8,2)
);

CREATE TABLE Pedido(
    num_pedido 		numeric(4) CONSTRAINT num_pedidoPK PRIMARY KEY,
    pr_entrega 		numeric(3) CONSTRAINT pr_entregaNM NOT NULL,
    cod_clie       	REFERENCES Cliente(cod_cliente),
    cod_ven        	REFERENCES Produto(cod_prod)
);

CREATE TABLE item_pedido(
    num_pedido 		REFERENCES Pedido(num_pedido),
    cod_prod		REFERENCES Produto(cod_prod),
    quant      		numeric(8,2)
);

CREATE TABLE atualiza_preco(
    preco_anterior	numeric(8,2),
    preco_novo		numeric(8,2),
    dt_atualiza 	DATE,
    cd_prod        	REFERENCES Produto(cod_prod)
);

declare
    newVal numeric(8,2);
    percentUp numeric(4,1) := 20.0;
	var_id numeric(4) := 31;
	val numeric(8,2);
begin
    select val_unit into val from Produto where cod_prod = var_id;
	newVal := (100 / percentUp) * val + val;
	insert into atualiza_preco values (val, newVal, sysdate, var_id);
	update Produto set val_unit = newVal where cod_prod = var_id;
end;

select * from atualiza_preco;
select * from Produto where cod_prod = 31;

/Inserts Tabela Cliente/
INSERT INTO Cliente VALUES(720, 'Ana', 'Rua 17 n.19', 'Niterói', 24358310, 'RJ', '12113231/0001-34', 2134);
INSERT INTO Cliente VALUES(870, 'Flávio', 'Av. Pres. Vargas, 10', 'São Paulo', 22763931, 'SP', '22534126/9387-9', 4631); 
INSERT INTO Cliente VALUES(110, 'Jorge', 'Rua Caiapó, 13', 'Curitiba', 30078500, 'PR', '14512764/9834-9', '');
INSERT INTO Cliente VALUES(222, 'Lúcia', 'Rua Itabira, 123', 'Belo Horizonte', 22124391, 'MG', '283152123/9348-8', 2985); 
INSERT INTO Cliente VALUES(830, 'Mauricio', 'Av. Paulista, 1236', 'São Paulo', 3012683, 'SP', '32816985/7465-6', 9343);

INSERT INTO Cliente VALUES(130, 'Edmar', 'Rua da Praia, s/n', 'Salvador', 30079300, 'BA', '23463284/234-9', 7121);
INSERT INTO Cliente VALUES(410, 'Rodolfo', 'Largo da Lapa, 27', 'Rio de Janeiro', 30078900, 'RJ', '12835128/2346-9', 7431);
INSERT INTO Cliente VALUES(20, 'Beth', 'Av. Climério, 45', 'São Paulo', 25679300, 'SP', '32485126/7326-8', 9280);
INSERT INTO Cliente VALUES(157, 'Paulo', 'Trav. Moraes, casa 3', 'Londrina', 'PR', '', '32848223/324-2', 1923);
INSERT INTO Cliente VALUES(180, 'Lívio', 'Av. Beira Mar, 1256', 'Florianópolis', 30077500, 'SC', '12736571/2347-4', 1111);

INSERT INTO Cliente VALUES(260, 'Susana', 'Rua Lopes Mandes, 12', 'Niterói', 30046500, 'RJ', '21763571/232-9', 2530);
INSERT INTO Cliente VALUES(290, 'Renato', 'Rua Meireles, 123', 'São Paulo', 30225900, 'SP', '13276571/1231-4', 1820);
INSERT INTO Cliente VALUES(390, 'Sebastião', 'Rua da Igreja, 10', 'Uberaba', 30438700, 'MG', '32176547/213-3', 9071);
INSERT INTO Cliente VALUES(234, 'José', 'Quadra 3, Bl. 3, sl. 1003', 'Brasília', 22841650, 'DF', '21763576/1232-3', 2931);


/Inserts Tabela Vendedor/
INSERT INTO Vendedor VALUES(209, 'José', 1800, 'C');
INSERT INTO Vendedor VALUES(111, 'Carlos', 2490, 'A');
INSERT INTO Vendedor VALUES(11, 'João', 2780, 'C');
INSERT INTO Vendedor VALUES(240, 'Antônio', 9500, 'C');
INSERT INTO Vendedor VALUES(720, 'Felipe', 4600, 'A');
INSERT INTO Vendedor VALUES(213, 'Jonas', 2300, 'A');
INSERT INTO Vendedor VALUES(101, 'João', 2650, 'C');
INSERT INTO Vendedor VALUES(310, 'Josias', 870, 'B');
INSERT INTO Vendedor VALUES(250, 'Maurício', 2930, 'B');

/Inserts tabela Produto/
INSERT INTO Produto VALUES(25, 'Kg', 'Queijo', 0.97);
INSERT INTO Produto VALUES(31, 'BAR', 'Chocolate', 0.87); 
INSERT INTO Produto VALUES(78, 'L', 'Vinho', 2.00);
INSERT INTO Produto VALUES(22, 'M', 'Linho', 0.11); 
INSERT INTO Produto VALUES(30, 'SAC', 'Açúcar', 0.30);

INSERT INTO Produto VALUES(53, 'M', 'Linha', 1.80);
INSERT INTO Produto VALUES(13, 'G', 'Ouro', 6.18);
INSERT INTO Produto VALUES(45, 'M', 'Madeira', 0.25);
INSERT INTO Produto VALUES(87, 'M', 'Cano', 1.97);
INSERT INTO Produto VALUES(77, 'M', 'Papel', 1.05);


/Inserts da Tabela Pedido/
INSERT INTO Pedido VALUES(121, 20, 410, 209);
INSERT INTO Pedido VALUES(97, 20, 720, 101);
INSERT INTO Pedido VALUES(101, 15, 720, 101);
INSERT INTO Pedido VALUES(137, 20, 720, 720);
INSERT INTO Pedido VALUES(148, 20, 720, 101);
INSERT INTO Pedido VALUES(189, 15, 870, 213);
INSERT INTO Pedido VALUES(104, 30, 110, 101);
INSERT INTO Pedido VALUES(203, 30, 830, 250);
INSERT INTO Pedido VALUES(98, 20, 410, 209);
INSERT INTO Pedido VALUES(143, 30, 201, 11);
INSERT INTO Pedido VALUES(105, 30, 180, 240);
INSERT INTO Pedido VALUES(111, 15, 260, 240);
INSERT INTO Pedido VALUES(103, 20, 260, 11);
INSERT INTO Pedido VALUES(91, 20, 260, 11);
INSERT INTO Pedido VALUES(138, 20, 260, 11);
INSERT INTO Pedido VALUES(108, 15, 290, 310);
INSERT INTO Pedido VALUES(119, 30, 390, 250);
INSERT INTO Pedido VALUES(127, 10, 410, 11);


/Inserts tabela item_pedido/
INSERT INTO item_pedido VALUES(121, 25, 10);
INSERT INTO item_pedido VALUES(121, 31, 35);
INSERT INTO item_pedido VALUES(97, 77, 20);
INSERT INTO item_pedido VALUES(101, 31, 9);
INSERT INTO item_pedido VALUES(101, 78, 18);
INSERT INTO item_pedido VALUES(101, 13, 5);
INSERT INTO item_pedido VALUES(98, 77, 5);
INSERT INTO item_pedido VALUES(148, 45, 8);
INSERT INTO item_pedido VALUES(148, 31, 7);
INSERT INTO item_pedido VALUES(148, 77, 3);
INSERT INTO item_pedido VALUES(148, 25, 10);
INSERT INTO item_pedido VALUES(148, 78, 30);
INSERT INTO item_pedido VALUES(104, 53, 32);
INSERT INTO item_pedido VALUES(203, 31, 6);
INSERT INTO item_pedido VALUES(189, 78, 45);
INSERT INTO item_pedido VALUES(143, 31, 20);
INSERT INTO item_pedido VALUES(143, 78, 10);