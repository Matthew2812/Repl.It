#include <stdio.h>
#define TAMANHO 5

//Busca Linear. E = Elemento; I = Indice; Vet = Vetor.
int buscaLinear (int e, int i, int vet[]){
  //Compara o Elemento com o número do Vetor
  if (e == vet[i]){
    //Se verdadeiro, retorna o indice
    return i;
  }
  //Se o indice percorrer o vetor inteiro e não encontrar o elemento, retorne -1
  else if (i == -1){
    return -1;
  }
  //Chamada recursiva da função
  else{
    return buscaLinear(e, i-1, vet);
  }
}

//Busca Binária. E = Elemento; Maior = Tamanho do vetor; Menor = Primeiro elemento do vetor; *Vet = Ponteiro do vetor.
int buscaBinaria (int e, int maior, int menor, int *vet){
  //Declara o meio do vetor
  int i = (maior + menor)/2;
  //Compara o Elemento com o Elemento do meio do vetor
  if (e == vet[i]){
    //Se for igual, retorna o Indíce
    return i;
  }
  //Compara se o meio do vetor é igual aos seus limites
  else if (i == menor || i == maior){
    //Se for igual, retorna -1 (O elemento não está no vetor)
    return -1;
  }
  //Compara se o Elemento é menor que o Elemento do meio do vetor
  if (e < vet[i]){
    //Se for, retorna a parte esquerda do vetor e compara
    return buscaBinaria(e, i, menor, vet);
  }
  //Retorna a parte direita do vetor
  else {
    return buscaBinaria(e, maior, i, vet);
  }
}

//Sequência de Fibonacci. N = N-ésimo número da sequência
int fibonacci(int n){
  //Se N for igual a 1
  if (n == 1){
    //retorna 0 (Primeira posição da Fibonacci)
    return 0;
  }
  //Se N for igual a 2
  else if (n == 2){
    //retorna 1 (Segunda posição da Fibonacci)
    return 1;
  }
  //Se N for maior que 2
  else{
    //Retorna o valor da posição da Fibonacci
    return fibonacci(n-1) + fibonacci(n-2);
  }
}

//Tentando criar um quicksort
void quicksort(int *vet, int tam){
  int pivo, novo[tam], k, aux;
  int maior = tam;
  int menor = 0;

  for (int i = 0; i < tam; i++){
    k = 0;
    pivo = vet[i];
    for (int j = 0; j < tam; i++){
  
      aux = vet[maior];
      vet[maior] = vet[menor];
      vet[menor] = aux;  
      }
  novo[k] = pivo;
  }
  printf("\nVetor: [ ");
  for (int i = 0; i < TAMANHO; i++)
    printf("%d ", vet[i]);
  printf("]");
} 

int main (){
  int valor, e, vet[TAMANHO], *p, n;

  for (int i = 0; i < TAMANHO; i++){
    printf("Digite um valor: ");   
    scanf("%d", &valor);
    vet[i] = valor;
  }
  p = vet;
  printf("\nVetor criado: [ ");
  for (int i = 0; i < TAMANHO; i++){
    printf("%d ", p[i]);
  }
  printf("]");
  
  printf("\nDigite um número para buscar no vetor: ");
  scanf("%d", &e);
  
  printf ("Busca Linear: %d", buscaLinear(e, TAMANHO-1, vet));
  printf ("\nBusca binária: %d", buscaBinaria(e, TAMANHO,  0, vet));
  
  printf ("\n\nDigite um número para Fibonacci: ");
  scanf("%d", &n);
  
  printf("\n%dº valor da Fibonacci: %d", n, fibonacci(n));
  return 0;
  
}