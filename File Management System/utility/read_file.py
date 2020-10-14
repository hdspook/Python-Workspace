def readFile(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    f.close()
    return line