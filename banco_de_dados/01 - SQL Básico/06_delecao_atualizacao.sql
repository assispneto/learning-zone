-- Deleta um registro em trabalha_em
DELETE FROM trabalha_em
WHERE fcpf='12345678966' AND pnr=1;

-- Atualizar todos os funcionarios cujo departamento é 5 para departamento 1
UPDATE funcionario
SET dnr=1
WHERE dnr=5;