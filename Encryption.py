alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
allen = len(alphabets)
inp=input("Type the secret message that to be delivered to Hitler: ").lower()
outp=""
shino=int(input("choose the shift no: "))

for eachltr in inp:
    i=0
    finish=False
    while not finish:
        letter=alphabets[i]
        if eachltr==letter:
            outpltr=alphabets[i + shino]
            outp+=outpltr
            finish=True
        else:
            i+=1
        
        
print(f"Send this as it is to thatass: {outp}")

        
        