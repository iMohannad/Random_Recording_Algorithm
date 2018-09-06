import sys
sys.path.append('../Python')

from fractions import Fraction
import IFRA
import IFRA_positive
import revisited_rdr


def testDesnity(K):
    i = 5
    rdr = 0
    ifrdr = 0
    ifrdrold = 0
    [rdr_num, rdr_dom] = [0, 0]
    [ifrdr_num, ifrdr_dom] = [0, 0]
    [ifrdrold_num, ifrdrold_dom] = [0, 0]
    while i <= 50:
        total_avg_den_rdr = 0
        total_avg_den_ifrdr = 0
        total_avg_den_ifrdrold = 0
        count = 0
        j = i
        while count < j:
            avg_den_rdr = 0
            avg_den_ifrdr = 0
            avg_den_ifrdrold = 0
            count = count + 1
            D = IFRA.generate_random_D(300, i)
            for k in K:
                rdr = revisited_rdr.RDP(k, D)
                ifrdr = IFRA.RDR_algorithm(D, k)
                ifrdrold = IFRA_positive.RDR_algorithm(D, k)
                [rdr_num, rdr_dom] = revisited_rdr.average_density(rdr)
                [ifrdr_num, ifrdr_dom] = IFRA.average_density(ifrdr)
                [ifrdrold_num, ifrdrold_dom] = IFRA_positive.average_density(ifrdrold)
                avg_den_rdr = avg_den_rdr + float(rdr_num)/rdr_dom
                avg_den_ifrdr = avg_den_ifrdr + float(ifrdr_num)/ifrdr_dom
                avg_den_ifrdrold = avg_den_ifrdrold + float(ifrdrold_num)/ifrdrold_dom
            total_avg_den_rdr = total_avg_den_rdr + avg_den_rdr/len(K)
            total_avg_den_ifrdr = total_avg_den_ifrdr + avg_den_ifrdr/len(K)
            total_avg_den_ifrdrold = total_avg_den_ifrdrold + avg_den_ifrdrold/len(K)
        # print "RDR > ", rdr
        # print "IFRA > ", ifrdr
        avg_den_rdr = total_avg_den_rdr/j
        avg_den_ifrdr = total_avg_den_ifrdr/j
        avg_den_ifrdrold = total_avg_den_ifrdrold/j
        print "Digit set = ", D
        print "RDR = ", rdr_num, "/", rdr_dom
        print "IFRA = ", ifrdr_num, "/", ifrdr_dom
        print "D_length = ", len(D)
        print "RDR = ", Fraction(avg_den_rdr).limit_denominator(), " = ", avg_den_rdr
        print "IFRA = ", Fraction(avg_den_ifrdr).limit_denominator(), " = ", avg_den_ifrdr
        print "IFRA_Old = ", Fraction(avg_den_ifrdrold).limit_denominator(), ' = ', avg_den_ifrdrold, "\n\n"
        i = i + 1



if __name__ == "__main__":
    k = [651056770906015076056810763456358567190100156695615665659,
         723647816274791289489234589823745819748919823748132114123,
         182734757873569834951818919184818418294381845818567267241,
         678954729851252385323481287667812418539458486123951344599,
         124158546800001293123412834918394812491000019234891241901,
         124718438021650006546498470546510346543065497984600164987,
         984204650651503454630300015456450016549874981203165498797,
         312165498413198410060651560608967987910320194981001330311,
         781205164160606406606000321654984032064032065494860300351,
         654649810694791320641940323064946000651498798461613564989]
    w = [7, 9 , 11]
    testDesnity(k)
    # D = [1, 3, 23, 27]
    # k = 32119
    # ifrdr = IFRA.RDR_algorithm(D, k)
    # ifrdr_old = IFRA_positive.RDR_algorithm(D, k)
    # print "IFRA > ", ifrdr
    # print "IFRA_old > ", ifrdr_old
    # D = [1, 3, 9, 19, 21, 27]
    # w = 6
    # while w > 1:
    #     x = revisited_rdr.get_Dw(D, w)
    #     print "w = ", w, ", D- = ", x
    #     w = w-1

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