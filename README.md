# Get Website Tree Structure By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

`from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

`from time import sleep`

### The I Used The Library Imaplib To Give Me Acces To Gmail Account

`import imaplib`

### I've Made a Function For The Progress Bar Like That :

    def progress(rang):
    for i in tqdm(rang, desc ="Progress : "):
            sleep(.1)

> As You All Can See I Made This Progress Bar Relative To The Searching Progress

---

# Let's Begin The Code Explanation :

## When We Talk About dealing With Websites We are Talking About Scraping Data From There So We Need A Library Called :

> Beautiful Soup

> `from bs4 import BeautifulSoup`

## And We Need To Deal With Links And Urls So We Need A library Called "Urllib" To Get Requests :

> `import urllib.request`

## And Of Course At The End We've Must To Write The Result in a XML File

### So To Deal With XML Files You Must use a Library :

`import xml.etree.ElementTree as ET`

# let's Begin Our Program :

## We've Started With Asking For Website To Use it In The Scrapping Process :

    var=input("Enter a Website : ")

## Secondely Get The Website a string Format To Make The Library Have A Search For Your Desired Website :

    var=str(var)
    html_page = urllib.request.urlopen(var)
    soup = BeautifulSoup(html_page)

## We Need To Loop On The HTML Result Given and Only Select The href Links So That Will Give us in a certain Way How Much Websites are under these Website as Given Below

> This Will Find For Us Only The "a" Tags

    for link in soup.findAll('a'):

> We Will Also Scrap The Href In Order To Get directories

        linkfound = link.get('href')

> We Call The Progress Bar Will The Program Is Looking For Links

        progress(link)

> You Will Need This Conditions In Order To Not fulfill The List Of Links With Empty Ones

        if linkfound == '#' or linkfound == 'None' or linkfound == '/' or linkfound == None :
            pass

> If The Program Found A Logic Looking Link it Will Be Added to The Links List To Count Them Later

        else:
            LinksList.append(linkfound)

---

## Write The Result On a XML File

### First Thing I Need To Make my XML File Good Looking File So I've Used a Prettier Script :

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

## Now The Writing Part

### So Each Time I Need to Write The Parent Element Tag And Then The Child Element

    xml_dox = ET.Element('root')
    for i in range(0,len(LinksList)-1):
        LinksList[i] = ET.SubElement(xml_dox,f'{LinksList[i]}')

> Write The Parent Element :

        ET.SubElement(LinksList[i], f'{LinksList[i]}')

> Write The Child Element :

        ET.SubElement(LinksList[i], f'{LinksList[i+1]}')
    indent(xml_dox)
    tree = ET.ElementTree(xml_dox)

> Now Write It :

    tree.write('yourfile.xml',encoding='utf-8',xml_declaration=True)

---

Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)
