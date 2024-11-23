{ pkgs ? import <nixpkgs> {} }:

let
    pythonEnv = pkgs.python3.withPackages (ps: with ps; [ pip ]);
in
pkgs.mkShell {
    buildInputs = [
        pythonEnv
        pkgs.tree
    ];

    shellHook = ''
        export PYTHONPATH=$PYTHONPATH:$(pwd)

        python3 -m venv .venv
        source .venv/bin/activate

        pip install django Pillow django-crispy-forms crispy-bootstrap5

        alias cls='clear'
        alias validate='django-admin --version'
        alias new-project='django-admin startproject '
        alias startapp='python manage.py startapp '
        alias makemigrations='python manage.py makemigrations '
        alias sqlmigrate='python manage.py sqlmigrate topics 0001'
        alias migrate='python manage.py migrate'
        alias updatedb='makemigrations; sqlmigrate; migrate'
        alias createsuperuser='python manage.py createsuperuser'
        alias runserver='python manage.py runserver'
        alias run='echo "Nothing to run :("'
    '';
}