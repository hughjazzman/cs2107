import requests
from bs4 import BeautifulSoup

og = bytearray.fromhex('90e31e0976237046b219cad55d3a3d996746308c14e2f8bddd5f757c0d565c2fb9cf316278785a6035b29f6d75c64e2bbc44b486c6052344157256974f907c03ba6ddd351f5e0515e9902f377c184bf9ec4feec430b7f96db8fb9b6b960e377948099003f613bd02de4df3a49903087e8e09d23f6a738cf16a4de2494943229859cf69c8f947ef434b5e4b00eace1531a490b5c48219dbc9e61b0b9d99e4ebe81505e7cab31dbb6ed03f4d5f67d9ea66a689430f17d7c0ccc584fc0acdf3ae2757a7a0e4375a275ae880a26cddf9610530b6e097d8ae78c7dff7f0d6c055c74f02098b425c00a222e33840694243d4334ff40980de801b5d030ac3dd2e4620bba220c58997a3c4ffa01ea1dd77caec0e')
iv = og[-16:]
cblock = len(og)//16 - 1

# to get initial padding
def getpad():
    i = -1
    while True:
        ng = og.copy()
        ng[i] = 0
        
        # send data to check encrypted block
        data = {'data': ng.hex()}
        r = requests.post('http://ctf.nus-cs2107.com:2773/',data=data)
        soup = BeautifulSoup(r.text, 'html.parser')

        # encrypted block to compare brute force
        act = soup.find(id="result").string
        if act == "Successful!":
            print(i)
            
        i -= 1
    return i

# getpad()

# decryption of a single block
def decblock(res, c, iv):
    ogc = c.copy()
    for i in range(len(res), 16):
        c = ogc.copy()

        # get appropriate XOR'd values
        for j in range(i):
            c[-j-1] ^= (res[j] ^ (i-j+1))

        currbt = c[-i-1]
        # brute force 256 bytes to guess the next byte
        for t in range(256):
            c[-i-1] = t ^ currbt

            data = {'data':(c+iv).hex()}
            r = requests.post('http://ctf.nus-cs2107.com:2773/',data=data)
            soup = BeautifulSoup(r.text, 'html.parser')

            # encrypted block to compare brute force
            act = soup.find(id="result").string
            if act == "Successful!":
                print(chr(t ^ 1))
                # add to current block's plaintext
                res.append(t ^ 1)
                break
        print(act)
    return res

def padoracle():
    iv = og[-16:]
    i = 3

    # final result
    finalres = bytearray()
    # initial padding
    res =  bytearray((3,2,1))
    
    for i in range(cblock):
        # add next block's decryption to final result
        finalres.extend(decblock(res, og[:-(i+1)*16], iv))
        # update iv to next block
        iv = og[-(i+2)*16:-(i+1)*16]
        # to check current block plaintext
        print(bytes(res[::-1]))
        # clear plaintext block for next iteration
        res.clear()
    return bytes(finalres[::-1])

print(padoracle())      
