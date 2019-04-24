def is_chinese(uchar):
    if uchar >= '\u4e00' and uchar <= '\u9fff':
        return True
    else:
        return False


try:
    while 1:
        s = input()
        h = 0
        for i in s:
           if is_chinese(i):
               h += 1
        print(h) 
except:
    pass
