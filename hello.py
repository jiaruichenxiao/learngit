#hello.py

def application(environ, start_response):
    start_response('200 OK' , [('Content-Type','text/html')])
    body='<hl>Hello,%s!</hl>'%(environ['PATH_INFO'][2:]or 'web')#PATH_INFO是从/后的字符算起，1：就是从第一个到最后，2：就是从第二个到最后。
    return [body.encode('gbk')]