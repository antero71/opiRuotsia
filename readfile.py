def readFile(file_name):
    file = open(file_name,"r")
    lines = file.readlines()
    file.close()
    return lines
