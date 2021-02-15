import requests
import json

n1 = 8
n2 = 6

for i in range(255):
    data = {'guess':0}
    r = requests.post('http://ctf.nus-cs2107.com:2774/submit',data=data)
    # soup = BeautifulSoup(r.text, 'html.parser')
    d = json.loads(r.text)
    # print(soup)

    # print(d)
    
    isCorrect = d['correct']
    ans = d['answer']

    print(isCorrect, ans)