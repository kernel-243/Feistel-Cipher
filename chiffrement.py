def string_to_bits(s):
    """Convertir une chaîne de 8 bits en liste d'entiers"""
    return [int(c) for c in s]

def bits_to_string(bits):
    """Convertir une liste d'entiers en chaîne de 8 bits"""
    return ''.join(str(b) for b in bits)

def shift_left(array, n):
    """Décaler une liste vers la gauche de n positions"""
    return array[n:] + array[:n]

def shift_right(array, n):
    """Décaler une liste vers la droite de n positions"""
    return array[-n:] + array[:-n]

# Demander à l'utilisateur la clé K et la permutation H
k = input("Entrez la clé K (8 bits) : ")
h = input("Entrez la permutation H (8 chiffres) : ")

# Vérifier que la clé et la permutation ont la bonne longueur
if len(k) != 8 or len(h) != 8:
    print("La clé et la permutation doivent avoir une longueur de 8 bits.")
    exit()

# Convertir la clé et la permutation en listes d'entiers
k_bits = string_to_bits(k)
h_perm = string_to_bits(h)

# Diviser N en deux blocs de 4 bits
g0_bits = h_perm[:4]
d0_bits = h_perm[4:]

# Calculer les sous-clés
p_perm = [2, 0, 1, 3]
k1_bits = [k_bits[i] ^ k_bits[i+4] for i in range(4)]
k2_bits = [k_bits[i+4] & k_bits[i] for i in range(4)]
g1_bits = [d0_bits[p_perm[i]] ^ k1_bits[i] for i in range(4)]
d1_bits = [g0_bits[i] ^ (g1_bits[i] | k1_bits[i]) for i in range(4)]
g2_bits = [d1_bits[p_perm[i]] ^ k2_bits[i] for i in range(4)]
d2_bits = [g1_bits[i] ^ (g2_bits[i] | k2_bits[i]) for i in range(4)]

# Concaténer les blocs G2 et D2
c_bits = g2_bits + d2_bits

# Appliquer l'inverse de la permutation H
c_perm = [0] * 8
for i in range(8):
    c_perm[h_perm[i]] = c_bits[i]

# Afficher le texte chiffré
print("Texte chiffré :", bits_to_string(c_perm)) 
