from cipher import decrypt, pad_key, IV

info = ['31', 'August', '8', '08', 'Aug', '1976', 'Petya', 'Tan', 'Ah', 'Huey', 'TAH', 'Stuxnet', 'Wannacry', 'Rose', 'Ng', 'Mary', 'accountant','accounting', 'taxes', 'walks', 'beach', 'Dahlias', '3235', 'Security', 'Drive', 'Block', '2107C', '94561256', 'blue']

delimiter = ['','-','_',' ']
c = 'b/XyIz3oPwptQvJmEr7RG74q80Lpw8jFT/Zd95uCKY4='

wordlist = [info]

def d():
    # Check for single word password
    for word in info:
        currkey = pad_key(word)
        try:
            done = decrypt(currkey, IV, c)
            print(currkey)
            print(done)
            return
        except UnicodeDecodeError:
            continue
    
    # Multi-word
    i = 1
    while len(wordlist) < 5:
        wordlist.append([])
        for preword in wordlist[i-1]:
            for joiner in delimiter:
                for word in info:

                    # Build and pad the guessed key
                    currstr = preword + joiner + word
                    currkey = pad_key(currstr)
                    
                    # Use to decrypt
                    try:
                        done = decrypt(currkey, IV, c)
                        print(currkey)
                        print(done)
                        return
                    except UnicodeDecodeError:
                        continue
                    finally:
                        wordlist[i].append(currstr)
        i += 1
                    
d()
    
