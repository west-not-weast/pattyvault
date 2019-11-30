from bs4 import BeautifulSoup
import requests

#URL = "https://spongebob.fandom.com/wiki/List_of_transcripts"
#r = requests.get(URL)
#soup = BeautifulSoup(r.content,'html5lib')
#links = soup.find_all("a", string="View transcript")
#for link in links:
#  homepage = "https://spongebob.fandom.com/"
#  href = link.get('href')
#  if href is not None:
#  	with open('transcript_urls.txt', 'a') as transcript_urls:
#      transcript_urls.write(homepage + href + '\n')

with open("transcript_urls.txt") as f:
    urls = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
urls = [x.strip('\n') for x in urls] 
for url in urls:
  epname = url[35:-11]
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html5lib')
  epnum = "-1"
  epnumanchor = soup.find("a", string="[edit]")
  if epnumanchor is not None:
    epnum = epnumanchor.get('href')[51:-12]
  transcriptul = soup.find("ul", attrs={'class': None})
  if transcriptul is not None:
    transcript = transcriptul.contents
    tstring = ""
    for line in transcript:
            tstring += line.text.encode("utf-8")
    with open("sb-transcripts\\" + epname + ".trans", 'a') as transfile:
            f = epname + '\n' + epnum + '\n'
            transfile.write(f.encode('utf-8') + tstring)
	
## print(homepage + href) ##
## print(soup.prettify().encode("utf-8")) ##