import sys
import os

class l:
    kmain = ""
class g:
    bootloader = "bits 32\n\nextern _kmain\ncall _kmain\n\ntimes (510-($-$$)) db 0\ndw 0xAA55"

fname = sys.argv[1].replace(".tea", "")
binname = sys.argv[1].replace(".tea", ".bin")
kname = sys.argv[1].replace(".tea", ".c")
bname = sys.argv[1].replace(".tea", ".s")

def openfile():
    f = open(sys.argv[1], 'r').read()
    f = f.split("\n")
    return f

def openfilepart(start):
    f = open(sys.argv[1], 'r').read()
    f = f.split("\n")
    f[f.index(start):len(f)]
    return f

def filegen():
    try:
        os.mkdir(fname)
        os.chdir(fname)
    except:
        os.chdir(fname)

    kernel = "#include \"teaos.h\"\n\nvoid kmain()\n{\n" + l.kmain + "}"

    kernelfile = open(kname, 'w')
    kernelfile.write(kernel)
    kernelfile.close()

    bootfile = open(bname, 'w')
    bootfile.write(g.bootloader)
    bootfile.close()



def parse(ncode):
        for i in ncode:
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
                            text += append
                        else:
                            append = j.replace(" ", "")
                            if append in vars:
                                text += vars[append]
                    l.kmain += "    print((char *)\"" + text + "\");\n"

if __name__ == "__main__":
    parse(openfile())
    filegen()