/*Criar um banco de dados*/
CREATE DATABASE cia;

/*Usar um banco de dados*/
USE cia;

/*Criar tabela*/
CREATE TABLE DEPARTAMENTO (
	cd_departamento INT			NOT NULL,
    nm_departamento VARCHAR(30) NOT NULL,
    nr_departamento INT			NOT NULL,
    
    CONSTRAINT PK_DEPARTAMENTO PRIMARY KEY(cd_departamento)
);

/*Inserir informações dentro de uma tabela*/
INSERT INTO DEPARTAMENTO(cd_departamento, nm_departamento, nr_departamento) VALUES(1010,'RH',90010);
INSERT INTO DEPARTAMENTO(cd_departamento, nm_departamento, nr_departamento) VALUES(1020,'Compras',109320);
INSERT INTO DEPARTAMENTO(cd_departamento, nm_departamento, nr_departamento) VALUES(1030,'Vendas',853559);
INSERT INTO DEPARTAMENTO(cd_departamento, nm_departamento, nr_departamento) VALUES(1040,'Financeiro',1000100);
INSERT INTO DEPARTAMENTO(cd_departamento, nm_departamento, nr_departamento) VALUES(1050,'Diretoria',550100);

/*Selecionar todos os arquivos de uma tabela*/
SELECT * FROM DEPARTAMENTO;

CREATE TABLE PROJETO (
	cd_projeto 				INT				NOT NULL,
    nm_projeto 				VARCHAR(30) 	NOT NULL,
    dt_inicioProjeto 		DATE			NOT NULL,
    dt_finalProjeto 		DATE,
    cd_departamentoControla INT				NOT NULL,
    
    /*Definição de chave primária e chave extrangeira*/
    CONSTRAINT PK_PROJETO 				PRIMARY KEY(cd_projeto),
    CONSTRAINT FK_PROJETO_Departamento 	FOREIGN KEY(cd_departamentoControla) REFERENCES DEPARTAMENTO(cd_departamento)
);

CREATE TABLE GENERO (
	cd_genero 	INT 			NOT NULL,
    ds_genero 	VARCHAR(20)		NOT NULL,
    abr_genero 	CHAR(5)			NOT NULL,
    
    CONSTRAINT PK_GENERO PRIMARY KEY(cd_gerero)
);

CREATE TABLE FUNCIONARIO (
	cd_funcionario 				INT 			NOT NULL,
    nm_funcionario 				VARCHAR(30) 	NOT NULL,
    dt_nascFuncionario 			DATE 			NOT NULL,
    /*Definição de números decimais*/
    vlr_salarioFuncionario 		DECIMAL(12,2)	NOT NULL,
    /*O exemplo diz que o número terá 12 caracteres, e contando de trás para frente, 2 números serão decimais*/
    cd_generoFuncionario 		INT 			NOT NULL,
    cd_departamentoFunnionario 	INT 			NOT NULL,
    
    CONSTRAINT PK_FUNCIONARIO 				PRIMARY KEY(cd_funcionario),
    CONSTRAINT FK_FUNCIONARIO_Genero 		FOREIGN KEY(cd_generoFuncionario) 				REFERENCES GENERO(cd_genero),
    CONSTRAINT FK_FUNCIONARIO_Departamento 	FOREIGN KEY(cd_departamentoFuncionario) 		REFERENCES DEPARTAMENTO(cd_departamento)
);

CREATE TABLE GRAU_PARENTESCO (
	cd_grauParentesco  INT 			NOT NULL,
	ds_grauParentesco  VARCHAR(20) 	NOT NULL,
    
	CONSTRAINT PK_GRAU_PARENTESCO PRIMARY KEY (cd_grauParentesco)
);

CREATE TABLE FUNCIONARIO_DEPENDENTE (
	cd_Funcionario					INT				NOT NULL,
	cd_FuncionarioDependente		INT				NOT NULL,
	nm_FuncionarioDependente		VARCHAR(30)		NOT NULL,
	dt_nascFuncionarioDependente	DATE			NOT NULL,
	cd_GeneroFuncionarioDependente	INT				NOT NULL,
	cd_GrauParentesco				INT				not null,
    
	CONSTRAINT PK_FUNCIONARIO_DEPENDENTE 					PRIMARY KEY (cd_FuncionarioDependente),
	CONSTRAINT FK_FUNCIONARIO_DEPENDENTE_Genero 			FOREIGN KEY(cd_GeneroFuncionarioDependente)	REFERENCES GENERO       (cd_Genero),
	CONSTRAINT FK_FUNCIONARIO_DEPENDENTE_Funcionario 		FOREIGN KEY(cd_Funcionario)					REFERENCES FUNCIONARIO (cd_Funcionario),
	CONSTRAINT FK_FUNCIONARIO_DEPENDENTE_Grau_Parentesco 	FOREIGN KEY(cd_GrauParentesco)				REFERENCES GRAUPARENTESCO (cd_GrauParentesco)
);

