from bs4 import BeautifulSoup
import urllib.request as url
url_domain = 'http://likms.assembly.go.kr'
url_sub = '/bill/billDetail.do?'
url_qstr = 'billId=PRC_F1V9P0I3X2B5A1G0S3O4C1X8B6D0E0'
url_str = url_domain+url_sub+url_qstr
html = url.urlopen(url_str).read()
soup = BeautifulSoup(html, 'html.parser')
txt = soup.find(attrs={'class':'subti01'}).text
print(txt)

