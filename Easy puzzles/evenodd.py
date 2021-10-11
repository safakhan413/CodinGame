def foo(l):
    for i,v in enumerate(l):
        if i%2 == 0:
            l[i] = v+1
        else:
            l[i] = v-1
    return l


print(foo([10, 10, 10, 10, 10]))