import urllib.request;
from bs4 import BeautifulSoup


def read_url(link: str):
  f = urllib.request.urlopen(link)
  myfile: str = f.read().decode('utf-8')
  return myfile


start = 4421
end = 5125

for page in range(end - start):
  page_url = f'https://makedonski.gov.mk/corpus?strana={page+start}'
  # print(f'Page {page_url}')
  data = read_url(page_url)
  soup = BeautifulSoup(data, 'html.parser')

  # print(soup)
  for item in soup.select('.content-title strong'):
    print(item.string)
