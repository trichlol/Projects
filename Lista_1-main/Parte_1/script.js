/*1) Faça um programa que compare o valor de entrada digitado pelo usuário nas seguintes condições: se
for menor que 18 deverá imprimir a mensagem: “Você é adolescente” e aparecer a idade digitada,
concatenando o valor; se for maior que 18 e menor igual a 65 deverá imprimir: “Você é jovem”, e se for
acima de 65 anos deverá imprimir você é idoso. (Deverá utilizar if..else if..else)*/

function idade() {
    let x = document.querySelector('#classeIdade').value

    if (x < 18) {
        alert('Você é adolescente')
    }
    else if (x >= 18 && x <= 65) {
        alert('Você é jovem')
    }
    else {
        alert('Você é idoso')
    }
}

/*2) Com laço “For” você deverá fazer a seguinte condição: quando o contador chegar ao número digitado
pelo usuário deverá imprimir uma mensagem: “Você tem essa idade: “ + idade (deve concatenar). Caso não
chegar a essa idade deverá imprimir: “Dados não encontrado!”*/

function contador1() {
    let y = document.querySelector('#forIdade').value

    if (y < 0){
        alert('Dados não encontrados')
    }

    for (let i=0; i<=y; i++) {
        if (i == y){
            alert('Você tem essa idade: ' + i)
        }
    }
}

/*3) Utilizando o laço “While” utilize a mesma lógica com do laço “For”.*/

function contador2() {
    let idade = document.querySelector('#whileIdade').value

    if (idade < 0){
        alert('dados nao encontrados')
    }

    let cont = 0

    while (idade >= cont) {
        if (cont == idade) {
            alert('Você tem essa idade: ' + cont)
        }
        cont++
    }
}

/*4) Explique a diferença entre o laço “do...while” e o laço “while”.*/

/*O "while" e o "do ... while" são duas estruturas de loop em JavaScript que permitem que você execute
repetidamente um bloco de código enquanto uma determinada condição for verdadeira. A principal
diferença entre as duas estruturas é que a instrução "do ... while" executa o bloco de código pelo
menos uma vez, mesmo que a condição não seja verdadeira, enquanto a instrução "while" verifica a
condição primeiro antes de executar o bloco de código.*/

/*5) Com laço “Switch case” faça a seguinte lógica: Com a entrada de dados do usuário caso for 1, deve
imprimir: “Gosto de anime Naruto”, caso 2: “One Punch é muito bom”, caso 3: “A série Supernatural é
muito boa”, caso 4: “Vikings com Ragnar era o melhor”, caso nenhuma das opções: você assiste algo que
não está na lista.*/

function caso() {
    let n = Number(document.querySelector('#serie').value)

    switch(n) {
        case 1:
            alert('Gosto de anime Naruto')
            break
        case 2:
            alert('One Punch é muito bom')
            break
        case 3:
            alert('A série Supernatural é muito boa')
            break
        case 4:
            alert('Vikings com Ragnar era o melhor')
            break
        default:
            alert('Você assiste algo que não está na lista')
    }
}