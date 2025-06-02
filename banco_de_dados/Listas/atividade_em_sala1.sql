DROP TABLE IF EXISTS livros ;

CREATE TABLE editoras (
    id INTEGER PRIMARY KEY,
    nome varchar(50)
);

CREATE TABLE autores (
    id INTEGER PRIMARY KEY,
    nome varchar(50)
);

CREATE TABLE livros (
    isbn CHAR(13) PRIMARY KEY,
    titulo varchar(50),
    ano_publicacao INTEGER,
    qtd_estoque INTEGER,
    valor DECIMAL(10, 2),
    id_editora INTEGER,
    FOREIGN KEY (id_editora) REFERENCES editoras(id)
);

CREATE TABLE livros_autores (
    isbn char(13),
    id_autor int,
    PRIMARY KEY(isbn, id_autor),
    FOREIGN KEY(isbn) REFERENCES livros(isbn),
    FOREIGN KEY(id_autor) REFERENCES autores(id)
);

INSERT INTO editoras VALUES
(1, 'Atica'),
(2, 'FTD'),
(3, 'Melhoramentos'),
(4, 'Novatec'),
(5, 'Bookman');

INSERT INTO autores VALUES
(1, 'João'),
(2, 'Maria'),
(3, 'José'),
(4, 'Lúcia'),
(5, 'Carlos'),
(6, 'Pedro'),
(7, 'Ana');



INSERT INTO livros VALUES
(213, 'Banco de Dados', 2011, 2, 40.00, 4),
(425, 'Sistemas Operacionais',	2010, 3, 80.00 ,3),
(732, 'Lógica de Programação',	2009, 1, 60.00 ,2),
(441, 'Programação Orientada a Objetos', 2012, 1, 70.00 ,1),
(659, 'Java para Nerds', 2010,	3, 100.0, NULL),
(863, 'Engenharia de Software', 2010,2, 40.00, 2),
(376, 'Redes de Computadores',	2008, 1, 100.00, 3);

INSERT INTO livros_autores VALUES
(732, 1),
(425, 3),
(659, 4),
(441, 2),
(659, 1),
(425, 5),
(213, 3);

-- Q1
SELECT titulo
FROM livros
WHERE valor = (
    SELECT max(valor)
    FROM livros
);

-- Q2 
SELECT DISTINCT a.nome
FROM autores a, livros_autores la
WHERE la.id_autor = a.id AND
      la.isbn IN(
                SELECT isbn
                FROM livros
                WHERE valor = (
                    SELECT min(valor)
                    FROM livros
                )
      );

SELECT a.nome
FROM livros l, autores a, livros_autores la
WHERE l.isbn=la.isbn AND 
      la.id_autor=a.id AND 
      l.valor = (
		SELECT min(l1.valor)
		FROM livros l1
       );
       

-- Q3
SELECT DISTINCT a.nome
FROM autores a, livros_autores la
WHERE la.id_autor = a.id AND
      la.isbn IN (
        SELECT isbn
        FROM livros
        WHERE valor > (
            SELECT AVG(valor)
            FROM livros
        )
      )
ORDER BY a.nome ASC;

-- Q4
SELECT titulo, valor*qtd_estoque
FROM livros
WHERE qtd_estoque > 1
ORDER BY valor*qtd_estoque DESC;

-- Q5
SELECT a.nome, COUNT(la.isbn) as count
FROM livros_autores la RIGHT OUTER JOIN autores a ON
 a.id = la.id_autor
GROUP BY a.id, a.nome
ORDER BY count DESC;

-- Q6
SELECT e.nome, (
    SELECT max(valor)
    FROM livros l
    WHERE l.id_editora=e.id
),
(
    SELECT min(valor)
    FROM livros l
    WHERE l.id_editora=e.id
)
FROM editoras e;

-- Q7
SELECT e.nome
FROM editoras e
WHERE (
    SELECT max(l.valor)
    FROM livros l
    WHERE e.id=l.id_editora
) > 30;

