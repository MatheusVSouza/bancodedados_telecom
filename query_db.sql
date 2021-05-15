create schema TelecomDB;

USE TelecomDB;

CREATE TABLE `Usuario`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255) NOT NULL,
    `cpf` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL
);

ALTER TABLE
    `Usuario` ADD UNIQUE `usuario_cpf_unique`(`cpf`);
ALTER TABLE
    `Usuario` ADD UNIQUE `usuario_email_unique`(`email`);
    
CREATE TABLE `Chip`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `operadora_id` INT NOT NULL,
    `fabricante_id` INT NOT NULL,
    `imsi` VARCHAR(255) NOT NULL
);

ALTER TABLE
    `Chip` ADD UNIQUE `chip_imsi_unique`(`imsi`);
CREATE TABLE `Numero`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `ddd_id` INT NOT NULL,
    `ddi_id` INT NOT NULL,
    `chip_id` INT NOT NULL,
    `numero` VARCHAR(255) NOT NULL,
    `disponivel` TINYINT(1) NOT NULL
);

CREATE TABLE `Agencia`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `operadora_origem` INT NOT NULL,
    `nome` VARCHAR(255) NOT NULL
);


CREATE TABLE `Plano`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `agencia_id` INT NOT NULL,
    `nome` VARCHAR(255) NOT NULL,
    `preco` DOUBLE(8, 2) NOT NULL,
    `pagamento` ENUM('') NOT NULL,
    `dt_expiracao` DATE NOT NULL
);

CREATE TABLE `Fabricante`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `razao_social` VARCHAR(255) NOT NULL,
    `cnpj` VARCHAR(255) NOT NULL
);

ALTER TABLE
    `Fabricante` ADD UNIQUE `fabricante_cnpj_unique`(`cnpj`);
CREATE TABLE `DDD`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `valor` VARCHAR(255) NOT NULL,
    `regiao` VARCHAR(255) NOT NULL
);

CREATE TABLE `DDI`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `valor` VARCHAR(255) NOT NULL,
    `pais` VARCHAR(255) NOT NULL
);

CREATE TABLE `Operadora`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255) NOT NULL,
    `cnpj` VARCHAR(255) NOT NULL
);

ALTER TABLE
    `Operadora` ADD UNIQUE `operadora_cnpj_unique`(`cnpj`);
CREATE TABLE `Assinatura`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `numero_id` INT NOT NULL,
    `plano_id` INT NOT NULL,
    `dt_criacao` DATE NOT NULL
);

CREATE TABLE `Torre`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `operadora_id` INT NOT NULL,
    `ddd_id` INT NOT NULL,
    `endereco` VARCHAR(255) NOT NULL,
    `alcance` DOUBLE(8, 2) NOT NULL,
    `altura` DOUBLE(8, 2) NOT NULL
);

