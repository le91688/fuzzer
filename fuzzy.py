import subprocess

def run(data):
    path = '/somepath/to/something/'
    args = '--somearg'
    try:
        ps = subprocess.check_output([path, args ,data])
        ps.wait()
    except Exception, e:
        if (e.returncode == -11):
            f.write ("overflow@:\n")
            f.write (data)
            f.write ("\n")
        else:
            pass

if __name__ == "__main__":
    f = open('seglog', 'w') 
    junk = "A"
    for x in range(0,100000):  
        junk += "A"
        run(junk)
    f.close()
