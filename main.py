import xml.etree.ElementTree as ET
import json, os

def super_classes_glossario(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for child in root:
        for x in child:
            print(x[0].tag)
            for y in x:
                print(y[0].text, y[1].text)

def categories_glossario(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

def verifica(i):
    if 'ns1:category' in i:
        print(i['ns1:category'])
        for j in i['ns1:category']:
            verifica(j)

def verify_sub(category, taxonomy):
    print(category)
    buff = "['" + taxonomy
    with open('taxonomy_1.json') as f:
        categories = json.loads(f.read())
    apnd = open('file.txt', 'a+')
    # print(category['ns1:name'])
    if 'ns1:category' in category:
        
        buff = buff +"', "+category['ns1:name']  +"', " 
        # print('category ', category['ns1:name'], 'tem sub = ')
        for i in category['ns1:category']:
            # print('o sub de ', category['ns1:name'], ' é ', i['ns1:name'])
            buff = buff + "'"+i['ns1:name'] + "', "
            verify_sub(i, taxonomy)
            # buff = buff + x
        buff = buff + "]\n"
        buff = buff.replace(", ]","]")
        apnd.write(buff)
        print('retorno if')
        print(buff)
    else:
        buff = buff + "', "+category['ns1:name'] + "']\n"
        print('retorno else')
        print(buff)
        apnd.write(buff)
        apnd.close()


# super_classes_glossario('subjects.xml')
# categories_glossario('taxonomy1.xml')
with open('taxonomy_1.json') as f:
        categories = json.loads(f.read())

for i in categories['ns1:taxonomySubject']['ns1:taxonomy']['ns1:category']['ns1:category']:
    apnd = open('file.txt', 'a+')
    verify_sub(i, categories['ns1:taxonomySubject']['ns1:subject']['ns1:name'])
    apnd.close()

print(categories['ns1:taxonomySubject']['ns1:subject']['ns1:name'])

    # print(x)
# path = '/home/luizgustavo/Documentos/Taxonomia-Petrobras/SoapClientBaseDocumentos/out'

# directory = []
# # r=root, d=directories, f = directory
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.json' in file:
#             directory.append(os.path.join(r, file))

# for file in directory:
#     # print(file)
#     with open(file) as f:
#         categories = json.loads(f.read())
#         for i in categories['ns1:taxonomySubject']['ns1:taxonomy']['ns1:category']:
#             verify_sub(i)