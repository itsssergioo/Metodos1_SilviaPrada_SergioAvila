function help(){
	echo "---Debe incluir tres parametros: posición inicial, velocidad inicial y tiempo total---"
}

if ! [ $# -eq 3 ]; then
	help
	exit 1
	else
		echo "---Corriendo programa---"
fi 



