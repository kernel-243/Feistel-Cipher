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

# Diviser K en deux blocs de 4 bits
k1_bits = [k_bits[i] ^ k_bits[i+4] for i in range(4)]
k2_bits = [k_bits[i+4] & k_bits[i] for i in range(4)]

# Demander à l'utilisateur l'ordre de décalage pour k1 et k2
shift1 = int(input("Entrez l'ordre de décalage pour k1 : "))
shift2 = int(input("Entrez l'ordre de décalage pour k2 : "))

# Appliquer les décalages à k1 et k2
k1_shifted = shift_left(k1_bits, shift1)
k2_shifted = shift_right(k2_bits, shift2)

# Afficher les sous-clés générées
print("Sous-clé 1 :", bits_to_string(k1_shifted))
print("Sous-clé 2 :", bits_to_string(k2_shifted))