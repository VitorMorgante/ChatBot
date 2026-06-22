# ROADMAP - ChatBot Institucional

## 1. Estado Atual da Auditoria (Fase 1)
Após a análise completa do diretório do projeto, constatou-se que não há arquivos de código-fonte presentes. Apenas as documentações (AGENTS.md, DATABASE.md, PRD.md) existem atualmente.

* **Funcionalidades implementadas**: Nenhuma (0%).
* **Funcionalidades ausentes**: Todas as funcionalidades descritas no PRD.
* **Divergências entre código e PRD**: Código inexistente, o que requer inicialização completa do projeto.
* **Divergências entre models.py e DATABASE.md**: O arquivo `models.py` não existe.
* **Problemas de arquitetura**: Não aplicável (ausência de código).
* **Problemas de segurança**: Não aplicável.
* **Problemas de performance**: Não aplicável.

## 2. Funcionalidades Concluídas
* Documentação de Requisitos (PRD)
* Documentação de Banco de Dados (DATABASE.md)
* Regras do Agente (AGENTS.md)

## 3. Funcionalidades Pendentes
* Inicialização do Projeto Django e estrutura de pastas (MVC).
* Configuração do PostgreSQL Neon e `.env`.
* RF01 - Cadastro de Professor
* RF02 - Cadastro de Aluno
* RF03 - Autenticação
* RF04 - Cadastro de Curso
* RF05 - Vinculação de Professor ao Curso
* RF06 - Vinculação de Aluno ao Curso
* RF07 - Upload de Material
* RF08 - Gerenciamento de Materiais
* RF09 - Criação de ChatBot
* RF10 - Associação de Materiais ao ChatBot
* RF11 - Consulta Inteligente
* RF12 - Histórico de Conversas
* RF13 - Controle de Permissões

## 4. Ordem de Implementação (Próximos Passos)

### Fase 2: Banco de Dados e Setup
* Criar projeto Django (`project`) e app principal (`website`).
* Remover SQLite e configurar PostgreSQL (Neon).
* Criar `.env.example` e gerenciar variáveis de ambiente (DATABASE_URL).

### Fase 3: Modelos
* Implementar `User`, `Student`, `Professor`, `Course`, `Material`, `ChatBot`, `Conversation`, e `Message` em `models.py`.
* Garantir UUIDs, `created_at`, `updated_at`, índices e validações conforme `DATABASE.md`.
* Gerar e rodar migrations iniciais.

### Fase 4: Requisitos Funcionais (Backend)
* Implementar a lógica de negócios e as rotas para atender do RF01 ao RF13.

### Fase 5: Interface (Frontend)
* Desenvolver templates utilizando HTML5, CSS3, Bootstrap 5 e jQuery.
* Criar as telas: Login, Dashboard, Cursos, Materiais, ChatBots, Conversas e Administração.

### Fase 6: IA (RAG)
* Implementar os serviços `embedding_service.py`, `retrieval_service.py` e `chatbot_service.py`.

### Fase 7: Segurança
* Auditoria OWASP, validação de inputs, middlewares de proteção (CSRF, XSS).
* Criação do `SECURITY_REPORT.md`.

### Fase 8: Testes
* Desenvolver testes unitários e de integração (Pytest) com mínimo de 80% de cobertura.

### Fase 9: Produção
* Configurar Gunicorn, Whitenoise, logs de aplicação.
* Criar `DEPLOYMENT.md`.
