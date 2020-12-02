

def t_args(**kwargs):

    for key, value in kwargs.items():
        print ("%s == %s" % (key, value))

def h(x, a, n):
    print(f'{a} {n}')

    return 4 + x + a + n


def g(x, a, n):

    print(f'{a} {n}')

    return x + a + n


if __name__ == '__main__':
    argsh = {'a': 3, 'n': 4}
    argsg = {'a': 3, 'n': 4}
    t_args(a=argsh.get('a'), n=argsh.get('n'))

    hh = {'f': 'h', 'args': argsh}
    gg = {'f': 'g', 'args': argsg}

    pipeline = [hh, gg]


    h(0, a=argsh.get('a'), n=argsh.get('n'))

    locals()['h'](0, a=argsh.get('a'), n=argsh.get('n'))


    x = 1
    '''
    for p in pipeline:
        x = locals()[p['f']](x, a=p['args'].get('a'), n=argsh.get('n'))
    '''

    [locals()[p['f']](x, a=p['args'].get('a'), n=argsh.get('n')) for p in pipeline]

    print(x)

     # http://www.apc.univ-paris7.fr/~lejeune/pipelet/html/tutorial.html