CREATE TABLE CARGO (
	cd_cargo INT 			NOT NULL,
    ds_cargo VARCHAR(20) 	NOT NULL,
    
    CONSTRAINT PK_CARGO PRIMARY KEY(cd_cargo)
);

CREATE TABLE FUNCIONARIO_LIMPEZA (
	cd_funcionarioLimpeza 	INT 	NOT NULL,
    vlr_jornadaTrabalho		INT 	NOT NULL,
    cd_cargo 				INT 	NOT NULL,
    
    CONSTRAINT PK_FUNCIONARIO_LIMPEZA 				PRIMARY KEY(cd_funcionarioLimpeza),
    CONSTRAINT FK_FUNCIONARIO_LIMPEZA_Funcionario 	FOREIGN KEY(cd_funcionarioLimpeza) 	REFERENCES FUNCIONARIO(cd_funcionario),
    CONSTRAINT FK_FUNCIONARIO_LIMPEZA_Cargo 		FOREIGN KEY(cd_cargo) 				REFERENCES CARGO(cd_cargo)
);

CREATE TABLE GRAU_ESCOLARIDADE (
	cd_grauEscolaridade INT 			NOT NULL,
    ds_grauEscolaridade VARCHAR(30) 	NOT NULL,
    
    CONSTRAINT PK_GRAU_ESCOLARIDADE PRIMARY KEY(cd_grauEscolaridade)
);

CREATE TABLE FUNCIONARIO_SECRETARIO(
	cd_funcionarioSecretario 	INT 	NOT NULL,
    cd_grauEscolaridade 		INT 	NOT NULL,
    
    CONSTRAINT PK_FUNCIONARIO_SECRETARIO 				PRIMARY KEY(cd_funcionarioSecretario),
    CONSTRAINT FK_FUNCIONARIO_SECRETARIO_Funcionario 	FOREIGN KEY(cd_funcionarioSecretario) 	REFERENCES FUNCIONARIO(cd_funcionario),
    CONSTRAINT FK_FUNCIONARIO_SECRETARIO_Escolaridade 	FOREIGN KEY(cd_grauEscolaridade) 		REFERENCES GRAU_ESCOLARIDADE(cd_grauEscolaridade)
);

CREATE TABLE AREA_ATUACAO (
	cd_areaAtuacao INT 			NOT NULL,
    ds_areaAtuacao VARCHAR(30) 	NOT NULL,
    
    CONSTRAINT PK_AREA_ATUACAO PRIMARY KEY(cd_areaAtuacao)
);

CREATE TABLE FUNCIONARIO_PESQUISADOR (
	cd_funcionarioPesquisador 	INT 	NOT NULL,
    cd_areaAtuacao 				INT 	NOT NULL,
    
    constraint PK_FUNCIONARIO_PESQUISADOR 				PRIMARY KEY(cd_funcionarioPesquisador),
    constraint FK_FUNCIONARIO_PESQUISADOR_Funcionario 	FOREIGN KEY(cd_funcionarioPesquisador) 	REFERENCES FUNCIONARIO(cd_funcionario),
    constraint FK_FUNCIONARIO_PESQUISADOR_Area_Atuacao 	FOREIGN KEY(cd_areaAtuacao) 			REFERENCES AREA_ATUACAO(cd_areaAtuacao)
);

CREATE TABLE PROJETO_FUNCIONARIO_PESQUISADOR (
	cd_projeto_funcionario_pesquisador 	INT 	NOT NULL,
    cd_funcionarioPesquisador 			INT 	NOT NULL,
    cd_projeto 							INT 	NOT NULL,
    qtd_horasSemanais 					INT 	NOT NULL,
    
    CONSTRAINT PK_PROJETO_FUNCIONARIO_PESQUISADOR 							PRIMARY KEY(cd_projeto_funcionario_pesquisador),
    CONSTRAINT FK_PROJETO_FUNCIONARIO_PESQUISADOR_Funcionario_Pesquisador 	FOREIGN KEY(cd_funcionarioPesquisador) 				REFERENCES FUNCIONARIO_PESQUISADOR(cd_funcionarioPesquisador),
    CONSTRAINT FK_PROJETO_FUNCIONARIO_PESQUISADOR_Projeto 					FOREIGN KEY(cd_projeto) 							REFERENCES PROJETO(cd_projeto)
);