import sys
sys.path.append('../Python')

from fractions import Fraction
import IFRA
import revisited_rdr


def testDesnity_multi(K):
    length = len(K)
    i = 5
    rdr = 0
    ifrdr = 0
    [rdr_num, rdr_dom] = [0, 0]
    [ifrdr_num, ifrdr_dom] = [0, 0]

    while i <= 50:
        D = IFRA.generate_random_D(i*6, i)
        avg_den_rdr = 0
        avg_den_ifrdr = 0
        for k in K:
            rdr = revisited_rdr.RDP(k, D)
            ifrdr = IFRA.RDR_algorithm(D, k)
            [rdr_num, rdr_dom] = revisited_rdr.average_density(rdr)
            [ifrdr_num, ifrdr_dom] = IFRA.average_density(ifrdr)
            avg_den_rdr = avg_den_rdr + float(rdr_num)/rdr_dom
            avg_den_ifrdr = avg_den_ifrdr + float(ifrdr_num)/ifrdr_dom
        # print "RDR > ", rdr
        # print "IFRA > ", ifrdr
        print "Digit set = ", D
        print "RDR = ", rdr_num, "/", rdr_dom
        print "IFRA = ", ifrdr_num, "/", ifrdr_dom
        print "D_length = ", len(D), ", RDR = ", Fraction(avg_den_rdr/length).limit_denominator(), " = ", avg_den_rdr/length, ", IFRA = ", Fraction(avg_den_ifrdr/length).limit_denominator(), " = ", avg_den_ifrdr/length,"\n"
        i = i + 1

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
    k = [651056770906015076056810763456358567190100156695615665659,
         564897984616489421648941841365468781321321987983186745187,
         231654984561198751321584897431849843154654213215644779875,
         568487954231586478954136136548956361215856235489646452139,
         654321564898751431564946513164416851649842184891518749841,
         487979843131687498132186410581018901045100402054489489789,
         123187981320654803210548910216548948972054981504654897941]
    # w = [7, 9 , 11]
    testDesnity_multi(k)
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