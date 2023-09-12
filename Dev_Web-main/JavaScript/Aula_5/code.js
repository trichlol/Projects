function teste() {
    var dados = [
        {id: 1, login: 'Pedro', senha: 123},
        {id: 2, login: 'Henrique', senha: 456},
        {id: 3, login: 'João', senha: 789}
    ]

    return dados

    /*
    console.log('ID |  LOGIN   | SENHA')
    console.log('---+----------+-------')
    console.log(dados[0].id + '  | ' + dados[0].login + '    | ' + dados[0].senha)
    console.log(dados[1].id + '  | ' + dados[1].login + ' | ' + dados[1].senha)
    console.log(dados[2].id + '  | ' + dados[2].login + '     | ' + dados[2].senha)

    alert('ID |  LOGIN   | SENHA\n---+----------+-------\n' + dados[0].id + '  | ' + dados[0].login + '    | ' + dados[0].senha + '\n' + dados[1].id + '  | ' + dados[1].login + ' | ' + dados[1].senha + '\n' + dados[2].id + '  | ' + dados[2].login + '     | ' + dados[2].senha)
    */
}

function logon(user, password) {

    const conj = teste()

    if(user == conj[0].login && password == conj[0].senha) {
        window.alert('Você está logado')
    } else {
        window.alert('ERRO!')
    }
}

function logar() {
    
    let user = prompt('Qual o seu usuário?')
    let pass = prompt('Qual a sua senha?')

    logon(user, pass)
}