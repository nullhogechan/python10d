x = 2
f = open('log.txt','a')
try:
    r = 1 + x
    print r
except:
    f.write('Error \r\n')
f.close()