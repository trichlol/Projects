/*33) Listar a coluna Divisao da tabela Departamento.*/
    SELECT
        Divisao
    FROM
        Departamento;

/*34) Listar a coluna Divisao da tabela Departamento, porém mostre somente linhas
distintas (sem repetição).*/
    SELECT
        DISTINCT(Divisao)
    FROM
        Departamento;

/*35) Crie uma cosulta que faça a concatenação entre as colunas Divisao e Local da
tabela Departamento, para separar as colunas utilize ‘ – ‘. Crie o um alias para
coluna ‘Divisão + Local‘*/
    SELECT
        Divisao + ' - ' + Local AS 'Local da Divisao'
    FROM
        Departamento;


/*36) Crie uma consulta que liste as colunas: NomeEmpregado e Salario da tabela
Empregado. Crie as seguintes colunas calculadas: (Conforme figura no PDF)*/
    SELECT
        NomeEmpregado,
        Salario,
        ISNULL(Salario,0) * 1.1 AS 'Salario Mais 10%',
        ISNULL(Salario,0) * 1.2 AS 'Salario Mais 20%',
        ISNULL(Salario,0) * 0.9 AS 'Salario Menos 10%',
        ISNULL(Salario,0) * 0.8 AS 'Salario Menos 20%',
    FROM
        Empregado;

/*37) Crie uma consulta que liste as colunas: NomeEmpregado e Salario da tabela
Empregado. Crie as seguintes colunas calculadas: (Conforme figura no PDF)*/
    SELECT
        NomeEmpregado,
        Salario,
        ISNULL(Salario,0) + ISNULL(Comissao,0) AS 'Salario Total',
        (ISNULL(Salario,0) + ISNULL(Comissao,0)) * 12 AS 'Salario Total Anual',
        (ISNULL(Salario,0) + ISNULL(Comissao,0)) * 0.02 AS 'Valor Desconto Plano de Saude',
        (ISNULL(Salario,0) + ISNULL(Comissao,0)) * 0.15 AS 'Valor Desconto Alimentacao',
        (ISNULL(Salario,0) + ISNULL(Comissao,0)) - ((ISNULL(Salario,0) + ISNULL(Comissao,0)) * (0.05 + 0.02 + 0.15)) AS 'Salario Liquido'
        ISNULL(Salario,0) / 30 AS 'Salario Diario',
        ISNULL(Salario,0) / 30 / 8 AS 'Salario por Hora',
        ISNULL(Salario,0) / 30 / 8 / 60 AS 'Salario por Minuto',
        ISNULL(Salario,0) / 30 / 8 / 60 /60 AS 'Salario por Segundo',
    FROM
        Empregado;