import sys

def generate_naf(w):
    naf_set = []
    naf_set.append(1)
    i = 3
    while (i <= (2**(w-1))):
        naf_set.append(i)
        i = i + 2;
    return naf_set
    
def find_naf(k, l, w):
    i = 0
    ki = -7
    result = []
    while k > 0:
        if (k % l) != 0:
            ki = k % (l**w)
            if ki > ((l**w)/2):
                ki = ki - (l**w)
            k = k - ki
        else:
            ki = 0
        k = k/l
        result.append(ki)
    result.reverse()
    return result



if __name__ == '__main__':
    y = generate_naf(int(sys.argv[3]))
    print y
    print len(y)
    x = find_naf(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]));
    x.reverse()
    print x
    print bin(int(sys.argv[1]))
