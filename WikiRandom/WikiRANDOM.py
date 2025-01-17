#PROCURA NA WIKIPEDIA A PARTIR DE UM LUGAR INICIAL E GERA LINKS RANDOMICOS
from	urllib.request	import	urlopen 
from	bs4	import	BeautifulSoup 
import	datetime 
import	random 
import	re

random.seed(datetime.datetime.now()) 
def	getLinks(articleUrl):				
	html	=	urlopen("http://pt.wikipedia.org"+articleUrl)				
	bsObj	=	BeautifulSoup(html)				
	return	bsObj.find("div",	{"id":"bodyContent"}).findAll("a",																						
					href=re.compile("^(/wiki/)((?!:).)*$")) 
links	=	getLinks("/wiki/Canguru")
while	len(links)	>	0:				
	newArticle	=	links[random.randint(0,	len(links)-1)].attrs["href"]				
	print(newArticle)				
	links	=	getLinks(newArticle)