def rgb(r, g, b):
    if r>255:
        r=255
    elif r<0:
        r=0
    r=f'{r:X}'
    if len(r)<2:
        r='0'+r
    if g>255:
        g=255
    elif g<0:
        g=0
    g=f'{g:X}'
    if len(g)<2:
        g='0'+g
    if b>255:
        b=255
    elif b<0:
        b=0
    b=f'{b:X}'
    if len(b)<2:
        b='0'+b
    return r+g+b