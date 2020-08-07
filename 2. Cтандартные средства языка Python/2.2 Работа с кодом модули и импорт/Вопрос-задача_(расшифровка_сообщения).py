import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)
    print(type(encrypted))


with open("passwords.txt", "rb") as inp:
    passwords = inp.read().splitlines()
print(passwords)

for el in passwords:
    try:
        print(simplecrypt.decrypt(el, encrypted).decode('utf8'))
    except Exception:
        print('пох')



