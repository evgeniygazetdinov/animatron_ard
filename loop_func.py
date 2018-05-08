# one love
loop = [i for i in range(30,100,1)]


def limiter_for_switcher(loop,keys):
    while len(loop) != keys:
        if len(loop)>keys:
            del loop[-1]
            print(loop)
            print(len(loop))
        if len(loop)< keys:
            for item in loop:
                loop.append(loop[item])
                if len(loop) == keys:
                    print(loop)
                    print(len(loop))
                    break
        return loop




limiter_for_switcher(loop,1000)
