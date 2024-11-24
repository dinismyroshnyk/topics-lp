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

2. Configuração de um ambiente virtual:
Para linux ou mac, pode-se instalar o gestor de pacotes nix e usar o comando `nix-shell` a partir da raiz do projeto.
```bash
nix-shell
```
O ficheiro `shell.nix` já inclui:
- Criação do ambiente virtual
- Instalação do Django e dependências
- Aliases úteis para comandos comuns
No caso do windows.
```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
No caso do windows:
```bash
pip install django Pillow django-crispy-forms crispy-bootstrap5
```
No linux ou mac ao utilizar a nix-shell já as instala.

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
