import random
from threading import timer

with open("BETTING/fixtures.txt", "r") as fix:
    fixtures=fix.readlines()
for fixture in fixtures:
    m=""
    n=fixture.replace("vs",f"{m:20}")
    t=(5,print(n))
    t.start()
