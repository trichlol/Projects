/*01) Lista Nome e salário de todos os Empregados.*/
    SELECT
        NomeEmpregado,
        Salario
    FROM
        Empregado;
        
/*02) Lista Nome e Local de todos os Departamentos.*/
    SELECT
        NomeDepto,
        Local
    FROM
        Departamento;

/*03) Lista Nome, salário e comissão dos Empregados com salario maior que 1.800.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao
    FROM
        Empregado;
    WHERE
        Salario > 1800;

/*04) Lista Nome, divisão e Local dos Departamentos da divisão SUL.*/
    SELECT
        NomeDepto,
        Divisao,
        Local
    FROM
        Departamento
    WHERE
        Divisao = 'SUL';

/*05) Lista Nome, departamento, salario e cargo dos Empregados com cargo GER e
salário menor que 2.000.*/
    SELECT
        NomeEmpregado,
        IdDepto,
        Salario,
        Cargo
    FROM
        Empregado
    WHERE
        Cargo = 'GER' AND 
        Salario < 2000;

/*06) Lista todos os dados dos Empregados com cargo ATEND ou salário entre 1.800
e 2.000.*/
    SELECT
        *
    FROM
        Empregado
    WHERE
        Cargo = 'ATEND' OR
        Salario BETWEEN 1800 AND 2000;

/*07) Lista Nome, Salário, comissão e remuneração total (Salário + Comissão) de
todos os empregados.  */
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado;

/*08) Lista Nome, Salário, comissão e remuneração total (Salário + Comissão) de
todos os empregados com salário maior que 2.000 ou comissão maior que 700.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario > 2000 OR
        Comissao > 700;

/*09) Lista Nome, Salário, comissão e remuneração total de todos os empregados
com remuneração total menor que 1.800.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario + Comissao < 1800;

/*10) Lista Nome e cargo dos Empregados que o nome comece com a letra D.*/
    SELECT
        NomeEmpregado,
        Cargo
    FROM
        Empregado
    WHERE
        NomeEmpregado LIKE 'D%';

/*11) Lista Nome e cargo dos Empregados que o nome tenha N como terceira letra.*/
    SELECT
        NomeEmpregado,
        Cargo
    FROM
        Empregado
    WHERE
        NomeEmpregado LIKE '__N%';

/*12) Lista Nome e cargo dos Empregados que o nome tenha N (maiúscula ou minúscula)
como terceira letra.*/
    SELECT
        NomeEmpregado,
        Cargo
    FROM
        Empregado
    WHERE
        NomeEmpregado LIKE '__N%' OR
        NomeEmpregado LIKE '__n%';

/*13) Lista Nome, Salário, comissão e remuneração total  (Salário + Comissão) de
todos os empregados com salário maior que 2.000 ou comissão maior que 800.
Apresenta o resultado classificado em ordem alfabética de nome.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario > 2000 OR
        Comissao > 800
    ORDER BY
        NomeEmpregado;

/*14) Lista Nome, Salário, comissão e remuneração total (Salário + Comissão) de
todos os empregados com salário maior que 2.000 ou comissão maior que 800.
Apresenta o resultado classificado em ordem crescente de salario.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario > 2000 OR
        Comissao > 800
    ORDER BY
        Salario;

/*15) Lista Nome, Salário, comissão e remuneração total (Salário + Comissão) de
todos os empregados com salário maior que 2.000 ou comissão maior que 800.
Apresenta o resultado classificado em ordem decrescente de salario.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario > 2000 OR
        Comissao > 800
    ORDER BY
        Salario DESC;

/*16) Lista Nome, Salário, comissão e remuneração total (Salário + Comissão) de
todos os empregados com salário maior que 2.000 ou comissão maior que 800.
Apresenta o resultado classificado em ordem crescente de remuneração total.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario > 2000 OR
        Comissao > 800
    ORDER BY
        Salario + Comissao;

/*17) Lista Nome, Salário, comissão e remuneração total de todos os empregados
com salário maior que 2.000 ou comissão maior que 800. Apresenta o resultado
classificado em ordem crescente de departamento e em cada departamento, em ordem
decrescente de salario.*/
    SELECT
        NomeEmpregado,
        Salario,
        Comissao,
        Salario + Comissao AS 'Remuneração Total'
    FROM
        Empregado
    WHERE
        Salario > 2000 OR
        Comissao > 800
    ORDER BY
        IdDepto,
        Salario DESC;

