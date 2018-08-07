import math
import random
import time

def check_rdr(rdr):
    for i in range (0, len(rdr)-1):
        if rdr[i] != 0 and rdr[i+1] != 0:
            return False
    return True

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
    D.insert(0, 1)
    return D

def add_carry_revised(bin_k):
    len_k = len(bin_k)
    bin_s = list(bin_k)

    carry = '0'
    if (bin_k == ''):
        return '1'
    if(bin_k[len_k-1] == '0'):
        bin_s[len_k-1] = '1'
    else:
        bin_s[len_k-1] = '0'
        carry = '1'

    index = len_k-2
    while carry == '1':
        if index == -1:
            carry = '0'
            bin_s.insert(0, '1')
        elif index == 0:
            carry = '0'
            if (bin_s[index] == '1'):
                bin_s[index] = '0'
                bin_s.insert(0, '1')
            else:
                bin_s[index] = '1'

        elif(bin_k[index] == '0'):
            bin_s[index] = '1'
            carry = '0'
        else:
            bin_s[index] = '0'
        index = index - 1
    bin_k = "".join(bin_s)
    return bin_k


def add_carry(bin_k, len_k, s, length_neg_bin_d, rdr):
    bin_s = list(bin_k)
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
    else:
        bin_s[len(bin_k)-s-1] = '1'

    while carry == '1':

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
    return bin_k

def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)))

def RDR_algorithm(D, k):
    # print "k > ", k
    # print "D > ", D
    rdr = []
    bin_k = bin(k)[2:]
    Wn = get_Wn(D)
    flag_d = 0
    max_length = len(bin(max(D)))
    count = 0
    while bin_k != '':
        # Remove leading zeros
        if bin_k[len(bin_k)-1] == '0':
            # print "###################################"
            # print "                ZERO               "
            # print "-----------------------------------"
            rdr.insert(0, 0)
            bin_k = bin_k[:len(bin_k)-1]
            # print "k > ", bin_k
            # print "RDR = ", rdr
            # print "-----------------------------------"
            continue
        for s in range(Wn + 1, 0, -1):
            count = count + 1
            if (s > len(bin_k)):
                    continue;
            # if count >= 20:
            #     bin_k = ''
            #     flag_d = 1
            #     break
            for d in D:
                bin_d = bin(d)[2:]
                length_bin_d = len(bin_d)
                k_reg = bin_k[len(bin_k) - s:]
                # Neg D
                neg_d = 2**s - d
                while neg_d < 0:
                    neg_d = 0
                neg_bin_d = bin(neg_d)[2:]
                length_neg_bin_d = len(neg_bin_d)
                if d <= k_reg:
                    # print "~~~~~~~~~~~~~~~~~~~~~*******************~~~~~~~~~~~~~~~~~~~~~~~"
                    # print "s = ", s, ", d = ", bin_d, ", neg_d = ", neg_bin_d, ", k = ", bin_k, "bin_d < bin_k = ", bin_d <= bin_k, " len(bin_d) > ", len(bin_d)
                    # print "k_reg = ", k_reg
                    # If d value equal to k
                    if int(bin_d, 2) ^ int(k_reg, 2) == 0:
                        # print "###################################"
                        # print "               EQUAL               "
                        # print "-----------------------------------"
                        # print s
                        # print k_reg
                        rdr.insert(0, d)
                        for j in range(0, s-1):
                            rdr.insert(0, 0)
                        bin_k = bin_k[:len(bin_k) - s]
                        flag_d = 1;
                        # print "k > ", bin_k, ", s > ", s
                        # print "RDR > ", rdr
                        break;
                    elif int(neg_bin_d, 2) ^ int(k_reg, 2) == 0 and neg_d != 1:
                        # print "###################################"
                        # print "              NEGATIVE             "
                        # print "-----------------------------------"
                        # if (len(bin_k)-s-1) != -1 and bin_k[len(bin_k)-s-1] == '1':
                            # print "CANNOT ADD CARRY"
                            # print "-----------------------------------"
                            # continue
                        rdr.insert(0, -d)
                        # Inserting zeros
                        for j in range(0, s-1):
                            rdr.insert(0, 0)
                        bin_k = bin_k[:len(bin_k) - s]
                        # print "k > ", bin_k, ", s > ", s
                        # print rdr
                        bin_k = add_carry_revised(bin_k)
                        # bin_k = add_carry(bin_k, len(bin_k), s, length_neg_bin_d, rdr)
                        flag_d = 1
                        # print "k > ", bin_k
                        # print "RDR > ", rdr
                        # print "neg_d = ", neg_bin_d, ", bin_k = ", bin_k
                        # print "RDR > ", rdr
                        # print "-----------------------------------"
                        break
                    max_length = max_length - 1
                    # print "~~~~~~~~~~~~~~~~~~~~~*******************~~~~~~~~~~~~~~~~~~~~~~~"
            if flag_d == 1:
                flag_d = 0
                s = Wn + 2
                break


        # if flag_d == 0 and s == 2:
        #     rdr.insert(0, 1)
        #     bin_k = bin_k[:len(bin_k)-1]
    while (rdr[0] == 0):
        rdr = rdr[1:]
    # print rdr
    return [rdr, len(rdr)]

def check_num(rdr):
    b = 1;
    sum = 0
    for i in range(len(rdr)-1, -1, -1):
        sum = sum + b*rdr[i]
        b = b*2
    return sum

def run_tests_time():
    min_len = 1000
    i = 5
    j = 0
    averageTime = 0
    while i <= 300:
        while j < 1000:
            print j
            D = generate_random_D(i*5, i)
            startTime = time.time()
            
            [rdr, min_length] = RDR_algorithm(D, 651056770906015076056810763456358567190100156695615665659)
            endTime = time.time()
            averageTime = averageTime + (endTime - startTime)
            j = j+1
            print "CHECK > ", check_num(rdr)
            check_flag = check_rdr(rdr)
            if check_flag == False:
                print " -------------------- False Flag -----------------------------"
                print "D > ", D
                print rdr
                break
            # print "RDR > ", rdr, " min_length > ", min_length
        averageTime = averageTime / 1000
        # print "rdr = ", rdr, " Min Length = ", min_length, " Average Time for digit set of Size ", i, " = ", averageTime
        print "Average Time for digit set of Size ", i, " = ", averageTime
        averageTime = 0
        j = 0
        i = i+1

if __name__ == '__main__':
    print "bin > ", bin(651056770906015076056810763456358567190100156695615665659)
    run_tests_time()
    # [rdr, min_len] = RDR_algorithm([1, 3, 23, 27], 651056770906015076056810763456358567190100156695615665659)
    # print "RDR > ", rdr
    # print "Min_len > ", min_len
    # print "IsRDR > ", check_rdr(rdr)
    # print "check > ", check_num(rdr)