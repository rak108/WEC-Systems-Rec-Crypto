# WEC-Systems-Rec-Crypto
This is the code for WEC NITK 2020 Systems Recruitment, and is for the Cryptography task.
The code is done in python, taking the required single line input and giving the required output, which is also attached in a text file. It implements the decoding functions for the following ciphers:
Base64 decoder, ROT13 cipher, Caeser Cipher, Vigenere Cipher and the Playfair Cipher.

## Problem Statement
### Cryptography
Introduction: 
Cryptography is a method of protecting information and communications through the use of codes so that only those for whom the information is intended can read and process it. The prefix "crypt-" means "hidden" or "vault" -- and the suffix "-graphy" stands for "writing."

In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation, digital signing, verification to protect data privacy, web browsing on the internet, and confidential communications such as credit card transactions and email.

Problem Statement: 
Alice wants to send a hidden message to Bob, who is a cryptography novice, aspiring to join web club but instead of sending the message directly to Bob she encrypts it in the following way:
The message is passed through a system containing 5 different encryption algorithm each done one after the other.
So consider the plaintext p1, is passed through 5 algorithms(e1,e2,e3,e4,e5) to get the ciphertext c1 in the following way:

P1 -> e1 -> e2 -> e3 -> e4 -> e5 -> C1

Now Bob receives the ciphertext C1 and notices that the input is in the form of 5 lines of text.
Alice reveals that the 1st line of the ciphertext is the most important and the other 4 lines are just hints which will help out in proceeding further.
So when Bob moves backwards in deciphering the text he first has to figure out e5 and once he decrypts the whole input line by line using the decryption algorithm for e5 he notices that the line 5 will provide him with some meaningful information to know that he is going on the right track and some vital information for the next step which is e4. Since Bob has finished decrypting line 5, it can now be discarded with only 4 lines left and Bob proceeds in the same way for 4 more times until only the 1st line remains with the final message. Notice that the first line is encrypted 5 times, the second line is encrypted 4 times, and so on, in the order described above.
Also Since Bob is just a cryptography novice, Alice has decided to test Bob's skills only based on some pre-existing encryption algorithms rather than creating algorithms on her own.
Can you help Bob out in figuring out the final message by implementing a program that takes 1 line of input(the 1st line) and outputs the final hidden message?

Input:

d3ZucXN0b2tib2xlamp5ZW5zdnlicGpsa3VhcGx2

b2dzd2xmcndwb2JmY2J4dmdtZGZseGp1dnZuaGZ0amFiZ2M=

YW9sdWxlYXJsZnB6anlmd2F2bnlod29m 					

aGZyZ3VyeHJsZ2pyYWds					

Z3JlYXRzdGFydA== 		

Alice also sends Bob a piece of paper which gives Bob an input and an output for each encryption algorithm so that Bob can figure out which encryption algorithm has been used at each step as follows.

e1:
	alice ------------key = cqyadmnwgetzboulsxhfkpivr -------> CHKYWF
  
e2 :
	says -------------key = abc----------------------> sbas

e3 :	
	all -----------------key = 5 --------------------> fqq

e4 :
	the  ------------no key----------------> gur

e5 :
	Best ---------no key---------> YmVzdA==
