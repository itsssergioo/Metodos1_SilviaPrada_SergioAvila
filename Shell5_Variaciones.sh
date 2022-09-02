function variaciones(n, r){
if r > n
then
        echo "factoriales de numeros negativos no existen"
else
fact = 1
x = 1
while x<=n:
fact = x*fact
x = x+1

numerador = fact         
dn = n - r              
fact = 1
x = 1
while x<=dn:
fact = x*fact
x = x+1
denominador = fact       
var = numerador/denominador

echo"las variaciones de", n, "elementos tomados de", r, "en", r, "son", var)
}
variaciones(6, 3)