ALTER TABLE
    `Numero` ADD CONSTRAINT `numero_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `Usuario`(`id`);
ALTER TABLE
    `Numero` ADD CONSTRAINT `numero_ddd_id_foreign` FOREIGN KEY(`ddd_id`) REFERENCES `DDD`(`id`);
ALTER TABLE
    `Numero` ADD CONSTRAINT `numero_ddi_id_foreign` FOREIGN KEY(`ddi_id`) REFERENCES `DDI`(`id`);
ALTER TABLE
    `Numero` ADD CONSTRAINT `numero_chip_id_foreign` FOREIGN KEY(`chip_id`) REFERENCES `Chip`(`id`);
ALTER TABLE
    `Chip` ADD CONSTRAINT `chip_operadora_id_foreign` FOREIGN KEY(`operadora_id`) REFERENCES `Operadora`(`id`);
ALTER TABLE
    `Chip` ADD CONSTRAINT `chip_fabricante_id_foreign` FOREIGN KEY(`fabricante_id`) REFERENCES `Fabricante`(`id`);
ALTER TABLE
    `Plano` ADD CONSTRAINT `plano_agencia_id_foreign` FOREIGN KEY(`agencia_id`) REFERENCES `Agencia`(`id`);
ALTER TABLE
    `Agencia` ADD CONSTRAINT `agencia_operadora_origem_foreign` FOREIGN KEY(`operadora_origem`) REFERENCES `Operadora`(`id`);
ALTER TABLE
    `Assinatura` ADD CONSTRAINT `assinatura_numero_id_foreign` FOREIGN KEY(`numero_id`) REFERENCES `Numero`(`id`);
ALTER TABLE
    `Assinatura` ADD CONSTRAINT `assinatura_plano_id_foreign` FOREIGN KEY(`plano_id`) REFERENCES `Plano`(`id`);
ALTER TABLE
    `Torre` ADD CONSTRAINT `torre_ddd_id_foreign` FOREIGN KEY(`ddd_id`) REFERENCES `DDD`(`id`);
ALTER TABLE
    `Torre` ADD CONSTRAINT `torre_operadora_id_foreign` FOREIGN KEY(`operadora_id`) REFERENCES `Operadora`(`id`);





##########################################################################################################################

#INSERTS::
INSERT INTO DDD(valor,regiao)
values (61, "Brasilia");

INSERT INTO DDD(valor,regiao)
values (62, "Goias");

INSERT INTO DDD(valor,regiao)
values (65, "Mato Grosso");

INSERT INTO DDD(valor,regiao)
values (67, "Mato Grosso do Sul");

INSERT INTO DDD(valor,regiao)
values (82, "Alagoas");

INSERT INTO DDD(valor,regiao)
values (71, "Bahia");

INSERT INTO DDD(valor,regiao)
values (84, "Rio Grande Do Norte");

INSERT INTO DDD(valor,regiao)
values (22, "Rio de Janeiro");

INSERT INTO DDD(valor,regiao)
values (11, "Sao Paulo");

INSERT INTO DDI(valor,pais)
values(54,"Argentina");

INSERT INTO DDI(valor,pais)
values(55,"Brasil");

INSERT INTO DDI(valor,pais)
values(1,"EUA");

INSERT INTO DDI(valor,pais)
values(34,"Espanha");

INSERT INTO DDI(valor,pais)
values(44,"Reino Unido");


INSERT INTO Usuario(nome,cpf,email)
values("Matheus Souza", "036.529.651-80", "matheusv.souzaa@gmail.com");

INSERT INTO Usuario(nome,cpf,email)
values("Thiago Vieira", "043.228.898-20", "thiago_vieira7@gmail.com");

INSERT INTO Usuario(nome,cpf,email)
values("Caio Aguiar", "098.112.442-09", "caiop_aguiar@outlook.com");

INSERT INTO Usuario(nome,cpf,email)
values("Cristina Soares", "042.998.561-02", "cristina.soaress@gmail.com");

INSERT INTO Usuario(nome,cpf,email)
values("Hamilton Pires", "022.871.332-23", "hamiltin.p@outlook.com");


INSERT INTO Operadora(nome,cnpj)
values("Claro", "58.517.582/0001-68");

INSERT INTO Operadora(nome,cnpj)
values("Vivo", "52.084.480/0001-10");

INSERT INTO Operadora(nome,cnpj)
values("TIM", "87.655.670/0001-24");

INSERT INTO Operadora(nome,cnpj)
values("Verizon", "64.494.339/0001-74");

INSERT INTO Operadora(nome,cnpj)
values("Sprint Nextel", "78.670.533/0001-78");

INSERT INTO Agencia(operadora_origem, nome)
values(3, "Correios");

INSERT INTO Agencia(operadora_origem, nome)
values(3, "Śurf");

INSERT INTO Agencia(operadora_origem, nome)
values(1, "Anatel");

INSERT INTO Agencia(operadora_origem, nome)
values(2, "Dry");

INSERT INTO Agencia(operadora_origem, nome)
values(4, "Verizon Communications");



INSERT INTO Fabricante(razao_social,cnpj)
values("Alo Social","92.663.906/0001-04");

INSERT INTO Fabricante(razao_social,cnpj)
values("GD","81.023.497/0001-65");

INSERT INTO Fabricante(razao_social,cnpj)
values("Valid","91.921.766/0001-64");

INSERT INTO Fabricante(razao_social,cnpj)
values("Watchdata","77.932.671/0001-15");

INSERT INTO Fabricante(razao_social,cnpj)
values("Eseye","91.549.174/0001-63");

INSERT INTO Fabricante(razao_social,cnpj)
values("Voy","92.429.394/0001-33");


INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(1,2,"5512920014780");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(1,6,"5521920193623");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(2,3,"5518920005653");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(2,2,"5511920101323");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(3,6,"5521920193675");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(3,6,"5511920101398");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(4,4,"5517933002182");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(4,4,"5512920014727");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(5,5,"5518920005654");

INSERT INTO Chip(operadora_id, fabricante_id, imsi)
values(5,5,"5517933002112");


INSERT INTO Pagamentos(tipo, valor, status, data)
values("", 0, "", CURRENT_DATE());

INSERT INTO Pagamentos(tipo, valor, status, data)
values("CARTÃO", 3230, "Pago", CURRENT_DATE());

INSERT INTO Pagamentos(tipo, valor, status, data)
values("CARTÃO", 4123, "Estornado", CURRENT_DATE());

INSERT INTO Pagamentos(tipo, valor, status, data)
values("BOLETO", 5413, "Pendente", CURRENT_DATE());

INSERT INTO Pagamentos(tipo, valor, status, data)
values("CARTÃO", 5213, "Pago", CURRENT_DATE());

INSERT INTO Pagamentos(tipo, valor, status, data)
values("CARTÃO", 7423, "Pendente", CURRENT_DATE());

INSERT INTO Pagamentos(tipo, valor, status, data)
values("BOLETO", 6372, "Pendente", CURRENT_DATE());



INSERT INTO Numero(user_id, ddd_id, ddi_id, chip_id, numero, disponivel)
values(1, 2, 2, 4, "31234124", 0);

INSERT INTO Numero(user_id, ddd_id, ddi_id, chip_id, numero, disponivel)
values(2, 2, 2, 2, "87189273", 0);

INSERT INTO Numero(user_id, ddd_id, ddi_id, chip_id, numero, disponivel)
values(3, 3, 2, 5, "12381252", 0);

INSERT INTO Numero(user_id, ddd_id, ddi_id, chip_id, numero, disponivel)
values(1, 2, 1, 3, "46637182", 0);

INSERT INTO Numero(user_id, ddd_id, ddi_id, chip_id, numero, disponivel)
values(4, 4, 3, 1, "72385193", 0);


INSERT INTO Plano(agencia_id, nome, preco, dt_expiracao, pagamento_id)
values(1, "Plano Fidelidade", 4123, CURRENT_DATE(), 1);

INSERT INTO Plano(agencia_id, nome, preco, dt_expiracao, pagamento_id)
values(1, "Felicidade Mobile", 3412, CURRENT_DATE(), 2);

INSERT INTO Plano(agencia_id, nome, preco, dt_expiracao, pagamento_id)
values(2, "Cliente Max", 5762, CURRENT_DATE(), 3);

INSERT INTO Plano(agencia_id, nome, preco, dt_expiracao, pagamento_id)
values(4, "Infinity", 8888, CURRENT_DATE(), 4);

INSERT INTO Plano(agencia_id, nome, preco, dt_expiracao, pagamento_id)
values(5, "Premiu", 9999999, CURRENT_DATE(), 5);


INSERT INTO Assinatura(numero_id, plano_id, dt_criacao)
values(5, 1, CURRENT_DATE());

INSERT INTO Assinatura(numero_id, plano_id, dt_criacao)
values(4, 2, CURRENT_DATE());

INSERT INTO Assinatura(numero_id, plano_id, dt_criacao)
values(3, 1, CURRENT_DATE());

INSERT INTO Assinatura(numero_id, plano_id, dt_criacao)
values(1, 3, CURRENT_DATE());

INSERT INTO Assinatura(numero_id, plano_id, dt_criacao)
values(2, 4, CURRENT_DATE());

INSERT INTO Assinatura(numero_id, plano_id, dt_criacao)
values(1, 5, CURRENT_DATE());


INSERT INTO Torre(operadora_id, ddd_id, endereco, alcance, altura)
values(1, 2, "Rua 97 1201", 2430, 130);

INSERT INTO Torre(operadora_id, ddd_id, endereco, alcance, altura)
values(1, 3, "Rua José Barroso 614", 3240, 180);

INSERT INTO Torre(operadora_id, ddd_id, endereco, alcance, altura)
values(2, 2, "Avenida Desembargador Clotário Portugal 373", 1500, 320);

INSERT INTO Torre(operadora_id, ddd_id, endereco, alcance, altura)
values(3, 1, "Rua São João 1517", 7800, 500);

INSERT INTO Torre(operadora_id, ddd_id, endereco, alcance, altura)
values(4, 1, "Quadra QNG 03 97", 6520, 380);

INSERT INTO Torre(operadora_id, ddd_id, endereco, alcance, altura)
values(5, 4, "Rua Maria Simões Fracaro 503", 2430, 120);














