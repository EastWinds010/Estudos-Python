# Lista básica de exercícios em Python

A resolução destes exercícios tem como objetivo iniciar os estudos na lingaguem Python, iniciando desde de seus exercícios mais simples fornecidos pela própria wiki do Python.

Esta lista de exercícios pode ser consultada em:
https://wiki.python.org.br/EstruturaSequencial
iawngnfaglkjn
let nome = window.prompt("digite seu nome Atleta");
let maior = -999999;
let menor = 10000000;
let media = 0;
let nota, nota2, nota3, nota4, nota5, nota6, nota7 = 0;0;0;0;0;0;0;   
let soma = 0;
let somap = 0
for(let i= 0; i<7; i++){
    nota = Number(window.prompt("digite as notas dada ao atlela"));
    if (nota>maior){
        maior=nota
    }
    if(nota<menor){
        menor=nota
    }
    somap = maior + menor;
    soma += nota;
    media = -(somap - soma) /5;
    
    switch(i){
    case 0:
    nota7 = nota;
    break;
    case 1:
    nota6 = nota;
    break;
    case 2:
    nota5 = nota;
    break;
    case 3:
    nota4 = nota;
    break;
    case 4:
    nota3 = nota;
    break;
    case 5:
    nota2 = nota;
    break;
    case 6:
    nota = nota;
    break;
    }
    console.log(`${nota}`);
    console.log(`${nota2}`);
    console.log(`${nota3}`);
    console.log(`${nota4}`);
    console.log(`${nota5}`);
    console.log(`${nota6}`);
    console.log(`${nota7}`);
}

console.log("Resultado Final");
console.log(`Atleta: ${nome}`);
console.log(`Melhor nota: ${maior}`);
console.log(`Pior nota: ${menor}`);
console.log(`Media: ${media}`);
