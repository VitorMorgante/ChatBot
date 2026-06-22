# Guia de Deploy - ChatBot Institucional

Este documento descreve os passos necessários para a implantação em ambiente de produção (ex: Heroku, Render, AWS, Railway).

## Pré-requisitos
* Servidor PostgreSQL Serverless (Neon).
* Conta na plataforma de hospedagem.
* Chave de API da LLM (OpenAI, Gemini, etc).

## 1. Variáveis de Ambiente (Configurar na Plataforma)
Definir as seguintes variáveis na nuvem:
* `DATABASE_URL`: String de conexão do PostgreSQL Neon (começando com `postgres://`).
* `SECRET_KEY`: Chave secreta longa e aleatória (nunca usar a de dev).
* `DEBUG`: `False`.

## 2. Servidor WSGI
O projeto já foi configurado para utilizar o **Gunicorn**.
Comando de inicialização sugerido (Procfile):
```
web: gunicorn project.wsgi --log-file -
```

## 3. Arquivos Estáticos (Whitenoise)
O `Whitenoise` foi adicionado aos middlewares para servir arquivos estáticos diretamente pelo Gunicorn.
É importante rodar o comando:
```bash
python manage.py collectstatic --noinput
```
Isso coletará os arquivos estáticos para a pasta `staticfiles`.

## 4. Health Check e Logs
* **Logs**: O Django está configurado (`settings.py`) para redirecionar logs de nível `INFO` ou superior para a saída padrão (`console`), ideal para plataformas modernas em nuvem.
* **Health Check**: Qualquer rota (como `/`) pode ser usada como check se retornar `200 OK`. Para testes mais aprofundados, pode-se usar o endpoint de login ou criar um endpoint `/health/` específico.

## 5. Passos para a Primeira Implantação
1. Enviar código para o repositório remoto conectado à plataforma.
2. Definir as variáveis de ambiente.
3. Garantir que as *migrations* sejam executadas (exemplo no comando release do Heroku: `python manage.py migrate`).
4. Criar o primeiro usuário ADMIN.
