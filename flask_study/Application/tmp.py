from functools import wraps


def post(*args,**kwargs):
    print(args)
    print(kwargs)



post(1,2,3,4,5,6,num=1,name="lili")