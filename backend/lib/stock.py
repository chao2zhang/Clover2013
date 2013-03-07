# Ref: http://www.cnblogs.com/kingwolfofsky/archive/2011/08/14/2138081.html

import urllib2

# Shanghai market only
sinaurl = 'http://hq.sinajs.cn/list=sh%s'

def stock(id):
    url = sinaurl % str(id)
    request = urllib2.Request(url)
    u = urllib2.urlopen(request)
    result = u.read().strip()
    st = result.find('=')
    info = eval(result[st+1:-1]).split(',')
    return float(info[3])
    

# print stock(601006)

