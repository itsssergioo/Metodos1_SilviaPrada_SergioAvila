pass=0
function checkvalue (){
if [ $1 -eq 1  ] || [ $2 -eq 0 ]
then 
	pass=1
else
	echo "---Intente de nuevo---" 
fi
};
while [ $pass -eq 0 ]
do
	echo "Inserte un parámetro para leer: ";
	read;
	checkvalue $REPLY
done 
echo "pass =" $pass
echo "---Programa terminado---" 




