import sys
import time
import l_naf
import revisited_rdr
import bit_wise_rdr

# m is the upper bound of random digit set
# l is the length of the digit set
def ifrdr_test(k, m, l):
    # generate a random digit set
    D = bit_wise_rdr.generate_random_D(m, l)
    startTime = time.time()
    [rdr, min_length] = bit_wise_rdr.RDR_algorithm(D, k)
    endTime = time.time()
    return endTime - startTime

# m is the upper bound of random digit set
# l is the length of the digit set
def rdr_test(k, m, l):
    # generate a random digit set
    D = revisited_rdr.generate_random_D(m, l)
    startTime = time.time()
    rdr = revisited_rdr.RDP(k, D)
    endTime = time.time()
    return endTime - startTime

def wnaf_test(k, w):
    D = l_naf.generate_naf(w)
    startTime = time.time()
    naf = l_naf.find_naf(k, 2, w)
    endTime = time.time()
    return endTime - startTime

def main():
    k = [651056770906015076056810763456358567190100156695615665659,
        2695995667150639794667015087019625940457807714424391721682712368051,
        115792089210351248362697456949407573528996955234135760342422159061068512044339,
        26959956671506397946670150870196259404578077144243917216827126959956671506397946670150870196259404578077144243917216,
        2695995667150639794667015087019625940457807714424391721682712368058238947189273490172349807129834790127349087129834623486127461012630462184628923461201280461]
    time_test = 0;
    time_res = [0, 0, 0]
    index = 0
    while index < 5:
        i = 5
        time_res = [0, 0, 0]
        while i > 0:
            # print i
            # time_res[0] = time_res[0] + ifrdr_test(k[index], 1023, 512)
            time_res[1] = time_res[1] + rdr_test(k[index], 1023, 512)
            # time_res[2] = time_res[2] + wnaf_test(k[index], 11)
            i = i - 1
        print "------------------------------- ", k[index]
        print "IFRDR > ", time_res[0]/5
        print "RDR > ", time_res[1]/5
        print "wNAF > ", time_res[2]/5
        index = index + 1


if __name__ == '__main__':
    main()

