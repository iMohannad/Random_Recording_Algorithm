import math


def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)))

def main():
    D = [1, 3, 23, 27]
    k = 31415
    rdr = []
    bin_k = bin(k)[2:]
    Wn = get_Wn(D)
    while k != 0:

        for d in D:
            if d < k:
                bin_d = bin(d)[2:]
                length_bin_d = len(bin(d))
                # Neg D
                neg_d = 2**i - d
                neg_bin_d = bin(neg_d)[2:]
                length_neg_bin_d = len(neg_bin_d)
                if bin_d ^ bin_k[len(bin_k)-length_bin_d-1:] == 0:
                    rdr.insert(0, d)
                    break
                if neg_bin_d ^ bin_k[len(bin_k)-length_neg_bin_d-1:] == 0:
                    rdr.insert(0, -d)
                    break


if __name__ == '__main__':
    main()