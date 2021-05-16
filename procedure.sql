################    PROCEDURE     #############################
#stored procedure que seleciona chips disponiveis por operadora

DELIMITER $$
CREATE PROCEDURE selecionar_chips_disponiveis (IN _operadora VARCHAR(255))
BEGIN  
SELECT c.imsi as codigo_chip FROM Chip c
INNER JOIN Operadora o
ON 
	c.operadora_id = o.id
WHERE 
    o.nome like CONCAT('%', _operadora, '%')
AND
    c.disponivel = 1;

END $$
DELIMITER ;
