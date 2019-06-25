//Importando bibliotecas

//Testando variáveis e print
var a = 3;
var b = 5;

console.log("A + B: " + (a + b));

//Testando laços

//Let mata a variável no for
for(let i = 0; i < 10; i++){
  console.log("Valor de i: " + i);
}

console.log();

var j = 0;
while(j < 10){
  console.log("Valor de j: " + j);
  j++;
}

//Criando funções
function soma(a, b){
  return a + b;
}

soma(a, b);

//Criando vetor e trabalhando com ele
var vetor = [];

for (let i = 10; i > 0; i--){
  vetor.push(i);
}