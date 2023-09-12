function mostrar1(){
    let a1 = 3
    let a2 = 4
    const total = a1 + a2
    return total
}

function mostrar2(a1, a2){
    const total = a1 + a2
    return total
}

function calcular(){
    if (mostrar1() == 7){
        console.log('É igual a 7')
    }else{
        console.log('Não é igual a 7')
    }
}

function calcular(){
    const ver = mostrar1()
    if (ver == 7){
        console.log('igual: '+ ver)
    }else{
        console.log('Você digitou ' + ver + 'não é número 7')
    }
}

function calcula (){
    let n1 = document.querySelector('valor1').value
    let n2 = document.querySelector('valor1').value
    const ver = mostrar1(n1, n2)
    console.log('igual: '+ ver)
}