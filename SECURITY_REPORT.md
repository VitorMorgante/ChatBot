# Relatório de Segurança (Auditoria OWASP)

O sistema "ChatBot Institucional" foi desenvolvido com o framework Django, que nativamente oferece proteção contra as principais vulnerabilidades listadas no OWASP Top 10.

## 1. Proteção contra SQL Injection (A03:2021)
* **Implementação**: Toda a comunicação com o banco de dados PostgreSQL (Neon) é intermediada pelo ORM do Django.
* **Resultado**: Consultas parametrizadas por padrão, bloqueando injeções diretas.

## 2. Cross-Site Scripting (XSS) (A03:2021)
* **Implementação**: O sistema de templates do Django efetua escape automático de todos os dados variáveis inseridos nas views (HTML auto-escaping).
* **Resultado**: Prevenção ativa contra execução de scripts maliciosos no cliente.

## 3. Cross-Site Request Forgery (CSRF)
* **Implementação**: Todos os formulários (POST) implementam a tag `{% csrf_token %}` e o middleware `CsrfViewMiddleware` está ativado.
* **Resultado**: Requisições de origem cruzada não autenticadas são rejeitadas.

## 4. Controle de Acesso e Autenticação (A01:2021 / A07:2021)
* **Implementação**:
  * Utilização de UUID como Primary Key (evita enumeração de IDs - IDOR).
  * Decorators `@login_required` aplicados em todas as rotas restritas.
  * Validação explícita de *Role* (`if request.user.role != '...'`) antes de exibir ou processar a lógica.
  * Senhas hasheadas via PBKDF2 (padrão Django).
  * Controle de vinculação entre ChatBot e Aluno (RF13).

## 5. Validação de Uploads
* **Implementação**: O formulário `MaterialForm` valida os arquivos através de `request.FILES`.
* **Futuro (Produção)**: Recomenda-se varredura de antivírus em arquivos PDF/DOCX e verificação rígida de MIME type antes da extração RAG.

## 6. Sessões Seguras
* **Implementação**: Configuração de middlewares de sessão com proteção contra clickjacking (`XFrameOptionsMiddleware`).

## 7. Próximos Passos
* Ativar as flags `SESSION_COOKIE_SECURE` e `CSRF_COOKIE_SECURE` no deploy final.
* Habilitar `SECURE_SSL_REDIRECT` em produção.
