import sys

vars = {}

def openfile():
    f = open(sys.argv[1], 'r').read()
    f = f.split("\n")
    return f

def openfilepart(start):
    f = open(sys.argv[1], 'r').read()
    f = f.split("\n")
    f[f.index(start):len(f)]
    return f

file = openfile()

def parsein(arg):
    for i in arg:
        if str(i)[0:4] == "echo":
            if ("(" and ")") in i :
                all = i[i.index("(")+1:len(i)]
                all = all[0:all.index(")")]
                all = all.split(";")
                text = ""
                for  j in all:
                    if "\"" in j:
                        append = j[j.index("\"")+1:len(j)]
                        append = append[0:append.index("\"")]
                        append = append.replace("\\n", "\n")
                        text += append
                    else:
                        append = j.replace(" ", "")
                        if append in vars:
                            text += vars[append]
                print(text, end='')
        elif str(i)[0:3] == "let":
            if ("<" and ">") in i:
                name = i[i.index("<")+1:len(i)]
                name = name[0:name.index(">")]
                name = name.replace(" ", "")
                val = ""
                if "=" in i:
                    eq = i.index("=")
                    if ( "[" and "]") in i:
                        if i.index("[") > eq:
                            all = i[i.index("[")+1:len(i)]
                            all = all[0:all.index("]")]
                            all = all.split(";")
                            spaces = ""

                            for j in all:
                                if "\"" in j:
                                    spaces = ""
                                    for i in range(len(j[0:j.index("\"")]) ):
                                        spaces += " "
                                    if j[0:j.index("\"")] != spaces:
                                        if "\"" in j:
                                            string = j[j.index("\"")+1:len(j)]
                                            string = string[0:string.index("\"")]

                                        list = []
                                        list.append(j)
                                        j = parsein(list)
                                        val += j
                                    else:
                                        append = j[j.index("\"")+1:len(j)]
                                        append = append[0:append.index("\"")]
                                        val += append
                                else:
                                    append = j.replace(" ", "")
                            vars[name] = val
        elif str(i)[0:5] == "getin":
            if ("(" and ")") in i:
                if "\"" in i:
                    text = i[i.index("\"")+1:len(i)]
                    text = text[0:text.index("\"")]
                    return input(text)
        elif str(i)[0:2] == "if":
            if ("(" and ")") in i:
                all = i[i.index("(")+1:len(i)]
                all = all[0:all.index(")")]
                print(all)
def parseout(arg):  
    for i in arg:
        if i[0:4] == "func":
            entry = 0
            if "[" in i and "]" in i:
                name = i[i.index("[")+1:len(i)]
                name = name[0:name.index("]")]
            if "(" in i and ")" in i:
                pass
            if name == "__entry__":
                code = openfilepart(i)
                code = code[1:code.index("end")]
                ncode = []
                for j in code:
                    if j[0:4] == "    ":
                        ncode.append(j[4:len(j)])
                
                parsein(ncode)
        if i[0:3] == "let":
            if ("<" and ">") in i:
                name = i[i.index("<")+1:len(i)]
                name = name[0:name.index(">")]
                name = name.replace(" ", "")
                val = ""
                if "=" in i:
                    eq = i.index("=")
                    if ( "[" and "]") in i:
                        if i.index("[") > eq:
                            all = i[i.index("[")+1:len(i)]
                            all = all[0:all.index("]")]
                            all = all.split(";")
                            for j in all:
                                if "\"" in j:
                                    append = j[j.index("\"")+1:len(j)]
                                    append = append[0:append.index("\"")]
                                    val += append
                                else:
                                    append = j.replace(" ", "")
                                    

                try:
                    ret = int(val)
                except:
                    ret = str(val)

                vars[name] = ret

if __name__ == "__main__":
    parseout(file)