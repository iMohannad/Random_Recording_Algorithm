def wmax(k, WMAX, D):
    w = WMAX;

    for i in range(WMAX + 2, -1, 1):
        d_flag = True;
        # check the first candidate where di \in D < k
        for d in D:
            if d >= k:
                d_flag = False;
                break;
        # If condition 1 is not satisified, choose another w
        if d_flag == False:
            continue;

        if pw(k, w):
            pass


def pw(k, w):
    return k % (2**w);


def get_Dw(D, w):
    Dw = [];
    for d in D:
        Dw.append(pw(d, w))
    return Dw.sort();