-- Q8
SELECT e.nome
FROM editoras e
WHERE (
    SELECT count(*)
    FROM livros l
    WHERE e.id=l.id_editora
) > 1;

-- Q9
SELECT a.nome
FROM autores a
WHERE EXISTS (
    SELECT *
    FROM editoras e, livros l, livros_autores la
    WHERE a.id=la.id_autor AND
          la.isbn=l.isbn AND
          l.id_editora=e.id AND
          e.nome='Melhoramentos' 
);

-- Q10.
SELECT a.nome
FROM autores a
WHERE NOT EXISTS (
    SELECT *
    FROM livros_autores la
    WHERE a.id=la.id_autor
);

-- Q11.
SELECT l.titulo
FROM livros l
WHERE l.valor >= ALL (
    SELECT l1.valor
    FROM livros l1
);

SELECT l.titulo
FROM livros l
WHERE l.valor >= (
    SELECT max(l1.valor)
    FROM livros l1
);

-- Q12.
SELECT l.titulo, e.nome, a.nome
FROM (editoras e FULL OUTER JOIN livros l ON e.id=l.id_editora)
      FULL OUTER JOIN livros_autores la ON l.isbn=la.isbn
      FULL OUTER JOIN autores  a ON la.id_autor=a.id;

-- Q13. a)
CREATE VIEW gasto_departamento AS
SELECT d.dnome, (
    SELECT SUM(f.salario)
    FROM funcionario f
    WHERE f.dnr=d.dnumero
) as soma
FROM departamento d
ORDER BY soma DESC;

CREATE VIEW gasto_departamento AS
SELECT d.dnome, sum(f.salario)
FROM funcionario f RIGHT OUTER JOIN departamento d ON f.dnr=d.dnumero
GROUP BY d.dnumero
ORDER BY sum(f.salario) DESC;

-- Q13 b)
CREATE VIEW local_func AS
SELECT p.projlocal, count(t.fcpf)
FROM projeto p LEFT OUTER JOIN trabalha_em t ON p.projnumero=t.pnr
GROUP BY p.projlocal;

-- Q13 c)
CREATE VIEW func_dependente AS
SELECT f.pnome, (
       SELECT COUNT(*) 
       FROM dependente d 
       WHERE d.fcpf=f.cpf AND d.sexo='F'
) as count_sexo_feminino ,
(   
    SELECT COUNT(*) 
    FROM dependente d 
    WHERE d.fcpf=f.cpf AND d.sexo='M'
) as count_sexo_masculino
FROM funcionario f;

SELECT *
FROM func_dependente;

-- Q13 d)


-- Q14
SELECT f.pnome || ' ' || f.minicial || ' ' || f.unome, COUNT(*), f1.pnome || ' ' || f1.minicial || ' ' || f1.unome, d.dnome
FROM funcionario f, trabalha_em t, funcionario f1, departamento d
WHERE f.cpf = t.fcpf AND
      f.cpf_supervisor = f1.cpf AND
      f.dnr = d.dnumero
GROUP BY f.cpf, f.pnome, f.minicial, f.unome, f1.pnome, f1.minicial, f1.unome, d.dnome;


-- Q15
SELECT f.pnome || ' ' || f.minicial || ' ' || f.unome, (
    SELECT COUNT(*)
    FROM trabalha_em t
    WHERE t.fcpf=f.cpf
) as count_projetos
FROM funcionario f
WHERE (
    SELECT COUNT(*)
    FROM trabalha_em t
    WHERE t.fcpf=f.cpf
) > 1;

SELECT f.pnome || ' ' || f.minicial || ' ' || f.unome, COUNT(*)
FROM funcionario f, trabalha_em t
WHERE f.cpf=t.fcpf
GROUP BY f.cpf, f.pnome, f.minicial, f.unome
HAVING COUNT(*)>1;