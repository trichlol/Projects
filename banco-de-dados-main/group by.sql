create database loja;
use loja;

create table estoque(
	codigo_estoque int primary key auto_increment,
    produto_estoque varchar(90) not null,
    quantidade_estoque int not null
);

alter table estoque add setor varchar(90) not null;

insert into estoque(produto_estoque, quantidade_estoque, setor) values
('feijão',12,'grãos'),
('arroz',30,'grãos'),
('macarrão',17,'grãos'),
('farinha',30,'grãos'),
('azeite',50,'óleos'),
('vinho',45,'bebidas'),
('água',12,'bebidas'),
('óleo de soja',13,'óleos'),
('óleo de coco',14,'óleos'),
('suco',10,'bebidas');

select * from estoque;

/*group by*/
select produto_estoque, max(quantidade_estoque) from estoque;
select setor, sum(quantidade_estoque) from estoque group by setor;
select setor, count(quantidade_estoque) from estoque group by setor;
select setor, sum(quantidade_estoque) from estoque group by setor having
sum(quantidade_estoque) >= 75;
select setor, sum(quantidade_estoque) from estoque group by setor order by
sum(quantidade_estoque);

/*Consultar a soma da quantidade em estoque agrupados por setor especificando
os setores óleos e grãos*/

select setor, sum(quantidade_estoque) from estoque group by setor having setor
in ('óleos', 'grãos');
/*having exerce função de where quando está sendo aplicado o GROUP BY*/

/*===================================================================================*/

create table vendas(
	codigo_vendas int auto_increment,
    codigo_estoque_vendas int not null,
    quantidade_vendas int,
    data_vendas date,
    primary key(codigo_vendas)
);

alter table vendas add foreign key(codigo_estoque_vendas)
references estoque(codigo_estoque); 

insert into vendas(codigo_estoque_vendas, quantidade_vendas, data_vendas) values
(1, 2, 20220815),
(2, 4, 20220815),
(3, 2, 20220815);

select * from vendas;

select * from vendas inner join estoque
on vendas.codigo_estoque_vendas=estoque.codigo_estoque;

select estoque.produto_estoque, vendas.quantidade_vendas, vendas.data_vendas
from vendas inner join estoque
on vendas.codigo_estoque_vendas=estoque.codigo_estoque
where vendas.quantidade_vendas>=2.66;

select estoque.produto_estoque, vendas.quantidade_vendas, vendas.data_vendas
from vendas right join estoque
on vendas.codigo_estoque_vendas=estoque.codigo_estoque;

select estoque.produto_estoque, vendas.quantidade_vendas, vendas.data_vendas
from vendas left join estoque
on vendas.codigo_estoque_vendas=estoque.codigo_estoque;

select avg(vendas.quantidade_vendas) from vendas;

/*Subconsulta = utiliza-se de outras consultas para a realização de uma nova consulta*/
select codigo_vendas, quantidade_vendas, data_vendas
from vendas where quantidade_vendas in(select avg(vendas.quantidade_vendas)
from vendas where data_vendas='20220815');

/*Realizar uma consulta que retorne o nome dos produtos que tenham vendas acima da média*/
select estoque.produto_estoque from vendas
inner join estoque on vendas.codigo_estoque_vendas=estoque.codigo_estoque
where vendas.quantidade_vendas>=(select avg(vendas.quantidade_vendas) from vendas);

/*=======================================================================================================*/

alter table vendas add vendedor varchar(90);

update vendas set vendedor='Fernando' where codigo_vendas=1;
update vendas set vendedor='Maria' where codigo_vendas=2;
update vendas set vendedor='José' where codigo_vendas=3;

insert into vendas values 
(10, 4, 2, '20220822', 'Fernando'),
(4, 5, 2, '20220822', 'Fernando'),
(5, 6, 3, '20220822', 'Maria'),
(6, 7, 1, '20220822', 'José'),
(7, 8, 4, '20220822', 'Maria'),
(8, 9, 3, '20220822', 'Maria'),
(9, 10, 4, '20220822', 'José');

/*Consultar o codigo_vendas de todas as vendas dos vendedores que tiveram os produtos com a maior quantidade vendida*/
select codigo_vendas from vendas
where quantidade_vendas in(select max(vendas.quantidade_vendas) from vendas);
 
select codigo_vendas, vendedor, quantidade_vendas from vendas
where vendedor in(select distinct(vendedor) from vendas
where quantidade_vendas = (select max(quantidade_vendas) from vendas));

/*=======================================================================================================*/

/*Consultar o produto mais vendido da loja*/
select estoque.produto_estoque, vendas.quantidade_vendas, vendas.codigo_estoque_vendas
from estoque inner join vendas
on vendas.codigo_estoque_vendas=estoque.produto_estoque
where quantidade_vendas in(select max(quantidade_vendas) from vendas);

select produto_estoque from estoque where codigo_estoque
in(select codigo_estoque_vendas from vendas
group by codigo_estoque_vendas
having codigo_estoque_vendas
in(select codigo_estoque_vendas from vendas
where quantidade_vendas = (select max(quantidade_vendas) from vendas)));