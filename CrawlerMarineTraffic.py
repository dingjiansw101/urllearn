import urllib.request
import chardet
import re
from urllib import request
from urllib import error
import time


visitedurls = set()

harbor_coordinates = {}

baseurl = r'https://www.marinetraffic.com'

def current_port_urls(url):
    html = get_html(url)
    if html == None:
        return []
    pattern = re.compile(r'"(/en/ais/details.*?):(.*?)"')

    results = re.findall(pattern, html)

    outurls = {result[1]:(baseurl + result[0] + ':' + result[1]) for result in results}

    #outurls = list(map(lambda x:(baseurl + '/' + x), urls))
    return outurls

def get_html(url):
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'

    print('url in get_html:', url)
    req = request.Request(url, headers=head)
    try:
        response = request.urlopen(req)
        html = response.read()
        char = chardet.detect(html)
        html = html.decode(char['encoding'])
        #print('html in get_html"', html)
        return html
    except error.HTTPError as e:
        print(e.reason)

def parse_marine(html):
    #pattern = re.compile(r'Latitude.*?Longitude:.*?<b>([-]*[0-9]+.[0-9]+).*?([-]*[0-9]+.[0-9]+)</b>', re.DOTALL)
    #print('html:', html)
    #pattern = re.compile(r'Latitude.*?Longitude:.*?\n.*?<b>([-]*[0-9\.]+).*?([-]*[0-9\.]+)</b>')
    pattern = re.compile(r'Latitude.*?Longitude:.*?\n.*?<b>([-]*[0-9\.]+).*?([-]*[0-9\.]+).*?</b>')
    #pattern = re.compile(r'Latitude.*?Longitude:.*?<b>.*?</b>', re.DOTALL)
    coordinate = re.findall(pattern, html)
    if (len(coordinate) == 0):
        return -1
    return coordinate
def extract_coord(url):
    html = get_html(url)
    #print('html: ', html)
    coordinate = parse_marine(html)
    #return coordinates
    print('coordinate:', coordinate)
    if (coordinate != -1):
        return coordinate
        #harbor_coordinates.append(coordinate)

def search():
    ## max num to be 1931
    outdir = r'/home/dingjian/code/urllearn/harbor_coordinates4.txt'
    with open(outdir, 'a') as f_out:
        for i in range(160, 1931):
            url = baseurl + '/en/ais/index/ports/all/page:' + str(i + 1)
            ports_urls = current_port_urls(url)
            for port_name in ports_urls:
                time.sleep(5)
                print('port name:', port_name)
                port_url = ports_urls[port_name]
                print('port url:', port_url)
                coord = extract_coord(port_url)
                harbor_coordinates[port_name] = coord
                outline = port_name + ' ' + str(coord[0][0]) + ' ' + str(coord[0][1])
                f_out.write(outline + '\n')
def testparse_coord():
    url = r'https://www.marinetraffic.com/en/ais/details/ports/309/China_port:TIANJIN'
    coord = extract_coord(url)
    print('coord: ', coord)

if __name__ == '__main__':
    #extract_coord()
    # url = r'http://gangkou.zou114.com/gk_cupre.html'
    # extract_coord(url)

    #start_url = r'https://www.marinetraffic.com/en/ais/index/ports/all/page:1'
    search()
    print('harbor_coordinates:', harbor_coordinates)
    #testparse_coord()