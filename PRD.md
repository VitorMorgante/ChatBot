# PRD.md (Product Requirements Document)

---

# Escopo do Sistema

## Funcionalidades Principais

O sistema deverá permitir:

* Cadastro de professores
* Cadastro de alunos
* Login e logout de usuários
* Gerenciamento de cursos
* Associação de professores aos cursos
* Associação de alunos aos cursos
* Upload de materiais didáticos
* Extração automática de conteúdo dos materiais
* Criação de chatbots especializados
* Associação de materiais aos chatbots
* Consulta inteligente via IA
* Histórico de conversas
* Controle de permissões por curso
* Gerenciamento de usuários
* Gerenciamento de materiais
* Gerenciamento de chatbots
* Painel administrativo
* Auditoria básica de acesso

---

## Funcionalidades Fora do Escopo

Liste o que o sistema NÃO deve fazer:

* Processamento de pagamentos
* Marketplace de cursos
* Aplicativo mobile nativo
* Integração com ERP acadêmico
* Integração com sistemas financeiros
* Videoconferência
* Correção automática de provas
* Emissão de certificados

---

# Regras de Negócio

* Apenas professores podem cadastrar materiais.
* Apenas professores podem criar chatbots.
* Apenas professores podem associar materiais aos chatbots.
* Apenas alunos matriculados em um curso podem acessar os chatbots vinculados ao curso.
* Um chatbot deve possuir pelo menos um material associado.
* Materiais removidos não podem ser utilizados para geração de respostas.
* Todo usuário deve possuir email único.
* Todo chatbot deve possuir um professor responsável.
* O sistema deve registrar todas as interações realizadas pelos alunos.
* Usuários inativos não podem acessar o sistema.

---

# Requisitos Funcionais

## RF01 - Cadastro de Professor

Descrição:
O sistema deve permitir o cadastro de novos professores.

Ator:
Administrador

Pré-condições:

* Administrador autenticado.

Fluxo principal:

1. Administrador acessa cadastro de professor.
2. Informa nome, email e senha.
3. Sistema valida os dados.
4. Sistema salva o professor.
5. Sistema retorna confirmação.

Fluxos alternativos:

- Email já cadastrado → sistema exibe erro.
- Dados inválidos → sistema exibe erro.

Pós-condições:

* Professor criado no sistema.

---

## RF02 - Cadastro de Aluno

Descrição:
O sistema deve permitir o cadastro de alunos.

Ator:
Administrador

Pré-condições:

* Administrador autenticado.

Fluxo principal:

1. Administrador acessa cadastro de aluno.
2. Informa dados do aluno.
3. Sistema valida informações.
4. Sistema salva registro.
5. Sistema confirma cadastro.

Fluxos alternativos:

- Email duplicado.
- Dados inválidos.

Pós-condições:

* Aluno cadastrado.

---

## RF03 - Autenticação

Descrição:
Permitir autenticação de usuários.

Ator:
Professor ou Aluno

Pré-condições:

* Usuário cadastrado.

Fluxo principal:

1. Usuário acessa tela de login.
2. Informa email.
3. Informa senha.
4. Sistema valida credenciais.
5. Sistema inicia sessão.

Fluxos alternativos:

- Senha incorreta.
- Usuário inexistente.
- Usuário inativo.

Pós-condições:

* Sessão autenticada.

---

## RF04 - Cadastro de Curso

Descrição:
Permitir criação de cursos.

Ator:
Administrador

Pré-condições:

* Administrador autenticado.

Fluxo principal:

1. Administrador acessa cadastro.
2. Informa nome e descrição.
3. Sistema valida dados.
4. Sistema salva curso.

Fluxos alternativos:

- Nome duplicado.

Pós-condições:

* Curso criado.

---

## RF05 - Vinculação de Professor ao Curso

Descrição:
Permitir associar professores a cursos.

Ator:
Administrador

Pré-condições:

* Professor cadastrado.
* Curso cadastrado.

Fluxo principal:

1. Seleciona professor.
2. Seleciona curso.
3. Confirma associação.
4. Sistema registra vínculo.

Fluxos alternativos:

- Professor inexistente.
- Curso inexistente.

Pós-condições:

* Professor associado ao curso.

---

## RF06 - Vinculação de Aluno ao Curso

Descrição:
Permitir matrícula de alunos em cursos.

Ator:
Administrador

Pré-condições:

* Aluno cadastrado.
* Curso cadastrado.

Fluxo principal:

1. Seleciona aluno.
2. Seleciona curso.
3. Confirma matrícula.
4. Sistema salva vínculo.

Fluxos alternativos:

- Aluno inexistente.
- Curso inexistente.

Pós-condições:

* Matrícula registrada.

---

## RF07 - Upload de Material

Descrição:
Permitir upload de materiais acadêmicos.

Ator:
Professor

Pré-condições:

* Professor autenticado.

Fluxo principal:

1. Professor acessa área de materiais.
2. Seleciona arquivo.
3. Informa título.
4. Sistema realiza upload.
5. Sistema extrai conteúdo.
6. Sistema salva material.

Fluxos alternativos:

- Arquivo inválido.
- Arquivo corrompido.
- Tamanho excedido.

Pós-condições:

* Material disponível.

---

## RF08 - Gerenciamento de Materiais

Descrição:
Permitir editar e excluir materiais.

Ator:
Professor

Pré-condições:

* Professor proprietário do material.

Fluxo principal:

