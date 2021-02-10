import requests
from bs4 import BeautifulSoup

def aes():
  # secret string to build with (contains flag)
  secret = '\n'
  
  # arbitrary number of blocks to start with, increase if more needed
  k = 10
  
  for i in range(100):
      # prepended string
      p = (16*k - 2 - i) * '!'
      
      # send data to check encrypted block
      data = {'creds': p}
      r = requests.post('http://ctf.nus-cs2107.com:2772/',data=data)
      soup = BeautifulSoup(r.text, 'html.parser')
      
      # encrypted block to compare brute force
      act = soup.find(id="new-creds").string[32*(k-1):32*k]
      
      # bruteforce characters
      for j in range(33,128):
          # add chr 1-by-1, secret required the newline character
          data = {'creds': p + secret + chr(j)}
          r = requests.post('http://ctf.nus-cs2107.com:2772/',data=data)
          soup = BeautifulSoup(r.text, 'html.parser')
          
          # retrieve new encrypted block
          enc = soup.find(id="new-creds").string[32*(k-1):32*k]

          # if new block and actual block are equal
          if enc == act:
              # then guessed char is correct, add to string
              secret += chr(j)
              if chr(j) == '}':
                  return secret
              print("chr",j, chr(j))
              break

print(aes())
        

