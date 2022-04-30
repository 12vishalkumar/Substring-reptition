import re
st = input()
mt = re.search(r'([0-9A-Za-z])\1+', st)
if(mt):
    print(mt.group(1))
else:
    print(-1)
