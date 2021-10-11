# 0 6 * * * task update_ptkey.py

import os
print(os.environ['JD_WSKEY'])

from ws2ptkey import genToken
res = []
for i in os.environ['JD_WSKEY'].split('&'):
    res.append(genToken(i))
#print('updated', res)

#os.environ['JD_COOKIE']= '&'.join(res)
text = ('export JD_COOKIE="{}"'.format('&'.join(res)) )
ws = 'export JD_WSKEY="{}"'.format(os.environ['JD_WSKEY'])

print(text)
with open('/ql/config/env.sh','w') as f:
    f.write(text+'\n'+ws)