1. Seleciona material.
2. Escolhe ação.
3. Sistema executa alteração.

Fluxos alternativos:

- Material inexistente.

Pós-condições:

* Material atualizado.

---

## RF09 - Criação de ChatBot

Descrição:
Permitir criação de chatbots.

Ator:
Professor

Pré-condições:

* Professor autenticado.

Fluxo principal:

1. Professor acessa módulo.
2. Informa nome.
3. Informa descrição.
4. Sistema cria chatbot.

Fluxos alternativos:

- Dados inválidos.

Pós-condições:

* Chatbot criado.

---

## RF10 - Associação de Materiais ao ChatBot

Descrição:
Permitir associação de materiais.

Ator:
Professor

Pré-condições:

* Chatbot existente.
* Material existente.

Fluxo principal:

1. Seleciona chatbot.
2. Seleciona materiais.
3. Confirma associação.
4. Sistema salva vínculo.

Fluxos alternativos:

- Material inexistente.

Pós-condições:

* Base de conhecimento criada.

---

## RF11 - Consulta Inteligente

Descrição:
Permitir perguntas em linguagem natural.

Ator:
Aluno

Pré-condições:

* Aluno matriculado.
* Chatbot disponível.

Fluxo principal:

1. Aluno acessa chatbot.
2. Digita pergunta.
3. Sistema busca contexto.
4. Sistema envia contexto à IA.
5. IA gera resposta.
6. Sistema apresenta resposta.

Fluxos alternativos:

- Sem contexto encontrado.
- Falha da IA.
- Falha de conexão.

Pós-condições:

* Resposta apresentada.

---

## RF12 - Histórico de Conversas

Descrição:
Registrar todas as interações.

Ator:
Sistema

Fluxo principal:

1. Receber pergunta.
2. Receber resposta.
3. Salvar histórico.

Pós-condições:

* Conversa registrada.

---

## RF13 - Controle de Permissões

Descrição:
Garantir isolamento dos cursos.

Ator:
Sistema

Fluxo principal:

1. Usuário solicita acesso.
2. Sistema verifica matrícula.
3. Sistema libera ou bloqueia acesso.

Fluxos alternativos:

- Usuário sem permissão.

Pós-condições:

* Segurança garantida.

---

# Requisitos Não Funcionais

## RNF01 - Performance

Descrição:
O sistema deve responder rapidamente.

Métrica:

- Tempo máximo de resposta: 2 segundos

Condição de carga:

- Até 1.000 usuários simultâneos

Critério de aceitação:

- 95% das requisições abaixo de 2 segundos

---

## RNF02 - Segurança

Descrição:

* Senhas criptografadas.
* HTTPS obrigatório.
* Proteção CSRF.
* Proteção XSS.
* Proteção SQL Injection.
* Controle de permissões.

---

## RNF03 - Usabilidade

Descrição:

* Interface responsiva.
* Navegação intuitiva.
* Compatível com desktop e dispositivos móveis.

---

## RNF04 - Escalabilidade

Descrição:

* Suportar crescimento progressivo de usuários.
* Suportar aumento de materiais acadêmicos.

---

## RNF05 - Confiabilidade

Descrição:

* Disponibilidade mínima de 99,9%.
* Backup automático diário.

---

## RNF06 - Manutenibilidade

Descrição:

* Código modular.
* Cobertura mínima de testes de 80%.

---

## RNF07 - Compatibilidade

Descrição:

* Compatível com Chrome.
* Compatível com Firefox.
* Compatível com Edge.
* Compatível com PostgreSQL Neon.

---

# Casos de Uso

## UC01 - Realizar Login

Ator:
Professor ou Aluno

Fluxo principal:

1. Informa email.
2. Informa senha.
3. Sistema autentica.

---

## UC02 - Criar ChatBot

Ator:
Professor

Fluxo principal:

1. Cria chatbot.
2. Configura chatbot.
3. Salva chatbot.

---

## UC03 - Enviar Material

Ator:
Professor

Fluxo principal:

1. Seleciona arquivo.
2. Realiza upload.
3. Sistema processa arquivo.

---

## UC04 - Consultar ChatBot

Ator:
Aluno

Fluxo principal:

1. Seleciona chatbot.
2. Realiza pergunta.
3. Recebe resposta.

---

# Dados do Sistema (Visão Geral)

Entidades principais

* User
* Professor
* Student
* Course
* Material
* ChatBot
* Conversation
* Message

---

# Critérios de Aceitação

Para considerar o sistema correto, ele deve:

* Permitir autenticação de usuários.
* Permitir cadastro de cursos.
* Permitir upload de materiais.
* Permitir criação de chatbots.
* Permitir consulta por IA.
* Impedir acesso indevido.
* Registrar histórico de conversas.
* Executar todos os testes com sucesso.

---

# Restrições do Projeto

* Utilizar Django.
* Utilizar PostgreSQL Neon.
* Utilizar Bootstrap.
* Não utilizar serviços pagos obrigatórios.
* Manter arquitetura MVC.

---

# Premissas

* Usuários possuem acesso à internet.
* Servidor Neon estará disponível.
* Professores fornecerão materiais adequados.
* Os modelos de IA estarão disponíveis para consulta.

---

# CHECK FINAL (para o estudante)

Antes de finalizar, revise:

* [ X ] Requisitos funcionais completos
* [ X ] Regras de negócio claras
* [ X ] Casos de uso definidos
* [ X ] Escopo bem delimitado