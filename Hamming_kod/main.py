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

# Pro zobrazení výsledku
print("Číslo je : " + data)