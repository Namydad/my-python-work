for a in range(a, num):
    if a % num == 0:
        print('not prime')
        break
else: # loop not exited via break
    print('prime')