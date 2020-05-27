import listAndDict as lad

#======================================================
#My Test code
print("My Test code for letterFrequency")
print("")
print(" The past and present energies, which guide the tragic genre, find their roots in the Ancient Attican Tradition. :")
print("\tExpected: {T': 2, 'h': 6, 'e': 13, ' ': 17, 'p': 2, 'a': 5, 's': 4, 't': 11, 'n': 10, 'd': 4, 'r': 7, 'g': 4, 'i': 11, ',': 2, 'w': 1, 'c': 4, 'u': 1, 'f': 1, 'o': 3, 'A': 2, '.': 1}")
print("\tYour output:", lad.letterFrequency("The past and present energies, which guide the tragic genre, find their roots in the Ancient Attican Tradition."))
print("")
print("")
print("My Test Code for primeList")
print("n = 100:")
print("\tExpected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]")
print("\tYour output:", lad.primeList(100))
print("")
print("")
print("======================================================")
#======================================================
# Given Test Code
print("Testing letterFrequency:")
print("aaaaaaaa:")
print("\tExpected: {'a': 8}")
print("\tYour output:", lad.letterFrequency("aaaaaaaa"))
print()
print("Here is a nice, big sentence.:")
print("\tExpected: {'H': 1, 'e': 6, 'r': 1, ' ': 5, 'i': 3, 's': 2, 'a': 1, 'n': 3, 'c': 2, ',': 1, 'b': 1, 'g': 1, 't': 1, '.': 1}")
print("\tYour output:", lad.letterFrequency("Here is a nice, big sentence."))
print()
print("The quick brown fox jumps over the lazy dog:")
print("\tExpected: {'T': 1, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 't': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}")
print("\tYour output:", lad.letterFrequency("The quick brown fox jumps over the lazy dog"))
print()
print("1t sh0uld w0rk w1th numb3r5 t00:")
print("\tExpected: {'1': 2, 't': 3, ' ': 5, 's': 1, 'h': 2, '0': 4, 'u': 2, 'l': 1, 'd': 1, 'w': 2, 'r': 2, 'k': 1, 'n': 1, 'm': 1, 'b': 1, '3': 1, '5': 1}")
print("\tYour output:", lad.letterFrequency("1t sh0uld w0rk w1th numb3r5 t00"))
print()
print("It. should;; even!. work><< with., crazy; punctuation::")
print("\tExpected: {'I': 1, 't': 4, '.': 3, ' ': 6, 's': 1, 'h': 2, 'o': 3, 'u': 3, 'l': 1, 'd': 1, ';': 3, 'e': 2, 'v': 1, 'n': 3, '!': 1, 'w': 2, 'r': 2, 'k': 1, '>': 1, '<': 2, 'i': 2, ',': 1, 'c': 2, 'a': 2, 'z': 1, 'y': 1, 'p': 1, ':': 2}")
print("\tYour output:", lad.letterFrequency("It. should;; even!. work><< with., crazy; punctuation::"))
print("\n")

print("Testing primeList:")
print("n = 7:")
print("\tExpected: [2, 3, 5, 7, 11, 13, 17]")
print("\tYour output:", lad.primeList(7))
print("n = 15:")
print("\tExpected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]")
print("\tYour output:", lad.primeList(15))
print("n = 25:")
print("\tExpected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]")
print("\tYour output:", lad.primeList(25))
print("\n")