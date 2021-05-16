###########       VIEW      ##################################################
#vizualiação de numeros utilizados com seu respectivo ddd e ddi

CREATE VIEW vw_numeros_utilizados
AS SELECT 
    CONCAT("+",di.valor," (", d.valor,") " , n.numero) as numero ,
    u.nome,
    u.cpf, 
    c.imsi as codigo_chip,
    o.nome as nome_operadora
FROM 
	Usuario u
INNER JOIN 
	Numero n 
ON 
	u.id = n.user_id
INNER JOIN 
	Chip c
ON 
	n.chip_id = c.id
INNER JOIN 
	Operadora o
ON 
	c.operadora_id = o.id
INNER JOIN 
	DDD d
ON 
	n.ddd_id = d.id
INNER JOIN 
	DDI di
ON 
	n.ddi_id = di.id
WHERE 
	c.disponivel = 0;