# DATABASE.md

---

# Visão Geral do Banco de Dados

Banco escolhido: PostgreSQL (Neon Serverless)

Tipo de Banco de Dados: Relacional

Estratégia de armazenamento:

Banco relacional normalizado seguindo a Terceira Forma Normal (3FN), utilizando chaves primárias UUID, integridade referencial por Foreign Keys, índices estratégicos para consultas frequentes e relacionamento N:N através de tabelas intermediárias.

O armazenamento será realizado em PostgreSQL Serverless (Neon), aproveitando escalabilidade automática, Point-In-Time Recovery (PITR) e alta disponibilidade.

---

# Modelo de Dados (Entidades)

## Entidade 1

Nome da entidade: User

Descrição:

Representa qualquer usuário autenticado do sistema.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | 550e8400-e29b |
| name | VARCHAR(255) | Sim | João Silva |
| email | VARCHAR(255) | Sim | joao@email.com |
| password_hash | TEXT | Sim | hashed_password |
| role | VARCHAR(20) | Sim | STUDENT |
| is_active | BOOLEAN | Sim | true |
| created_at | TIMESTAMP | Sim | 2026-06-22 |
| updated_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Email deve ser único.
* Senha deve possuir no mínimo 8 caracteres.
* Senha deve conter letras maiúsculas, minúsculas e números.
* Role deve ser STUDENT, PROFESSOR ou ADMIN.

---

## Entidade 2

Nome da entidade: Student

Descrição:

Representa um aluno do sistema.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| user_id | UUID | Sim | uuid |
| registration_number | VARCHAR(50) | Sim | 2026001 |
| created_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Usuário deve existir.
* Matrícula deve ser única.

---

## Entidade 3

Nome da entidade: Professor

Descrição:

Representa um professor da instituição.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| user_id | UUID | Sim | uuid |
| employee_code | VARCHAR(50) | Sim | PROF001 |
| created_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Usuário deve existir.
* Código funcional deve ser único.

---

## Entidade 4

Nome da entidade: Course

Descrição:

Representa um curso ou disciplina.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| name | VARCHAR(255) | Sim | Programação Web |
| description | TEXT | Não | Disciplina de desenvolvimento web |
| is_active | BOOLEAN | Sim | true |
| created_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Nome obrigatório.
* Nome não pode ser duplicado.

---

## Entidade 5

Nome da entidade: Material

Descrição:

Representa um material acadêmico enviado pelo professor.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| professor_id | UUID | Sim | uuid |
| title | VARCHAR(255) | Sim | Aula Django |
| file_name | VARCHAR(255) | Sim | aula01.pdf |
| file_path | TEXT | Sim | media/materials/aula01.pdf |
| extracted_text | TEXT | Sim | Conteúdo extraído |
| created_at | TIMESTAMP | Sim | 2026-06-22 |
| updated_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Professor deve existir.
* Arquivo deve possuir formato permitido.
* Título obrigatório.

---

## Entidade 6

Nome da entidade: ChatBot

Descrição:

Representa um chatbot criado por um professor.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| professor_id | UUID | Sim | uuid |
| name | VARCHAR(255) | Sim | ChatBot Django |
| description | TEXT | Não | Assistente da disciplina |
| is_active | BOOLEAN | Sim | true |
| created_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Professor deve existir.
* Nome obrigatório.

---

## Entidade 7

Nome da entidade: Conversation

Descrição:

Representa uma conversa iniciada por um aluno.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| student_id | UUID | Sim | uuid |
| chatbot_id | UUID | Sim | uuid |
| created_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Aluno deve existir.
* ChatBot deve existir.

---

## Entidade 8

Nome da entidade: Message

Descrição:

Representa uma mensagem dentro de uma conversa.

Atributos:

| Campo | Tipo | Obrigatório | Exemplo |
|---------|---------|---------|---------|
| id | UUID | Sim | uuid |
| conversation_id | UUID | Sim | uuid |
| sender_type | VARCHAR(20) | Sim | USER |
| content | TEXT | Sim | O que é Django? |
| created_at | TIMESTAMP | Sim | 2026-06-22 |

Regras de validação:

* Conteúdo obrigatório.
* Conversation deve existir.

---

# Relacionamentos

## Relação 1

User → Student

