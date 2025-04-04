-- Inserindo usuários
INSERT INTO Users (name, email, is_admin) VALUES
('João Amaral', 'joao.amaral@email.com', 1),
('Carlos Lima', 'carlos.lima@email.com', 0),
('Ana Oliveira', 'ana.oliveira@email.com', 0),
('Lucas Mendes', 'lucas.mendes@email.com', 0),
('Maria Souza', 'maria.souza@email.com', 0);

-- Inserindo tipos de manifestações
INSERT INTO ManifestTypes (name) VALUES
('Reclamação'),
('Sugestão'),
('Elogio'),
('Denúncia'),
('Dúvida');

-- Inserindo manifestações
INSERT INTO Manifestations (type_id, user_id, name, description, date, is_done) VALUES
(1, 5, 'Problema no sistema', 'Sistema apresenta erros frequentes.', '2025-04-01', 0),
(2, 2, 'Melhoria na plataforma', 'Seria interessante adicionar um modo noturno.', '2025-04-02', 0),
(3, 3, 'Ótimo atendimento', 'Fui muito bem atendida pelo suporte.', '2025-04-02', 0),
(4, 4, 'Conduta inadequada', 'Funcionário foi rude no atendimento.', '2025-04-03', 0),
(5, 1, 'Dúvida sobre acesso', 'Não consigo acessar minha conta.', '2025-04-03', 0),
(1, 1, 'Teste', 'Apenas um teste de funcionalidade.', '2025-04-03', 0),
(3, 1, 'Estrutura boa', 'Gostei da nova interface do sistema.', '2025-04-04', 0),
(2, 2, 'Iluminação Melhor', 'Sugestão para melhorar a iluminação da empresa.', '2025-04-04', 0);
