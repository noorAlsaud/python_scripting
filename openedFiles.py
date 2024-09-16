files = []
for i in range(10000):
    files.append(open("someText.txt", 'r'))
    print(i)

    # RESULT AN ARROR : TOO MANY OPEN FILES IN INDEX #8188