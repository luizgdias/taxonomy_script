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
    # print(category)
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
    taxonomy = json.loads(f.read())
    taxonomy_name = taxonomy['ns1:taxonomySubject']['ns1:subject']['ns1:name']

for category in taxonomy['ns1:taxonomySubject']['ns1:taxonomy']['ns1:category']['ns1:category']:
    apnd = open('file.txt', 'a+')
    # verifica se a categoria possui filhos, se possuir add numa lista do tipo: 
    # ['nome_taxonomia', 'nome_clase', 'nome_subclasse1', 'mome_subclasse2', 'nome_subclasseN']
    verify_sub(category, taxonomy_name)
    apnd.close()




# path = '/home/luizgustavo/Documentos/Taxonomia-Petrobras/SoapClientBaseDocumentos/out'
# directory = []
# # r=root, d=directories, f = directory
# for r, d, f in os.walk(path):
#     for path_arquivo in f:
#         if '.json' in path_arquivo:
#             directory.append(os.path.join(r, path_arquivo))

# for arquivo in directory:
#     print(arquivo)
#     temp = arquivo.split('out/')
#     print(str(temp[1]))
#     with open(arquivo) as f:
#         taxonomy = json.loads(f.read())
#         taxonomy_name = taxonomy['ns1:taxonomySubject']['ns1:subject']['ns1:name']
#         print(taxonomy_name)
#     for cat in taxonomy['ns1:taxonomySubject']['ns1:taxonomy']['ns1:category']:
#         if 'ns1:name' in cat:
#             print(cat)