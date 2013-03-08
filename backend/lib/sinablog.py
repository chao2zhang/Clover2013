
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'python-blogger'))

import pyblog

sinalurl = 'http://upload.move.blog.sina.com.cn/blog_rebuild/blog/xmlrpc.php'

def postblog(title, content, username, password):
    post = {'title': title, 'description': content}
    blog = pyblog.MetaWeblog(sinalurl, username, password, None)
    return blog.new_post(post, True)

