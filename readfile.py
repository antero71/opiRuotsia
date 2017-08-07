
def readFile(file_name):
    file = open(file_name,'r',encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines
