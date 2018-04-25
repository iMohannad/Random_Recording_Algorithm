import math

def generate_random_D(m, l):
    if l > (m+1)/2:
        raise ValueError("l should satisfy the condition l <= (m+1)/2")
    D = []
    for i in range(2, l+1, 1):
        odd = False
        while not odd:
            x = random.randint(3, m)
            if(x % 2 != 0 and x not in D):
                odd = True
        D.append(x)
    D.sort()
    return D

def add_carry(bin_k, len_k, s, length_neg_bin_d, rdr):
    bin_s = list(bin_k)
    print bin_s
    print "bin_s[", len(bin_k)-s-1,"] > ",bin_s[len(bin_k)-s-1]
    carry = '0'
    length_bin_s = len(bin_s)
    # Check up the carry
    # Index of next bit
    index =len(bin_k)-s-2
    if (len(bin_k)-s-1) == -1:
        if (s == length_neg_bin_d):
            rdr.insert(0, 1)
            flag_d = 1
            return ''
        else:
            flag_d = 1
            bin_s.insert(0, '1')
            bin_s = bin_s[:len(bin_s) - length_neg_bin_d]
            bin_k = "".join(bin_s)
            return bin_k
    if bin_s[len(bin_k)-s-1] == '1':
        carry = '1'
        bin_s[len(bin_k)-s-1] = '0'
        print "bin_s updated > ", bin_s, " len(bin_k)-s ", len(bin_k)-s
    else:
        bin_s[len(bin_k)-s-1] = '1'

    while carry == '1':
        print index

        if index == 0:
            if (bin_s[index] == '1'):
                bin_s[index] = '0'
                bin_s.insert(0, '1')
                carry = '0'
            else:
                bin_s[index] = '1'
            break
        carry = '1' if bin_s[index] == '1' else '0'
        bin_s[index] = '0' if bin_s[index] == '1' else '1'
        index = index - 1

    # Find number of zeros in the beginning
    # index = 0
    # while int(bin_s[len(bin_s)-index-1], 2) ^ int(neg_bin_d[len(neg_bin_d)-index-1]) == 0:
    #     rdr.insert(0, 0)
    #     index = index+1
    flag_d = 1
    bin_s = bin_s[:len(bin_s) - length_neg_bin_d]
    bin_k = "".join(bin_s)
    print "updated binary s> ", bin_s
    print "updated bin_k > ", bin_k
    print "RDR > ", rdr
    # bin_k = bin_k[:len(bin_s)-(s-1)]
    print "bin_k > ", bin_k
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    return bin_k

def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)))

def main():
    D = [1, 3, 23, 27]
    # D = [1, 17, 21, 25, 27]
    # D = [1, 9, 13, 17, 21]
    # D = [1, 3, 5, 11, 19]
    # D =  [1, 9, 11, 27, 29]
    # D =  [1, 3, 9, 15, 19]
    # D =  [1, 5, 19, 25, 27]
    # D =  [1, 9, 15, 17, 23] # Gives me problems .. problems solved
    # D =  [1, 3, 9, 11, 29]
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
            print rdr
            continue
        for s in range(Wn + 2, 1, -1):
            count = count + 1
            if count >= 20:
                bin_k = ''
                print "COUNT REACHED"
                flag_d = 1
                print rdr
                break
            for d in D:
                print "-----------------------new d-----------------------"
                bin_d = bin(d)[2:]
                length_bin_d = len(bin_d)
                print "D > ", d, " bin d > ", bin_d, " length_bin_d > ", length_bin_d
                # Neg D
                neg_d = 2**s - d
                while neg_d < 0:
                    neg_d = neg_d + 2**s
                print "neg_d = ", neg_d, " s = ", s,
                neg_bin_d = bin(neg_d)[2:]
                print " neg_bin_d = ", neg_bin_d
                length_neg_bin_d = len(neg_bin_d)
                print "bin_d> ", bin_d, " bin_k > ", bin_k, "bin_d < bin_k = ", bin_d <= bin_k
                if bin_d <= bin_k and length_bin_d <= len(bin_k):
                    print "----------------------bin_d less than bin_k"
                    # If d value equal to k
                    if int(bin_d, 2) ^ int(bin_k, 2) == 0:
                        rdr.insert(0, d)
                        print rdr
                        bin_k = ''
                        flag_d = 1
                        break
                    print bin_k[len(bin_k) - s:]
                    print "neg bin_d > ", int(neg_bin_d, 2) , " bin_k > ", int(bin_k[len(bin_k)-s:], 2), " Value > ", int(neg_bin_d, 2) ^ int(bin_k[len(bin_k)-s:], 2)
                    print "len bin_k > ", len(bin_k), " length of d = ", length_bin_d
                    print "int d = ", int(bin_d, 2), ", d = ", d, " bin_k = ", int(bin_k[len(bin_k)-length_bin_d-1:], 2)
                    print "length of bin_d", len(bin_d[length_bin_d-s:])
                    if len(bin_d[length_bin_d-s:]) == (s) and int(bin_d, 2) ^ int(bin_k[len(bin_k)-(s):], 2) == 0:
                        rdr.insert(0, d)
                        print "it went innnnnnnnnnnnnnn"
                        for j in range(0, length_bin_d-1):
                            rdr.insert(0, 0)
                        bin_k = bin_k[:len(bin_k)-length_bin_d]
                        print "update bin_k > ", bin_k
                        print "RDR > ", rdr
                        flag_d = 1
                        break
                    elif int(neg_bin_d, 2) ^ int(bin_k[len(bin_k)-length_neg_bin_d:], 2) == 0 and neg_d != 1:
                        if bin_k[len(bin_k)-s-1] == '1':
                            continue
                        print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
                        rdr.insert(0, -d)
                        # Inserting zeros
                        print "length neg_bin d > ", length_neg_bin_d
                        for j in range(0, length_neg_bin_d-1):
                            rdr.insert(0, 0)
                        bin_k = add_carry(bin_k, len(bin_k), s, length_neg_bin_d, rdr)
                        flag_d = 1
                        break
                    max_length = max_length - 1
            if flag_d == 1:
                flag_d = 0
                s = Wn + 2
                break
        if flag_d == 0 and s == 2:
            rdr.insert(0, 1)
            bin_k = bin_k[:len(bin_k)-1]
    print "Final RDR = ", rdr

def run_tests_time():
    i = 5
    [D, Di, naf, min_length] = RDR(1000, i, 26959956671506397946670150870196259404578077144243917216827126959956671506397946670150870196259404578077144243917216)
    min_len = min_length
    D_set = D
    D_result = Di
    naf_result = naf
    j = 0
    averageTime = 0
    while i <= 300:
        while j < 1000:
            startTime = time.time()
            [D, Di, naf, min_length] = RDR(1000, i, 269599566715063979466701508701962594045780726959956671506397946670150870196259404578077144243917216827126959956671506397946670150870196259404578077144243917216714424391721682712368051)
            endTime = time.time()
            averageTime = averageTime + (endTime - startTime)
            j = j+1
        averageTime = averageTime / 1000
        print "Average Time for digit set of Size ", i, " = ", averageTime
        averageTime = 0
        j = 0
        i = i+1

if __name__ == '__main__':
    main()