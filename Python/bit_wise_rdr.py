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
    max_length = bin(max(D))
    while bin_k != '':
        if bin_k[len(bin_k)-1] == 0:
            rdr.insert(0, 0)
            bin_k = bin_k[:len(bin_k)-1]
            continue
        for i in range(Wn + 2, 2, -1):
            for d in D:
                if d < k:
                    bin_d = bin(d)[2:]
                    print "bin_d = ", bin_d
                    length_bin_d = len(bin(d))
                    # Neg D
                    neg_d = 2**i - d
                    print "neg_d = ", neg_d, " i = ", i, " d = ", d
                    neg_bin_d = bin(neg_d)[2:]
                    print "neg_bin_d = ", neg_bin_d
                    length_neg_bin_d = len(neg_bin_d)
                    if int(bin_d, 2) ^ int(bin_k[len(bin_k)-length_bin_d:], 2) == 0:
                        rdr.insert(0, d)
                        bin_k = bin_k[:len(bin_k)-length_bin_d]
                        flag_d = 1
                        break
                    if int(neg_bin_d, 2) ^ int(bin_k[len(bin_k)-length_neg_bin_d:], 2) == 0:
                        rdr.insert(0, -d)
                        bin_k = bin_k[:len(bin_k)-length_neg_bin_d-1]
                        flag_d = 1
                        break
            if flag_d == 1:
                flag_d = 0
                break


if __name__ == '__main__':
    main()