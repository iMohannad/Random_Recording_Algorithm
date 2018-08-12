import sys
sys.path.append('../Python')

from fractions import Fraction
import IFRA
import revisited_rdr


def testDesnity(k):
    i = 5
    rdr = 0
    ifrdr = 0
    [rdr_num, rdr_dom] = [0, 0]
    [ifrdr_num, ifrdr_dom] = [0, 0]
    while i <= 50:
        D = IFRA.generate_random_D(i*6, i)
        rdr = revisited_rdr.RDP(k, D)
        ifrdr = IFRA.RDR_algorithm(D, k)
        [rdr_num, rdr_dom] = revisited_rdr.average_density(rdr)
        [ifrdr_num, ifrdr_dom] = IFRA.average_density(ifrdr)
        avg_den_rdr = float(rdr_num)/rdr_dom
        avg_den_ifrdr = float(ifrdr_num)/ifrdr_dom
        # print "RDR > ", rdr
        # print "IFRA > ", ifrdr
        print "Digit set = ", D
        print "RDR = ", rdr_num, "/", rdr_dom
        print "IFRA = ", ifrdr_num, "/", ifrdr_dom
        print "D_length = ", len(D), ", RDR = ", Fraction(avg_den_rdr).limit_denominator(), " = ", avg_den_rdr, ", IFRA = ", Fraction(avg_den_ifrdr).limit_denominator(), " = ", avg_den_ifrdr,"\n"
        i = i + 1



if __name__ == "__main__":
    k = 651056770906015076056810763456358567190100156695615665659
    w = [7, 9 , 11]
    testDesnity(k)
    # D = [1, 3, 23, 27]
    # rdr = revisited_rdr.RDP(k, D)
    # ifrdr = IFRA.RDR_algorithm(D, k)
    # [rdr_num, rdr_dom] = revisited_rdr.average_density(rdr)
    # [ifrdr_num, ifrdr_dom] = IFRA.average_density(ifrdr)
    # avg_den_rdr = float(rdr_num)/rdr_dom
    # avg_den_ifrdr = float(ifrdr_num)/ifrdr_dom
    # # print "RDR > ", rdr
    # # print "IFRA > ", ifrdr
    # print "k_rdr > ", IFRA.check_num(rdr)
    # print "k_ifrdr > ", IFRA.check_num(ifrdr)
    # print "Digit set = ", D
    # print "RDR = ", rdr_num, "/", rdr_dom
    # print "IFRA = ", ifrdr_num, "/", ifrdr_dom
    # print "D_length = ", len(D), ", RDR = ", Fraction(avg_den_rdr).limit_denominator(), " = ", avg_den_rdr, ", IFRA = ", Fraction(avg_den_ifrdr).limit_denominator(), " = ", avg_den_ifrdr,"\n"
        