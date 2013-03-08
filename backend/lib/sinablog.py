
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'python-blogger'))

import pyblog

sinalurl = 'http://upload.move.blog.sina.com.cn/blog_rebuild/blog/xmlrpc.php'

def postblog(username, password):
    blog = pyblog.MetaWeblog(sinalurl, username, password, None)
    blog.new_post()
