import os

os.system("pip3.4 install --user PrettyTable")

os.system('python asia.py  --evidence dysp=1  --query tub lung bron  --exact')

os.system('python asia.py  --evidence dysp=1  --query tub lung bron  --exact --gibbs -N 10000')

os.system('python asia.py  --evidence xray=1 dysp=0  --query tub lung bron  --exact')

os.system('python asia.py  --evidence xray=1 dysp=0  --query tub lung bron  --exact --gibbs -N 10000')

os.system('python asia.py  --evidence xray=1 dysp=0  --query tub lung bron  --exact --gibbs -N 10000 --ent')

os.system('python asia.py  --evidence xray=1 dysp=0  --query tub lung bron  --exact --gibbs -N 200000 --ent')
