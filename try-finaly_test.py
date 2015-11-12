f = open('log.txt','w')
try:
    f.write('logging start')
    f.write('\r\n')
finally:
    f.close()