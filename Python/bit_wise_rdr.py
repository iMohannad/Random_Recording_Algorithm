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
    count = 0
    while bin_k != '':
        # Remove leading zeros
        if bin_k[len(bin_k)-1] == '0':
            rdr.insert(0, 0)
            bin_k = bin_k[:len(bin_k)-1]
            continue
        for s in range(Wn + 2, 2, -1):
            count = count + 1
            if count == 10:
                bin_k = ''
                print rdr
                break
            for d in D[::-1]:
                print "-----------------------new d-----------------------"
                bin_d = bin(d)[2:]
                length_bin_d = len(bin_d)
                print "bin d > ", bin_d, " length_bin_d > ", length_bin_d
                # Neg D
                neg_d = 2**s - d
                while neg_d < 0:
                    neg_d = neg_d + 2**s
                print "neg_d = ", neg_d, " s = ", s, " d = ", d
                neg_bin_d = bin(neg_d)[2:]
                print "neg_bin_d = ", neg_bin_d
                length_neg_bin_d = len(neg_bin_d)
                if bin_d <= bin_k:
                    print "len bin_k > ", len(bin_k), " length of d = ", length_bin_d
                    print "int d = ", int(bin_d, 2), ", d = ", d, " bin_k = ", int(bin_k[len(bin_k)-length_bin_d-1:], 2)
                    if length_bin_d == (s-1) and int(bin_d, 2) ^ int(bin_k[len(bin_k)-length_bin_d:], 2) == 0:
                        rdr.insert(0, d)
                        print "it went innnnnnnnnnnnnnn"
                        for j in range(0, length_bin_d):
                            rdr.insert(0, 0)
                        bin_k = bin_k[:len(bin_k)-length_bin_d]
                        print "update bin_k > ", bin_k
                        flag_d = 1
                        break
                    elif int(neg_bin_d, 2) ^ int(bin_k[len(bin_k)-length_neg_bin_d:], 2) == 0 or int(neg_bin_d, 2) ^ int(bin_k[len(bin_k)-length_neg_bin_d:], 2) == 2**(s-1):
                        rdr.insert(0, -d)
                        # Inserting zeros
                        for j in range(0, length_neg_bin_d):
                            rdr.insert(0, 0)

                        carry = '0'
                        # Find number of zeros in the beginning
                        
                        bin_k = bin_k[:len(bin_k)-(s-1)]
                        print "bin_k > ", bin_k
                        bin_s = list(bin_k)
                        print bin_s
                        print bin_s[len(bin_k)-1]
                        if bin_s[len(bin_k)-1] == '1':
                            carry = '1'
                            index =len(bin_k)-1
                        else:
                            bin_s[len(bin_k)-1] = '1'
                        
                        while carry == '1':
                            carry = '1' if bin_s[index] == '1' else '0'
                            bin_s[index] = '0' if int(bin_s[index],2) ^ int(carry,2) == 0 else '1'
                            index = index - 1
                        flag_d = 1
                        bin_k = "".join(bin_s)
                        print "updated bin_k > ", bin_k
                        break
                    max_length = max_length - 1
            if flag_d == 1:
                flag_d = 0
                s = Wn + 2
                break
    print "Final RDR = ", rdr

if __name__ == '__main__':
    main()