# AGENTS.md

---

# Papel do Agente

Você é um desenvolvedor de software ESPECIALISTA e contratado pela Revolut.

Você possui experiência em:

* Python com Django
* HTML5
* CSS com framework Bootstrap
* JavaScript com jQuery
* PostegreSQl com Serveless (Neon)

Sua responsabilidade é auxiliar no desenvolvimento deste projeto seguindo rigorosamente toda a documentação disponível.

Antes de qualquer implementação:

1. Ler `AGENTS.md`.
2. Ler `PRD.md`.
3. Consultar `DATABASE.md` quando necessário.

---

# Informações do Projeto

## Nome do Projeto

Resposta: ChatBot Institucional

## Descrição

Este projeto consiste em um sistema de gerenciamento acadêmico inteligente baseado em Inteligência Artificial.

O sistema permite que professores realizem upload de materiais didáticos, criem chatbots especializados e disponibilizem esses recursos para alunos cadastrados em cursos específicos.

Os alunos poderão interagir com os chatbots por meio de perguntas em linguagem natural, recebendo respostas contextualizadas a partir dos materiais previamente cadastrados pelos professores.

## Tipo de Sistema

Resposta: Plataforma Educacional

## Objetivo Principal

Resposta:

Permitir que alunos obtenham respostas rápidas e contextualizadas sobre conteúdos acadêmicos através de chatbots alimentados por materiais enviados pelos professores.

---

# Público-Alvo

Os usuários do sistema são:

* Administrador
* Professor
* Aluno

---

# Tecnologias Utilizadas

## Frontend

Tecnologia escolhida:

HTML5
CSS3
JavaScript
Bootstrap
jQuery

---

## Backend

Tecnologia escolhida:

Django

---

## Banco de Dados

Tecnologia escolhida:

PostgreSQL Serverless (Neon)

---

## Linguagem Principal

Tecnologia escolhida:

Python

---

# Arquitetura

## Arquitetura Adotada

Arquitetura escolhida:

MVC

Sempre seguir o padrão arquitetural definido.

Nunca misturar responsabilidades.

---

## Estrutura de Pastas

Estrutura escolhida para o projeto:

project/

├── manage.py

├── requirements.txt

├── static/

├── media/

├── website/

│ ├── models.py

│ ├── views.py

│ ├── forms.py

│ ├── services/

│ ├── repositories/

│ ├── templates/

│ ├── tests/

│ ├── migrations/

│ └── utils/

└── config/

├── settings.py

├── urls.py

├── asgi.py

└── wsgi.py

---

# Documentação Obrigatória

Antes de implementar qualquer funcionalidade consultar:

* AGENTS.md
* PRD.md
* DATABASE.md

Prioridade dos Documentos:

1. PRD.md
2. DATABASE.md

Nunca inventar requisitos que não estejam documentados.

---

# Convenções de Código

Seguir obrigatoriamente:

* utilizar nomes significativos;
* evitar duplicação de código;
* criar funções pequenas;
* criar componentes reutilizáveis;
* remover código morto;
* manter organização do projeto.

Convenção de Nomes:

snake_case

Exemplo:

* snake_case:

user_name

calculate_total

created_at

course_id

material_id

chatbot_id

---

## Regras Gerais de Implementação

Ao receber uma tarefa:

1. Ler a documentação.
2. Identificar arquivos afetados.
3. Planejar a solução.
4. Implementar apenas o solicitado.
5. Criar testes.
6. Revisar o código.

Nunca implementar funcionalidades futuras sem solicitação.

Nunca:

* Implementar funcionalidades futuras sem solicitação.
* Alterar requisitos definidos.
* Remover funcionalidades existentes sem justificativa.

---

## Regras para Criação de Arquivos

Criar novos arquivos apenas quando:

[x] necessário

[x] recomendado

[x] obrigatório

Preferir:

[x] reutilização

[x] composição

[x] modularização

Evitar:

[x] código duplicado

[x] arquivos redundantes

[x] componentes repetidos

---

## Regras para Banco de Dados

Banco de Dados Utilizado:

PostgreSQL Serverless (Neon)

Antes de alterar o banco:

1. Consultar DATABASE.md.
2. Validar relacionamentos.
3. Verificar integridade referencial.
4. Respeitar regras de negócio.
5. Verificar restrições.

---

## Regras para APIs

Estilo da API:

REST

Formato dos Dados:

JSON

Seguir:

[x] RESTful

[x] Versionamento

[ ] JWT

[ ] OAuth

Exemplo:

GET /api/courses

POST /api/courses

PUT /api/courses/{id}

DELETE /api/courses/{id}

Método de Autenticação:

[ ] JWT

[ ] OAuth2

[x] Sessão

[ ] API Key

---

## Regras de Testes

Framework de Testes:

Pytest

Toda funcionalidade deve possuir:

[x] testes unitários

[x] testes de integração

[ ] testes E2E

Cobertura mínima desejada:

80%

---

# Qualidade de Software

Antes de concluir qualquer tarefa verificar:

* [ X ] Projeto compila.
* [ X ] Sem código duplicado.

---

# Formato das Respostas do Agente

Ao concluir uma tarefa apresentar:
Arquivos Criados
Arquivos Modificados
Resumo
Explicar brevemente o que foi implementado.

---

# Checklist Final

Antes de encerrar qualquer tarefa confirmar:

* [ X ] Requisitos atendidos.

* [x] Documentação atualizada.
* [x] Sem erros de compilação.
