import requests
import json
from xs128p import main

# n1 = 8
# n2 = 6

# prevans = None
# ans = None

lst = []



def getNums():
    ck = {'connect.sid':''}
    for i in range(108):
        data = {'guess':0}
        r = requests.post('http://ctf.nus-cs2107.com:2774/submit',data=data,cookies=ck)
        h = r.headers
        cok = h['Set-Cookie']
        cok = cok[cok.index('=')+1:cok.index(';')]
        ck={'connect.sid':cok}
        # print(ck)
        # soup = BeautifulSoup(r.text, 'html.parser')
        d = json.loads(r.text)
        # print(soup)

        # print(d)
        
        isCorrect = d['correct']

        if isCorrect:
            ans = 0
        else:
            ans = d['answer']

        if d['score'] == 10:
            print(d['flag'])
        
        lst.append(ans)
        # print(isCorrect, ans)

    print(''.join(str(ch) for ch in lst))
    # back = lst[12:]
    back = lst
    flst = []
    for i in range(6):
        c = back[i*18:(i+1)*18][::-1]
        sn = ''.join(str(ch) for ch in c)
        flst.append(int(sn))
    print(flst)
    print(ck)
    return ck








def proceed():
    ck = {'connect.sid': 's%3ArDSnqlkqXVwefwh3dN6DluskLAk16vZ2.1YAvU40OTkCHQTF9Q4h7xGHliOwL13i8IGfzmFKzJUE'}
    nextnum = 9884892174577977
    for i in range(10):
        data = {'guess':nextnum%10}
        nextnum /= 10
        r = requests.post('http://ctf.nus-cs2107.com:2774/submit',data=data,cookies=ck)
        h = r.headers
        cok = h['Set-Cookie']
        cok = cok[cok.index('=')+1:cok.index(';')]
        ck={'connect.sid':cok}

        d = json.loads(r.text)

        
        print(d)
    return d

# currCk = getNums()
# proceed()

def bruteforce():
    nums = [8891143815076903, 4598546047717944, 5496683590751053, 5051138430094635, 6375047782415866, 8392165846495605]
    
    cnum=nums[:-1]

    for i in range (99999):
        s = str(i)
        s = (5-len(s))*'0'+s
        cnum = list(str(n) for n in nums[:-1])
        for j in range(5):
            cnum[j] = float('0.' + s[j] + cnum[j])
        if main(cnum):
            return 

bruteforce()
