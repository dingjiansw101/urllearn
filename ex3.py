from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    Form_Data = {}
    Form_Data['i'] = 'jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1513340530750'
    Form_Data['sign'] = '7edfdd1fc8332c3347a6820b6e1f2818'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTION'

    data = parse.urlencode(Form_Data).encode('utf-8')

    response = request.urlopen(url, data)

    html = response.read().decode('utf-8')

    translate_results = json.loads(html)

    print(translate_results)
    #translate_results = translate_results['']