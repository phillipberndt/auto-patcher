import sys,os,re
 
rx = re.compile('^diff -Npru.*/(.*)\.(java|aidl)$')
 
patches = [ 'frameworks' ]
 
for p in patches:
    name_in = p + '.diff'
    fmt_name_out = p + '_%d_%s.diff'
   
    fin = open(name_in, 'rb')
    i = 0
    fout = None
    for l in fin.readlines():
        m = rx.match(l)
        if m:
            name_out = fmt_name_out % (i, m.group(1))
            print "Creating: '%s'" % name_out
            fout = open(name_out, 'wb')
            i += 1
 
        if i > 0:
            fout.write(l)
   
    try:
        fin.close()
        fout.close()
    except:
        pass
