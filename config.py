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

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es', 'pt']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    POSTS_PER_PAGE = 25
