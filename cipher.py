# Cifra de Cesar 

def cripta(chave, texto):
    '''Função para criptografar o texto'''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    texto = texto.lower()
    newTexto = ''    

    for i in texto:
        if i in alp:      
            pos = alp.find(i)
            newPos = pos + chave 
            if newPos > 25:
                newPos = newPos - 26

            newTexto = newTexto + alp[newPos]
            
        else: 
            newTexto = newTexto + i

    return newTexto    
    



def decripta(chave, texto):
    '''Função para decriptografar o texto'''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    texto = texto.lower()
    newTexto = ''    

    for i in texto:
        if i in alp:      
            pos = alp.find(i)
            newPos = pos - chave 
            if newPos > 25:
                newPos = newPos - 26

            newTexto = newTexto + alp[newPos]
            
        else: 
            newTexto = newTexto + i

    return newTexto 
    
         
print(decripta(11, 't zywj mpwtpgp ty deletdetnd esle t oznezcpo xjdpwq. htydezy d. nsfcnstww?'))