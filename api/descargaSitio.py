import requests
import json

url = 'http://www.thehackernews.com'
data = requests.get(url)
content = data.text


with open('sitio.html','w') as f:
    f.write(content)


def funcion3():
    return

def funcion2():
    return

def funcion1():
    return


if __name__ =='__main__':
    funcion1()
















import requests




if __name__ =='__main__':
    url ='http://google.com'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        file = open('google.html','wb')
        file.write(content)
        file.close()
