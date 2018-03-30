#this file provide absolutely moving file VAL.h to folder


extend =['h']

found ={x :[]for x in extend}
for name in files:
    ext =  name.lower().rsplit(".",1)[-1]