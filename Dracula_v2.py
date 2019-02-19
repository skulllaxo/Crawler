import requests
import csv
from bs4 import BeautifulSoup
import re

mat = open('Materias.csv', 'w')
arq = open('Soup.csv', 'r').readlines()
n = 1

# url = f'https://www.sitequevocequer.com.br/blog/page/{n}/'
# res = requests.get('https://www.sitequevocequer.com.br/blog/')
# res = requests.get(url)
# soup =BeautifulSoup(res.text,'lxml')

# hi = soup.select('title')
#
# x= soup.find_all('a')


# limite=13


# end = list()
# end2 = list()

# while n<=limite:
#     url = f'https://www.sitequevocequer.com.br/blog/page/{n}/'
#     # res = requests.get('https://www.sitequevocequer.com.br/blog/')
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'lxml')

# for link in soup.find_all('a'):   #pega os links da pagina
#     end.append(link.get('href'))

# for link in end:
#     if link not in end2:
#         end2.append(link)
# print(f'pagina {n} sendo sugada!!!')
# print(f'A lista de link tem {len(end2)} valores')
# n+=1

# for v in end2:
#     arq.write('\n'+v)


x = 1

limite = 526
limit = 1
end = list()
end2 = list()

while x <= limite:

    url = arq[x]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    for link in soup.find_all('a'):  # pega os links da pagina
        end.append(link.get('href'))
    for link in end:
        if link not in end2:
            # if 'bit.ly' in link:
            # if re.search(str("bit.ly"),str(link)):
            if str('bit.ly') in str(link):
                end2.append(link)
        else:
            pass

    print(f'endereço{x}\n Esta sendo sugado\nA lista de link tem {len(end2)} valores!!!!')
    for v in end2:

        try:
            mat.write(f'\nA pagina: {url} contem: {v}\n\n')
        except:
            print('Erro ao escrever')
    x += 1

# for v in soup.find_all('a'):
#     print(v)

# print(hi)


# print(hi[0].getText())

# print(soup.title.string)


# print(soup.p)
