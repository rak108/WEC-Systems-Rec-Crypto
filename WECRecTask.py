#Encryption method 5 is the base64 encoder-decoder
def base64_decoder(ciphertexte5):
    key_set="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    key=''.join(key_set)
    originalbinarystring=""
    plaintexte5=""
    for letter in ciphertexte5:
            if letter in key:
                binaryletter=bin(key.index(letter)).lstrip("0b")
                binaryletter=binaryletter.zfill(6)
                originalbinarystring+=binaryletter
    for i in range(0,len(originalbinarystring),8):
        letter=originalbinarystring[i:i+8]
        plaintexte5+=chr(int(letter,2))
    return plaintexte5

#Encryption method 4 is ROTF13, basically Caesar cipher with key=13
def rotf13_decoder(ciphertexte4):
    plaintexte4=""
    for letter in ciphertexte4:
        letterint=ord(letter)-ord("a")
        letterint=(letterint+13)%26 + ord("a")
        plaintexte4+=chr(letterint)
    return plaintexte4

#Encryption method 3 is Caesar Cipher with key 20
def caesar_decoder(ciphertexte3,key):
    plaintexte3=""
    for letter in ciphertexte3:
        letterint=ord(letter)-ord("a")
        if letterint>key:
            letterint=(letterint-key)%26 + ord("a")
            plaintexte3+=chr(letterint)
        else:
            letterint=(letterint+(26-key))%26 + ord("a")
            plaintexte3+=chr(letterint)
    return plaintexte3

#Encryption method 2 is Vigenere cipher with key "Cryptography"
def vigenere_decoder(ciphertexte2,key):
    key_length=len(key)
    intkey = [ord(i) for i in key]
    intciphertext = [ord(i) for i in ciphertexte2]
    plaintexte2=""
    for i in range(len(intciphertext)):
        plaintext=(intciphertext[i]-intkey[i%key_length]+ 26)%26
        plaintexte2+=chr(plaintext+ord("A"))
    return plaintexte2

#Encryption method 1 is Playfair cipher with key "NATDSZGRQHEBVPMXILFYWCUKOC"
def pairs(ciphertexte1):
    cipherarray=[]
    for letter in range(0,len(ciphertexte1),2):
        cipherarray.append(ciphertexte1[letter:letter+2])
    return cipherarray

def key_matrix(key):
    alphabets="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key1dmatrix=[]
    for letter in key:
        key1dmatrix.append(letter)
    
    for letter in alphabets:
        if letter not in key1dmatrix:
            key1dmatrix.append(letter)

    keymatrix=[[0 for i in range(5)] for j in range(5)]
    k=0
    for i in range(0,5):
        for j in range(0,5):
            keymatrix[i][j]=key1dmatrix[k]
            k+=1

    return keymatrix

def location(keymatrix, letter):
    loc=[]
    for i in range(5):
        for j in range(5):
            if keymatrix[i][j]==letter:
                loc.append(i)
                loc.append(j)
    return loc

def playfair_decoder(ciphertexte1,key):
    ciphertext=pairs(ciphertexte1)
    keymatrix=key_matrix(key)
    plaintext=[]
    for cipher in ciphertext:
        position1=location(keymatrix,cipher[0])
        position2=location(keymatrix,cipher[1])
        if position1[0]==position2[0]:
            plaintext.append(keymatrix[position1[0]][(position1[1]+4)%5])
            plaintext.append(keymatrix[position2[0]][(position2[1]+4)%5])
        elif position1[1]==position2[1]:
            plaintext.append(keymatrix[(position1[0]+4)%5][position1[1]])
            plaintext.append(keymatrix[(position2[0]+4)%5][position2[1]])
        else:
            plaintext.append(keymatrix[position1[0]][position2[1]])
            plaintext.append(keymatrix[position2[0]][position1[1]])

    originalmessage=''.join(plaintext)
    return originalmessage

#Main function
def main():
    cipher_text=(input("\nEnter cipher text: "))
    decrypted_e5= base64_decoder(cipher_text)
    # print(decrypted_e5)
    decrypted_e4= rotf13_decoder(decrypted_e5)
    # print(decrypted_e4)
    decrypted_e3=caesar_decoder(decrypted_e4,20)
    # print(decrypted_e3)
    decrypted_e2=vigenere_decoder(decrypted_e3,"cryptography")
    #print(decrypted_e2)
    plain_text=playfair_decoder(decrypted_e2,"NATDSZGRQHEBVPMXILFYWCUKOC")
    print("\nFinal plaintext obtained after 5 rounds of decryption is: \n" + plain_text)


if __name__ == "__main__":
     main() 