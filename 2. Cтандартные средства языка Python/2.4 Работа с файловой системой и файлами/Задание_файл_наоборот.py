

with open ("dataset_24465_4.txt") as f, open ("вывод.txt", 'w') as w:
    x = f.read().splitlines()
    x = x[::-1]
    contens = "\n".join(x)
    w.write(contens)