/*18) Lista o maior salário, o menor salário e a média dos salários de todos os
Empregados.*/
    SELECT
        MAX(Salario),
        MIN(Salario),
        AVG(Salario)
    FROM
        Empregado;

/*19) Lista o maior salário, o menor salário, a média dos salários e a quantidade
dos Empregados com cargo GER ou VENDAS.*/
    SELECT
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    WHERE
        Cargo IN ('GER', 'VENDAS');

/*20) Lista  o cargo, o maior salário, o menor salário, a média dos salários e a
quantidade dos Empregados para cada cargo.*/
    SELECT
        Cargo,
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    GROUP BY
        Cargo;

/*21) Lista  o departamento, o maior salário, o menor salário, a média dos salário
e a quantidade dos Empregados para cada departamento.*/
    SELECT
        IdDepto,
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    GROUP BY
        IdDepto;

/*22) Lista  o departamento, o maior salário, o menor salário, a média dos salários
e a quantidade dos Empregados para cada departamento, considerando somente empregados
com salário maior que 1.800.*/
    SELECT
        IdDepto,
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    WHERE
        Salario > 1800
    GROUP BY
        IdDepto;

/*23) Lista  o departamento, o cargo, o maior salário, o menor salário, a média dos
salários e a quantidade dos Empregados para cada cargo dentro de cada departamento.*/
    SELECT
        IdDepto,
        Cargo,
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    GROUP BY
        IdDepto,
        Cargo;

/*24) Lista  o departamento, o maior salário, o menor salário, a média dos salários
e a quantidade dos Empregados, apresentando somente departamentos que tenham pelo
menos 5 empregados. */
    SELECT
        IdDepto,
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    GROUP BY
        IdDepto
    HAVING 
        COUNT(*) >= 5;

/*25) Lista  o departamento, o maior salário, o menor salário, a média dos salários
e a quantidade dos Empregados com salário maior que 1.400, apresentando somente
departamentos que tenham pelo menos 3 empregados nessa condição.*/
    SELECT
        IdDepto,
        MAX(Salario),
        MIN(Salario),
        AVG(Salario),
        COUNT(*)
    FROM
        Empregado
    WHERE
        Salario > 1400
    GROUP BY
        IdDepto
    HAVING
        COUNT(*) >= 3;

/*26) Lista todos os dados dos Empregados que não tem comissão (ausência de valor).*/
    SELECT
        *
    FROM
        Empregado
    WHERE
        Comissao IS NULL;

/*27) Lista nome e salário dos empregados com salário menor que a média dos salários.*/
    SELECT
        NomeEmpregado,
        Salario
    FROM
        Empregado
    WHERE
        Salario < ( SELECT
                        AVG(Salario)
                    FROM
                        Empregado);

/*28) Lista os códigos de departamento que tenham empregados com salário maior que
a média de todos os salários (sem repetir códigos de departamento).*/
    SELECT
        DISTINCT(IdDepto)
    FROM
        Empregado
    WHERE
        Salario > ( SELECT
                        AVG(Salario)
                    FROM
                        Empregado);

/*29) Lista nome e salário dos empregados que tenham o menor salário em seu
departamento.*/
    SELECT
        NomeEmpregado,
        Salario
    FROM
        Empregado
    WHERE
        Salario = ( SELECT
                        MIN(Salario)
                    FROM
                        Empregado);

/*30) Lista quantos empregados em cada departamento tem salário maior que a média
de todos os salários.*/
    SELECT
        IdDepto,
        COUNT(*)
    FROM
        Empregado
    WHERE
        Salario > ( SELECT
                        AVG(Salario)
                    FROM
                        Empregado)
    GROUP BY
        IdDepto;