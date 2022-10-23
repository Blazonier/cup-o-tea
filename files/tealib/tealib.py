print("TEA-LIB v0")

class list:
    def fill(mode, positions):
        if mode == "index":
            list = []
            for i in range(int(positions)):
                list.append(int(i))
        elif mode == "number":
            list = []
            for i in range(int(positions)):
                list.append(int(i) + 1)
        else:
            print("TEA-LIB.list.fill -> mode argument must be 'index' or 'number'")
        try:
            return list
        except:
            pass
    def sort(mode, list):
        if mode == "int":
            return sorted(list)
        else:
            print("TEA-LIB.list.sort -> mode argument must be 'int'")