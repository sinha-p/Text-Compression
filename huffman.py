import nodes

hc = []
key = []


def huffman():
    textstr = ""
    try:
        with open("text.txt",'r') as text_file:
            textstr=text_file.read()
        text_file.close()
    except FileNotFoundError:
        print("Sorry no sample file found !!")
    index=0
    c = []
    freq = []
    path = ""
    totalstr=""
    compress = []
    decompress = []

    #   CALCULATION OF DIFFERENT CHARACTERS AND THEIR RESPECTIVE FREQUENCIES
    for i in range(len(textstr)):
        found = 0
        searchtill = index
        for j in range(searchtill):
            if textstr[i] == c[j]:
                freq[j] += 1
                found = 1
        if found == 0:
            c.append(textstr[i])
            freq.append(1)
            index += 1
    print(c)

    #   INSERTING CHARACTERS AND THEIR FREQUENCIES IN LIST
    Myqueue=nodes.MYQueue
    myqueue=Myqueue()
    for i in range(index):
        Myqueue.insert(myqueue, c[i], freq[i])

    #   CREATING HUFFMAN TREE
    while myqueue.size >= 2:
        n1 = Myqueue.removemin(myqueue)
        k1 = n1.getkey()
        v1 = n1.getvalue()
        n2 = Myqueue.removemin(myqueue)
        k2 = n2.getkey()
        v2 = n2.getvalue()
        newnode=Myqueue.insert(myqueue, (k1+k2), (v1+v2))
        newnode.left = n1
        newnode.right = n2
    buildpath(myqueue.header.getnext(), path)

    #   PRINTING KEY AND ITS PATH
    for i in range(len(key)):
        print(key[i]+" "+hc[i])
    for i in range(len(textstr)):
        for j in range(len(key)):
            if textstr[i] == key[j]:
                totalstr += hc[j]
    ts = totalstr
    print(totalstr)
    print(len(totalstr))
    if (len(totalstr)%8) != 0:
        extra = 8-(len(totalstr)%8)
    else:
        extra = 0
    for i in range(extra):
        totalstr += '0'
    try:
        with open("compress.bin","wb") as compressfile:
            for i in range(0, len(totalstr), 8):
                bin=totalstr[i:i+8]
                dec=int(bin, 2)
                compress.append(dec)
            bt=bytes(compress)
            try:
                compressfile.write(bt)
                compressfile.flush()
            except IOError:
                print("Error in writing to the file")
        compressfile.close()
    except Exception:
        print("Some exception occured during compress file creation !!")

    with open("compress.bin", "rb") as f:
        byte = f.read(1)
        while byte:
            decompress.append(int.from_bytes(byte, byteorder='little'))
            byte = f.read(1)
    decode(decompress, extra, newnode)

# FUNCTION TO BUILD PATH OF 0s AND 1s FOR DIFFERENT ELEMENT PRESENT IN THE FILE


def buildpath(root, path):
        if root.left is not None:
            buildpath(root.left, path+"0")
        if root.right is not None:
            buildpath(root.right, path+"1")
        if root.left is None and root.right is None:
            hc.append(path)
            key.append(root.getkey())

#FUNCTION TO DECOMPRESS THE COMPRESSED FILE


def decode(decompress, extra, header):
    decodedstr = ""
    for i in range(len(decompress)):
        bin='{0:08b}'.format(decompress[i])
        decodedstr += bin
    decodes = decodedstr[0:(len(decodedstr)-extra)]
    dstr = ""
    temp = header
    for i in range(len(decodes)):
        if temp.right == None and temp.left == None:
          dstr += temp.getkey()
          temp = header
        if decodes[i] == '0':
            temp = temp.left
        elif decodes[i] == '1':
            temp = temp.right
    dstr += temp.getkey()
    try:
        with open("decode.txt",'w') as decodef:
            decodef.write(dstr)
    except FileNotFoundError:
        print("File not found !!")


if __name__ == "__main__":
    huffman()
