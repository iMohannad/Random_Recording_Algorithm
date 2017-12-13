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
    return Dw.sort();

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
