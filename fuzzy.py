import subprocess

def run(data):
    path = '/usr/bin/curl'
    args = '--url'
    try:
        ps = subprocess.check_output([path, args ,data])
        ps.wait()
    except Exception, e:
        #print e.returncode
        if (e.returncode == -11):
            f.write ("overflow@:\n")
            f.write (data)
            f.write ("\n")
        else:
            pass
#def makejunk():
#    random.randint(1, 1000)

if __name__ == "__main__":
    f = open('seglog', 'w') 
    junk = "A"
    for x in range(0,100000):  
        junk += "A"
        run(junk)
    f.close()
