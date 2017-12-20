import urllib.request
import chardet
with urllib.request.urlopen(r'http://www.whatismyip.com.tw/') as response:
    html = response.read()
    char = chardet.detect(html)
    print(char)
    html = html.decode(char['encoding'])
    print(html)

