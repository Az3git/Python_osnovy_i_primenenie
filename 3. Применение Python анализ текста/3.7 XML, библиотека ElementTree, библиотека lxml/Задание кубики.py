from xml.etree import ElementTree

dicto = {}
blue = 0
red = 0
green = 0
root = ElementTree.fromstring(input())

for element in root.iter():
    print(element.tag, element.attrib)
    if element.attrib['color'] == 'blue':
        blue += 1
    elif element.attrib['color'] == 'red':
        red += 1
    elif element.attrib['color'] == 'green':
        green += 1
    break

def search_child (root, hit = 0):
    global blue
    global red
    global green
    for element in root:
        print(element.tag, element.attrib)
        if element.attrib['color'] == 'blue':
            blue += hit
        elif element.attrib['color'] == 'red':
            red += hit
        elif element.attrib['color'] == 'green':
            green += hit
        search_child(element, hit + 1)

search_child(root, 2)

print(red, green, blue)