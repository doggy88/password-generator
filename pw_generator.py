import random
import string

def generate_password(length, chars):
    """Ez a függvény egy véletlenszerű jelszót generál a felhasználó által megadott hosszúság és karakterkészlet alapján."""
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    """Ez a fő program, amely kéri a felhasználótól a jelszó hosszát és karakterkészletét, majd kiírja a generált jelszót."""
    length = int(input("Adja meg a jelszó hosszát: "))
    chars = ''
    if input("Használjon nagybetűket? (igen/nem) ").lower() == "igen":
        chars += string.ascii_uppercase
    if input("Használjon kisbetűket? (igen/nem) ").lower() == "igen":
        chars += string.ascii_lowercase
    if input("Használjon számokat? (igen/nem) ").lower() == "igen":
        chars += string.digits
    if input("Használjon speciális karaktereket? (igen/nem) ").lower() == "igen":
        chars += string.punctuation
    password = generate_password(length, chars)
    print("A generált jelszó:", password)

if __name__ == '__main__':
    main()
