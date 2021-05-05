from bs4 import BeautifulSoup
import urllib.request
import xml.etree.ElementTree as ET
from tqdm import tqdm
from time import sleep
#Try With This Website  http://igm.univ-mlv.fr/
LinksList = []
def progress(rang):
    for i in tqdm(rang, desc ="Progress : "):
            sleep(.1)

var=input("Enter a Website : ")
var=str(var)
html_page = urllib.request.urlopen(var)
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    linkfound = link.get('href')
    progress(link)
    if linkfound == '#' or linkfound == 'None' or linkfound == '/' or linkfound == None :
        pass
    else:
        LinksList.append(linkfound)
print(f"We've Found {len(LinksList)} Arborescence")

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem 

xml_dox = ET.Element('root')
for i in range(0,len(LinksList)-1):
    LinksList[i] = ET.SubElement(xml_dox,f'{LinksList[i]}')
    ET.SubElement(LinksList[i], f'{LinksList[i]}')
    ET.SubElement(LinksList[i], f'{LinksList[i+1]}')
indent(xml_dox)
tree = ET.ElementTree(xml_dox)
#I Named The File With These Name Cause I have problem with other Names But You Can Name it Whatever You Like
tree.write('pypy.xml',encoding='utf-8',xml_declaration=True)
input()