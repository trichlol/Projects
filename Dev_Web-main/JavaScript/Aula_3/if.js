function mostrar() {
    let a1 = 2
    let a2 = 10
    const total = a1 + a2
    console.log(total)
    return total
}

const mostra = mostrar()

if (mostra < 9) {
    console.log('Você ainda é uma criança de ' + mostra + ' de idade')
}else if (mostra > 8 && mostra < 65){
    console.log('Você é jovem de acordo com a ONU')
}else if (mostra > 66 && mostra < 90) {
    console.log('Você é idoso')
}else{
    console.log('Você é ancião')
}