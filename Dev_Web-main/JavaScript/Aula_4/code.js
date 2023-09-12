function repetir(n){
    switch(n){
        case 1:
            alert('Página 1')
            document.location.href='pagina1.html'    
            break
            
        case 2:
            alert('Página 2')
            document.location.href='pagina2.html'
            break
            
        case 3:
            alert('Página 3') 
            break
            
        case 4:
            alert('Página 4') 
            break
        
        default:
            alert('Nenhuma página encontrada')
    }
}