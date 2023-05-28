
#!/bin/bash
#
# Ejemplo de Menu en BASH
# Script SuperScant
# <6/03/2023 Alberto Jahir Chavero lara>
#
date
    echo "|"
    echo "|---------------------------|"
    echo "|   Menu Principal          |"
    echo "|---------------------------|"
    echo "|1. Net Discover"
    echo "|2. Portscan"
    echo "|3. Welcome"
    echo "|4. Exit"
    echo "|"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) /home/jqhir/Desktop/netdiscover.sh;;
        2) /home/jqhir/Desktop/portscan.sh;;
        3) /home/jqhir/Desktop/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac
