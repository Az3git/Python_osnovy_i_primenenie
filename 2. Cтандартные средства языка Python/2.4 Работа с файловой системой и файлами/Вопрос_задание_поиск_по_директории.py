import os.path
dicte = []


os.chdir("/home/alexeydworf/Downloads/MainMain")

f = open("output", "w")

for current_dir, dirs, files in os.walk("."):
    for file in files:
        exenc = file.partition('.')[2]
        if exenc == 'py':
            current_dir = current_dir[2:]
            dicte.append(current_dir)
            break

    print('\n')

for elem in sorted(dicte):
    f.write(elem)
    f.write("\n")