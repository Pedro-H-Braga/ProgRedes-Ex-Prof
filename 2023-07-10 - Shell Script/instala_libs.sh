#!/bin/bash
#
# Instalacao de Bibliotecas basicas no linux
#

MODULOS="psycopg2 requests"
VIRTUAL_ENV="ambiente_teste"

# --------------------------------------------------
echo "Instalando VIRTUALENV..."

sudo pip install virtualenv --user


# --------------------------------------------------
echo "Criando o Ambiente Virtual..."

virtualenv $VIRTUAL_ENV

#python -m venv $VIRTUAL_ENV

# --------------------------------------------------
echo "#Ativando o ambiente virtual..."

# Linux/MacOS
source $VIRTUAL_ENV/bin/activate

# Windows (Powershell)
#$VIRTUAL_ENV\Scripts\activate.ps1

# Windows (cmd)
#$VIRTUAL_ENV\Scripts\activate.bat

# --------------------------------------------------
echo "Instalando Bibliotecas..."

sudo -H pip3 install --upgrade pip

for modulo in $MODULOS
   do
      sudo -H pip3 install $modulo --user
   done