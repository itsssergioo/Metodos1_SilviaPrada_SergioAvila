x=$(pwd)
y="/data"
z="$x$y"
if [ $x -eq $z ]
then
        exit 1
else
        mkdir $z
fi

