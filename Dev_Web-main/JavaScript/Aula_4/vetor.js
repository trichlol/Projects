function array(){

    let loguser = 'Alinny'
    let logsenha = 789

    let login = ['Pedro','Alinny','André']
    let senha = [123,789,274]

    for(let i=0; login.length > i; i++){
        for(let j=0; senha.length > j; j++){
            
        }
        if(login[i] == loguser && senha[i] == logsenha){
            alert('Usuário encontrado')
            break
        }
        else{
            alert('Não há esse usuário')
        }        
    }
}