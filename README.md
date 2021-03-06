# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:nmoura/wttd-eventex.git
cd wttd-eventex
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku create <NOME_DA_INSTANCIA>
heroku config:push
heroku config:set SECRET_KEY=$(python contrib/secret_gen.py)
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```