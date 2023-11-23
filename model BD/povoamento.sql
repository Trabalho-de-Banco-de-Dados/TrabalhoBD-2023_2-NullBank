INSERT INTO `nullbank`.`Endereco` (`idEndereco`, `tipo_logradouro`, `nome_logradouro`, `numero`, `bairro`, `cep`, `cidade`, `estado`) VALUES (1, 'Rua', 'Rua Principal', 123, 'Centro', '12345-678', 'CidadeB', 'UF');
INSERT INTO `nullbank`.`Cliente` (`cpf`, `nome_completo`, `rg`, `orgao_emissor`, `uf_rg`, `data_nascimento_cliente`, `Endereco_idEndereco`) VALUES ('12345678901', 'Cliente A', '123456789', 'SSP', 'UF', '1980-01-01', 1);
INSERT INTO `nullbank`.`Agencia` (`idAgencia`, `nome`, `salario_montante_total`, `cidade`) VALUES (1, 'Agencia A', 0.00, 'CidadeA');
