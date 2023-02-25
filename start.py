print("Please, select:")
print("1: WORKER:")
print("2: SECRET: UNAVAIABLE")
WhatAreYouNeed = int(input())
if WhatAreYouNeed == 1:
    exec(open("worker.py").read())
elif WhatAreYouNeed == 2:
    print("UNAVAIABLE")
else:
    print("Shutdown.")