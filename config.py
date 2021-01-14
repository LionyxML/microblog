''' Arquivo criado para evitar configurações no mesmo arquivo utilizado para criar
    a aplicação.
    Poderia ser deixado no microblog.py as variáveis globais, na forma:
    app.config['SECRET_KEY'] ='my-secret-key'

    Utilizando o conceito separation of concerns, utilizo uma forma mais elaborada
    e extensíve, criando uma classe para armazenar as variáveis de configuração.
    Isso mantém as coisas organizadas.

    Não esquecer de importar no __init__.py

'''

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'

