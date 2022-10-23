import sys

def openfile():
    f = open(sys.argv[1], 'r').read()
    f = f.replace("\n", "")
    f = f.split(";")
    return f

file = openfile()

def parse(arg):
    for i in arg:
        if i[0:7] == "whistle":
            if "\"" in i:
                text = i[i.index("\"")+1:len(i)]
                text = text[0:text.index("\"")]
                text = text.replace("\\n", "\n")
                print(text, end='')

if __name__ == "__main__":
    parse(file)