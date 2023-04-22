def string_to_bits(s):
    # Convertir une chaîne de 8 bits en liste d'entiers
    bits = []
    for c in s:
        bits.append(int(c))
    return bits

def bits_to_string(bits):
    # Convertir une liste d'entiers en chaîne de 8 bits
    s = ""
    for bit in bits:
        s += str(bit)
    return s

def shift_left(array, n):
    # Décaler une liste vers la gauche de n positions
    shifted = array[n:] + array[:n]
    return shifted

def shift_right(array, n):
    # Décaler une liste vers la droite de n positions
    shifted = array[-n:] + array[:-n]
    return shifted

# Demander à l'utilisateur la clé K et la permutation H
k_string = input("Entrez la clé K (8 bits) : ")
h_string = input("Entrez la permutation H (8 chiffres) : ")

# Vérifier que la clé et la permutation ont la bonne longueur
if len(k_string) != 8 or len(h_string) != 8:
    print("La clé et la permutation doivent avoir une longueur de 8 bits.")
    exit()

# Convertir la clé et la permutation en listes d'entiers
k_bits = string_to_bits(k_string)
h_perm = string_to_bits(h_string)

# Demander à l'utilisateur l'ordre de décalage pour les sous-clés
shift_order = int(input("Entrez l'ordre de décalage pour les sous-clés (1 ou 2) : "))
if shift_order != 1 and shift_order != 2:
    print("L'ordre de décalage doit être 1 ou 2.")
    exit()

# Demander à l'utilisateur sa propre permutation
custom_perm_answer = input("Voulez-vous utiliser une permutation personnalisée ? (O/N) : ")
if custom_perm_answer.upper() == "O":
    # Demander à l'utilisateur de saisir sa propre permutation
    p_perm = []
    print("Entrez votre permutation personnalisée (4 chiffres) : ")
    for i in range(4):
        p_perm.append(int(input()))
else:
    # Utiliser la permutation par défaut
    p_perm = [2, 0, 1, 3]

# Demander à l'utilisateur le bloc C de 8 bits
c_string = input("Entrez le bloc C de 8 bits : ")
c_bits = string_to_bits(c_string)

# Appliquer la permutation H
h_permuted = [0] * 8
for i in range(8):
    h_permuted[h_perm[i]] = c_bits[i]

# Diviser le bloc en deux blocs de 4 bits
g2_bits = h_permuted[:4]
d2_bits = h_permuted[4:]

# Calculer les sous-clés
if shift_order == 1:
    k1_bits = shift_left(k_bits, 1)
    k2_bits = shift_left(shift_left(k_bits, 1), 2)
else:
    k1_bits = shift_left(k_bits, 2)
    k2_bits = shift_left(shift_left(k_bits, 2), 1)
g1_bits = [p_perm.index(i) for i in range(4)]
d1_bits = [p_perm.index(i) for i in range(4)]
for i in range(4):
    g1_bits[i] = d2_bits[p_perm[i]] ^ k1_bits[i]
    d1_bits[i] = g2_bits[i] ^ (g1_bits[i] | k1_bits[i])
g0_bits = [p_perm.index(i) for i in range(4)]
d0_bits = [p_perm.index(i) for i in range(4)]
for i in range(4):
    g0_bits[i] = d1_bits[p_perm[i]] ^ k2_bits[i]
    d0_bits[i] = g1_bits[i] ^ (g0_bits[i] | k2_bits[i])

# Concaténer les blocs G0 et D0
n_bits = g0_bits + d0_bits

# Appliquer l'inverse de la permutation H
n_permuted = [0] * 8
for i in range(8):
    n_permuted[i] = n_bits[h_perm[i]]

# Afficher le texte clair
print("Texte clair :", bits_to_string(n_permuted)) 