def readFile(file_name):
    raws_file_name = '%r' %file_name
    f = open(raws_file_name[1:-1], 'r')
    line = f.readline()
    f.close()
    return line