Tipo de relação: 1:1

Descrição:

Um usuário pode possuir um único registro de aluno.

---

## Relação 2

User → Professor

Tipo de relação: 1:1

Descrição:

Um usuário pode possuir um único registro de professor.

---

## Relação 3

Professor → Material

Tipo de relação: 1:N

Descrição:

Um professor pode possuir vários materiais.

---

## Relação 4

Professor → ChatBot

Tipo de relação: 1:N

Descrição:

Um professor pode criar vários chatbots.

---

## Relação 5

Course → Student

Tipo de relação: N:N

Descrição:

Um curso pode possuir vários alunos e um aluno pode participar de vários cursos.

Tabela intermediária:

course_students

---

## Relação 6

Course → Professor

Tipo de relação: N:N

Descrição:

Um curso pode possuir vários professores e um professor pode lecionar vários cursos.

Tabela intermediária:

course_professors

---

## Relação 7

Course → ChatBot

Tipo de relação: N:N

Descrição:

Um chatbot pode ser disponibilizado para vários cursos.

Tabela intermediária:

course_chatbots

---

## Relação 8

ChatBot → Material

Tipo de relação: N:N

Descrição:

Um chatbot pode utilizar vários materiais.

Tabela intermediária:

chatbot_materials

---

## Relação 9

Student → Conversation

Tipo de relação: 1:N

Descrição:

Um aluno pode iniciar várias conversas.

---

## Relação 10

Conversation → Message

Tipo de relação: 1:N

Descrição:

Uma conversa possui várias mensagens.

---

# Regras de Integridade

* Email deve ser único.
* Não permitir usuários duplicados.
* Não permitir materiais sem professor.
* Não permitir chatbot sem professor.
* Não permitir conversa sem aluno.
* Não permitir mensagem sem conversa.
* Não permitir referência a registros inexistentes.
* Não permitir associação duplicada em tabelas N:N.

---

# Índices e Performance

Índices necessários:

* index em email (User)
* index em role (User)
* index em professor_id (Material)
* index em professor_id (ChatBot)
* index em student_id (Conversation)
* index em chatbot_id (Conversation)
* index em conversation_id (Message)
* index em created_at (Conversation)
* index em created_at (Message)

---

# Estratégia de performance

* Paginação obrigatória.
* Índices em Foreign Keys.
* Consultas otimizadas com select_related().
* Consultas otimizadas com prefetch_related().
* Evitar N+1 queries.
* Utilização do pool de conexões do Neon.
* Cache preparado para futura integração com Redis.

---

# Migrations

## Estratégia de versionamento

ORM gerenciado (Django ORM)

---

## Ferramenta de migrations

Outro

Django Migrations

---

# Regras de Exclusão e Atualização

## Exclusão

* Soft delete para User.
* Soft delete para Material.
* Soft delete para ChatBot.
* Hard delete apenas para registros temporários.
* Não permitir exclusão de registros vinculados sem validação.

---

## Atualização

* Atualização parcial permitida.
* IDs nunca podem ser alterados.
* Emails devem continuar únicos.
* Atualização deve registrar updated_at.

---

# Segurança de Dados

* Senhas armazenadas apenas em hash.
* Dados sensíveis não podem ser registrados em logs.
* Conexão SSL obrigatória.
* UUID obrigatório em todas as entidades.
* Proteção contra SQL Injection através do ORM.

---

# Backup e Recuperação

Estratégia de backup:

* Point-In-Time Recovery (PITR) do Neon.
* Backup automático diário.
* Retenção mínima de 30 dias.

---

Recuperação:

* Restore completo do banco.
* Restore para ponto específico no tempo.
* Recuperação de tabelas via exportação.

---

# Restrições do Banco

* Utilizar exclusivamente PostgreSQL Neon.
* Não criar tabelas fora do modelo definido no PRD.
* Não duplicar entidades.
* Toda entidade deve possuir chave primária.
* Toda chave estrangeira deve possuir integridade referencial.

---

# CHECK FINAL

Antes de finalizar, verificar:

* [ ] Todas as entidades do PRD estão representadas
* [ ] Relacionamentos coerentes
* [ ] Tipos de dados definidos corretamente
* [ ] Regras de integridade claras
* [ ] Compatível com arquitetura definida