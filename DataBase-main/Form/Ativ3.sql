/*62) Criar a tabela de departamento, conforme abaixo:*/

CREATE TABLE Departamento (
    IdDepto     int         NOT NULL,
    NomeDepto   varchar(15) NOT NULL,
    Gerente     int         NOT NULL,
    Divisao     varchar(10) NOT NULL,
    Local       varchar(15) NOT NULL,

    PRIMARY KEY (IdDepto)
);

/*63) Criar a tabela de empregado, conforme abaixo:*/
CREATE TABLE Empregado (
    IdEmpregado     int             NOT NULL,
    NomeEmpregado   varchar(20)     NOT NULL,
    IdDepto         int             NOT NULL,
    Cargo           varchar(6)      NOT NULL,
    Tempo_Emp       int             NULL,
    Salario         decimal(10,2)   NULL,
    Comissao        decimal(10,2)   NULL,

    PRIMARY KEY (IdEmpregado)
);

/*64.Na tabela de empregado criar a chave estrangeira com o campo iddepto e
a tabela Departamento.*/
    ALTER TABLE
        Empregado
    ADD
        CONSTRAINT FK_Departamento
    FOREIGN KEY (IdDepto)
    REFERENCES 
        Departamento(IdDepto);