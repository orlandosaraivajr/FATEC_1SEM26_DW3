import requests

with open('projetos.txt') as f:
     for linha in f:
        url = linha.split('|')[-1]
        try:
            url = url.replace(' ','')
            print(url)
            r = requests.get(url)
            if '.py' in r.text:
                print(f'Visitei {url}')
        except:
            print(f'Não encontrei projeto do  {linha.split('|')[-2]}')
            
        
        


try:    
    f = open('projetos2.txt')
    lines = f.readlines()
    print(lines)
    f.close()
except FileNotFoundError:
    print('Não consegui abrir o arquivo projetos2.txt')
    

