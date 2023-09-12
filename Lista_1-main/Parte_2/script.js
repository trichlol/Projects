function java() {
    alert('Olá, JavaScript')
}

function soma() {
    let a = Number(document.querySelector('#num1').value)
    let b = Number(document.querySelector('#num2').value)

    const total = a+b
    alert('A soma é: ' + total)
}

function sub() {
    let a = Number(document.querySelector('#num1').value)
    let b = Number(document.querySelector('#num2').value)

    const total = a-b
    alert('A subtração é: ' + total)
}

function mult() {
    let a = Number(document.querySelector('#num1').value)
    let b = Number(document.querySelector('#num2').value)

    const total = a*b
    alert('A multiplicação é: ' + total)
}

function div() {
    let a = Number(document.querySelector('#num1').value)
    let b = Number(document.querySelector('#num2').value)

    const total = a/b
    alert('A divisão é: ' + total)
}