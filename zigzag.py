import time, sys, random
indent = 0
indentIncreasing = True

try:
    while True:
     print(' ' * indent, end = ' ')
     print('*******')
     time.sleep(0.1)
     
     if indentIncreasing:
      indent = indent + 1
      randNum = random.randrange(3,15)
      #print(randNum)
      if indent == randNum-1 or indent == randNum:
       indentIncreasing = False
     else:
      indent = indent - 1
      if indent == 0:
       indentIncreasing = True
except KeyboardInterrupt:
 sys.exit()