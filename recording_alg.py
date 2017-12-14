import math
import random
import sys

"""
    wmax(k) is the largest integer w <= WMAX such that two conditions are satisified:
    1. di < k,
    2. pw(k) in Dw'

    Parameters
    ----------
    k : int
        an integer k to be represented in random representation
    WMAX : int
        WMAX is the integer calculate from get_WMAX(D)

    Returns
    -------
    int
        an integer that satisifies the two coniditons for wmax(k)
"""
def wmax(k, Wn, D):
    w = Wn + 2;
    for i in range(Wn + 2, 1, -1):
        d_flag = True;
        Dw_neg = get_Dw_Neg(D, i);
        # check the first candidate where di \in D < k
        for d in D:
            if d >= k:
                d_flag = False;
                break;
        # If condition 1 is not satisified, choose another w
        if d_flag == False:
            continue;

        if (pw(k, i) in Dw_neg):
            w = i;
            break;
    return w;



# pw(k) = k % (2**w)
def pw(k, w):
    return k % (2**w);

"""
    Calculcate the set D_w

    Parameters
    ----------
    arg1 : List
        set of odd integers
    arg2 : int
        an integer >= 2

    Returns
    -------
    List
        a list that contains Dw which is pw(d) for each d in D
"""
def get_Dw(D, w):
    Dw = [];
    for d in D:
        Dw.append(pw(d, w))
    Dw.sort();
    return Dw;

"""
    Calculcate the set D_w' by using Dw

    Parameters
    ----------
    arg1 : List
        set of odd integers
    arg2 : int
        an integer >= 2

    Returns
    -------
    List
        a list that contains Dw and Dw_Neg
"""
def get_Dw_Neg(D, w):
    Dw = get_Dw(D, w);
    Dw_Neg = [];
    const = 2**w;
    for d in Dw:
        Dw_Neg.append(const - d);

    # get the union of Dw and Dw_Neg
    result = list(set().union(Dw, Dw_Neg));
    result.sort(); # sort the array
    return result


def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)));

def digitD(k, D):
    if k % 2 == 0:
        return 0;
    if k == 1:
        return k;
    Wn = get_Wn(D);
    Wmax = wmax(k, Wn, D);
    Dwmax = get_Dw(D, Wmax);
    result = -100;
    flag_cond1 = False;
    if pw(k, Wmax) in Dwmax:
        for d in D:
            if d >= k:
                continue;
            if pw(k, Wmax) == pw(d, Wmax):
                result = d;
                # this flag is to check if it's need to go and check the other condition.
                flag_cond1 = True;
                break;
        if flag_cond1:
            return result;

    if (2**Wmax - pw(k, Wmax)) in Dwmax:
        for d in D:
            if d >= k:
                continue;
            if (2**Wmax - pw(k, Wmax)) == pw(d, Wmax):
                result = -d;
        return result;
    print Wmax
    print Dwmax
    print "no condition"


def RDP(k, D):
    bin_k = []; # binary representation of k to contain the result
    while k != 0:
        ki = digitD(k, D);
        bin_k.insert(0, ki);
        k = (k - ki) / 2;

    return bin_k;


def generate_random_D(m, l):
    if l > (m+1)/2:
        raise ValueError("l should satisfy the condition l <= (m+1)/2");
    D = [];
    for i in range(2, l+1, 1):
        odd = False;
        while not odd:
            x = random.randint(3, m);
            if(x % 2 != 0 and x not in D):
                odd = True;
        D.append(x);
    D.sort();
    return D;

if __name__ == '__main__':
    k = int(sys.argv[1]);
    m = int(sys.argv[2]);
    l = int(sys.argv[3]);
    D = generate_random_D(m, l);
    D.insert(0, 1);
    print "D = ", D, ", n = ", len(D);
    result = RDP(k, D);
    print result;
    print "Length => ", len(result)
