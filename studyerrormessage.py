x = '2'
f = open('log.txt','a')
try:
    r = 1 + x
    print r
except Exception, e:
    f.write(str(e) + ': Error \r\n')
f.close()
