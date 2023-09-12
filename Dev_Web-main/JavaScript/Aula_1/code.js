//TIPOS DE VARIÁVEIS

/*var a1 = null //global/funciona em qulquer lugar do programa - usado para testes/dados sem importância*/

function soma() {
  let a1 = Number(prompt('Digite o primeiro valor:'));
  let a2 = Number(prompt('Digite o segundo valor:')); //usado dentro da função - mais seguro
  const total = a1 + a2; //precisa de um valor - usado dentro da função

  return total
}

function subtrair() {
    let a1 = Number(prompt('Digite o primeiro valor:'))
    let a2 = Number(prompt('Digite o segundo valor:'))
    const total = a1 - a2

    return total
}

function mult(a1,a2) {
    const total = a1 * a2
    return total
}

function div(a1,a2) {
    const total = a1 / a2
    return total
}

function teste() {

    console.log('A soma é: ' + soma(12,4))
    console.log('A subtração é: ' + subtrair(12,4))
    console.log('A multiplicação é: ' + mult(12,4))
    console.log('A divisão é: ' + div(12,4))

    /*if(a == 1) {
        alert('A soma é: ' + soma())
    }else{
        alert('A subtração é: ' + subtrair())
    }*/
    
    /*console.log(total); //Imprime no terminal
    alert(total); //Imprime em uma caixa de alerta*/
}