from random import randint
high= 50
buzz=0
while(True):
      temp= randint(0,100)
      hum= randint(0,100)
      if (temp>=high):
            buzz=1
      else:
            buzz=0
