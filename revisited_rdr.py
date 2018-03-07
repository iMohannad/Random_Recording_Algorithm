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
        d_flag = False;
        D_neg = get_D_neg(D, i);
        D_pos = get_D_pos(D, i);
        print "------------ WMAX = ", i, " ----------------"
        print "D_pos_", i, " = ", D_pos
        print "D_neg_", i, " = ", D_neg

        # # check the first candidate where di \in D < k
        # for d in D:
        #     if d < k:
        #         d_flag = True;
        #         break;
        # If condition 1 is not satisified, choose another w
        # if d_flag == False:
        #     continue;

        Dw = get_Dw(D, i);
        print "Dw_", i, " = ", Dw;
        print "pw(", k, ", ", i, ") = ", pw(k, i);
        if (pw(k, i) in Dw):
            w = i;
            break;
        print "--------------------------------------------"
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
def get_D_pos(D, w):
    D_pos = [];
    for d in D:
        entry = pw(d, w)
        if (entry not in D_pos):
            D_pos.append(pw(d, w))
    D_pos.sort();
    return D_pos;

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
def get_D_neg(D, w):
    D_pos = get_D_pos(D, w);
    Dw_Neg = [];
    const = 2**w;
    for d in Dw:
        Dw_Neg.append(const - d);

    Dw_Neg.sort();
    return Dw_Neg;

# Get the union of D+ and D-
def get_Dw(D, w):
    D_pos = get_D_pos(D, w);
    D_neg = get_D_neg(D, w);
    result = list(set().union(D_pos, D_neg));
    result.sort();
    return result;

def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)));

def digitD(k, D):
    if k % 2 == 0:
        return 0;
    if k == 1:
        return k;
    Wn = get_Wn(D);
    h = wmax(k, Wn, D);
    D_pos = get_D_pos(D, h);
    D_neg = get_D_neg(D, h);
    print "D_neg = ", D_neg;
    result = -100;
    flag_cond1 = False;
    if pw(k, Wmax) in Dwmax:
        for d in D:
            if d >= k:
                continue;
            print "pw(k, Wmax) > ", pw(k, Wmax), "pw(d, Wmax) > ", pw(d, Wmax)
            if pw(k, Wmax) == pw(d, Wmax):
                result = d;
                # this flag is to check if it's need to go and check the other condition.
                flag_cond1 = True;
                break;
        if flag_cond1:
            print result;
            return result;

    print "2**Wmax - pw(", k, ", Wmax) > ", (2**Wmax - pw(k, Wmax))
    if (2**Wmax - pw(k, Wmax)) in Dwmax:
        for d in D:
            if d >= k:
                continue;
            print "pw(k, Wmax) > ", pw(k, Wmax), "2**Wmax - pw(d, Wmax) > ", (2**Wmax - pw(d, Wmax))
            if (2**Wmax - pw(k, Wmax)) == pw(d, Wmax):
                print d;
                result = -d;
                break;
        return result;
        
    print Wmax
    print Dwmax
    print "2**Wmax ", 2**Wmax
    print "pw(k, Wmax) ", pw(k, Wmax)
    print "2**Wmax - pw(k, Wmax = ", 2**Wmax - pw(k, Wmax)
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

""" To run the program, you need to input 3 values,
    k: The number to be converted
    m: it's an upper bound for the set of numbers where the set D will be generated from
       so, if m = 10 it means, D will be generated from the set [1, 2 .... 10]
    l: The number of elements in the set D.

    Running the program from a terminal as follows:
    python recording_alg.py k m l   (Where k, m, and l are numbers)
"""
if __name__ == '__main__':
    # k = int(sys.argv[1]);
    # m = int(sys.argv[2]);
    # l = int(sys.argv[3]);
    # D = generate_random_D(m, l);
    k = 39;
    D = [3, 23, 27, 53, 61, 71, 79, 97];
    # D = [3, 23, 27]
    D.insert(0, 1);
    print "D = ", D, ", n = ", len(D);
    result = RDP(k, D);
    print result;
    print "Length => ", len(result)
