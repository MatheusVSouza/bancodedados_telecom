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
