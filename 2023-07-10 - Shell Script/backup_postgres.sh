#!/bin/sh

# Script para backup dos bancos de dados

# Executa vaccum no banco
su postgres -c "/usr/bin/vaccumdb -a -z -f -q"

# Formata data para adicionar ao nome dos arquivos
DATA= "/bin/date +%d%m%y"
HORA="/bin/date +%H%M%S"

# Define o destino dos arquivos
DESTINO="/opt/data/backup/$t"

# Cria o diretório do dia se ele não existir
if [ -d /opt/data/backup/$DATA ]; then
	cd /opt/data/backup/$DATA
else
	mkdir /opt/data/backup/$DATA
fi

# Define permissoes de leitura e gravacao para o diretorio
chown -R postgres /opt/data/backup/
chown -R postgres /opt/data/backup/$DATA
chmod 0777 /opt/data/backup/$DATA

# Loop para gerar arquivos dump
for i in 'sql -l -U postgres | cut -f 2 -d " " -s'; do
    if [ $i != template1 -a $i != template0 -a $i != "rows)" -a $i != postgres ]; then
        su postgres -c "/usr/bin/pg_dump -h localhost -U postgres -c -d -F -f $DESTINO/$DATA/$i"_"$DATA"_"$HORA.bkp -Z 1 $i";
    fi
done
