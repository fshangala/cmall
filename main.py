import sys, lzma
from rich import print

def compress(*args):
    filepath = args[2]
    with open(filepath,"rb") as sourcefile:
        data = sourcefile.read()
        with lzma.open("compressed.xz","wb") as destfile:
            destfile.write(data)

def decompress(*args):
    filepath = args[2]
    with lzma.open(filepath,"rb") as sourcefile:
        data = sourcefile.read()
        with open("decompressed.zip","wb") as destfile:
            destfile.write(data)
    

args = sys.argv
if len(args) != 3:
    print("2 arguments required (type,filepath)")
    exit()

if args[1] == 'compress':
    compress(*args)
elif args[1] == 'decompress':
    decompress(*args)
