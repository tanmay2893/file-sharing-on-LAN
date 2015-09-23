from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from helper import SimpleHTTPRequestHandler,set_directory
import os,urllib,urllib2
from easygui import *
import socket
'''
print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip=s.getsockname()[0]
s.close()
nick=raw_input('Enter your nick\n')
msgbox("Select the directory in which excel sheet will be saved or is already present")
d=diropenbox()
print d
def run():
    global ip, nick
    print('http server is starting...')
 
    #ip and port of server
    #by default http server port is 80
    server_address = ('', 80)
    set_directory(d)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    try:
        urllib2.urlopen('http://localhost:3000/nick/'+nick)
    except:
        print 'not found'
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
