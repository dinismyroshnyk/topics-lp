# Topics - Aplicação de Fórum em Django

Esta é uma aplicação web desenvolvida em Django que permite a gestão de tópicos de discussão, similar a um fórum. Os usuários podem criar tópicos, adicionar comentários e interagir com o conteúdo.

## Funcionalidades

- Criação, visualização, edição e exclusão de tópicos
- Sistema de comentários em tópicos
- Autenticação de usuários
- Interface responsiva e amigável
- Formulários aprimorados com django-crispy-forms

## Requisitos

- Python 3.8+
- Django 4.0+
- django-crispy-forms
- Virtualenv (recomendado)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/dinismyroshnyk/topics-lp
cd topics
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superutilizador:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Estrutura do Projeto

```
topics/
├── manage.py
├── requirements.txt
├── topics/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── forum/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── admin.py
    └── tests.py
```

## Executando os Testes

Para executar os testes unitários:

```bash
python manage.py test
```

## Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nome-da-feature`)
5. Abra um Pull Request
