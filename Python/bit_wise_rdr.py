import math


def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)))

def main():
    D = [1, 3, 23, 27]
    k = 31415
    rdr = []
    bin_k = bin(k)[2:]
    Wn = get_Wn(D)
    flag_d = 0
    max_length = len(bin(max(D)))
    while bin_k != '':
        if bin_k[len(bin_k)-1] == '0':
            rdr.insert(0, 0)
            bin_k = bin_k[:len(bin_k)-1]
            continue
        for s in range(Wn + 2, 2, -1):
            for d in D:
                bin_d = bin(d)[2:]
                length_bin_d = len(bin(d))
                # Neg D
                neg_d = 2**s - d
                # print "neg_d = ", neg_d, " i = ", s, " d = ", d
                neg_bin_d = bin(neg_d)[2:]
                # print "neg_bin_d = ", neg_bin_d
                length_neg_bin_d = len(neg_bin_d)
                if d < k:
                    bin_d = bin(d)[2:]
                    print "bin_d = ", bin_d
                    length_bin_d = len(bin(d))
                    # Neg D
                    neg_d = 2**i - d
                    while neg_d < 0:
                        neg_d = neg_d + 2**i
                    print "neg_d = ", neg_d, " i = ", i, " d = ", d
                    neg_bin_d = bin(neg_d)[2:]
                    print "neg_bin_d = ", neg_bin_d
                    length_neg_bin_d = len(neg_bin_d)
                    if length_bin_d == max_length and int(bin_d, 2) ^ int(bin_k[len(bin_k)-length_bin_d:], 2) == 0:
                        rdr.insert(0, d)
                        bin_k = bin_k[:len(bin_k)-length_bin_d]
                        flag_d = 1
                        break
                    if length_neg_bin_d == max_length and int(neg_bin_d, 2) ^ int(bin_k[len(bin_k)-length_neg_bin_d:], 2) == 0:
                        rdr.insert(0, -d)
                        bin_k = bin_k[:len(bin_k)-length_neg_bin_d-1]
                        flag_d = 1
                        break
                    max_length = max_length - 1
            if flag_d == 1:
                flag_d = 0
                max_length = bin(max(D))
                break
    print "Final RDR = ", rdr

if __name__ == '__main__':
    main()