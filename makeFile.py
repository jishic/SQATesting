# -*- coding:UTF-8 -*-

def changeFile(file):
    filedata = ""
    with open(file,"r") as f:
        for line in f:
            if ";" in line:
                line = line.replace(";",";\n")
            else if "{" in line:
                line = line.replace("{","{\n")
            else if "}" in line:
                line = line.replace("}","}\n")
            filedata+=line
    with open(file,"w") as f:
        f.write(filedata)

if __name__ == '__main__':
    changeFile()
