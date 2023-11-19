import numpy
import sys

# Mapa znaků
text2num = {
	'A': '0000',
	'B': '0001',
	'C': '0010',
	'D': '0011',
	'E': '0100',
	'F': '0101',
	'G': '0110',
	'H': '0111',
	'I': '1000',
	'J': '1001',
    'K': '1001',
    'L': '1010',
    'M': '1100',
    'N': '1101',
    'O': '1110',
    'P': '1111'
}

# Zadání znaků
num = "P"

# Překládání znaků na čísla
# Používáme tyto funkce join() + split()
data = ''.join(text2num[ele] for ele in num.split())


if (len (sys.argv) > 1):
    data = sys.argv[1]


def encode(m,g):
    x = numpy.dot (m,g) % 2
    return x


def decode(m,h):
    dec = numpy.dot (h,m) % 2
    return dec


def Flip_Bit(enc,bitpos):
    if (enc[bitpos] == 1):
        enc[bitpos] = 0
    else:
        enc[bitpos] = 1
    return enc


def hamming(a):
    g = numpy.array ([[1,0,0,0,1,1,1],[0,1,0,0,0,1,1],[0,0,1,0,1,0,1],[0,0,0,1,1,1,0]])
    h = numpy.array ([[1,0,1,1,1,0,0],[1,1,0,1,0,1,0],[1,1,1,0,0,0,1],])

    a = a[:4]

    enc = encode (a,g)

    dec = decode (enc,h)
    print ("Vstup  \t\tKod (1 error)  \tError pozice")
    print (a,"\t",enc,"\t",dec)

    print ("----------------------")
    print ("1 error:")
    print ("Vstup  \t\t Kod (1 error)  \t Error pozice")
    for i in range (0,7):
        enc = encode (a,g)
        enc1 = Flip_Bit (enc,i)
        dec = decode (enc1,h)
        print (a,"\t",enc1,"\t",dec)


a = numpy.frombuffer (data.encode (),dtype=numpy.uint8) - ord ('0')

hamming (a)