import math
import random
import time

def average_density(rdr):
    countZeros = 0
    length = 0
    for i in rdr:
        length = length + 1
        if (i == 0):
            countZeros = countZeros + 1
    return [countZeros, length]


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
    # convert bin_k to an array to allow change of one bit easily
    bin_s = list(bin_k)

    carry = '0'
    # If k is empty, Then carry needs to be added last.
    if (bin_k == ''):
        return '1'

    # If LSB is 0, we just add carry to make it one. If it's 1, we make it 0 and carry is set to 1
    if(bin_k[len_k-1] == '0'):
        bin_s[len_k-1] = '1'
    else:
        bin_s[len_k-1] = '0'
        carry = '1'

    # index is set to the second LSB
    index = len_k-2
    while carry == '1':
        # if k was only 1 bit, we just append the carry
        if index == -1:
            carry = '0'
            bin_s.insert(0, '1')
        # if we reached the MSB and it's 1, then we make it 0 and append 1,
        # if it is 0, it is just set to 1.
        elif index == 0:
            carry = '0'
            if (bin_s[index] == '1'):
                bin_s[index] = '0'
                bin_s.insert(0, '1')
            else:
                bin_s[index] = '1'
        # if the bit is neither of the last two cases, it's set to 1 when it is 0,
        # or it is set to 0, and carry is still 1
        elif(bin_k[index] == '0'):
            bin_s[index] = '1'
            carry = '0'
        else:
            bin_s[index] = '0'
        # Update the index
        index = index - 1
    # bin_s is converted back to a variable
    bin_k = "".join(bin_s)
    return bin_k

def get_Wn(D):
    return int(math.floor(math.log(max(D), 2)))

def RDR_algorithm(D, k):
    rdr = []
    bin_k = bin(k)[2:]
    # get number of bits
    Wn = get_Wn(D)
    flag_d = 0
    while bin_k != '':
        # If k is even, zero is appened to rdr and k is shifted right 1 bit
        if bin_k[len(bin_k)-1] == '0':
            rdr.insert(0, 0)
            bin_k = bin_k[:len(bin_k)-1]
            continue
        # if LSB is not 0, we extract w bit
        for w in range(Wn + 1, 0, -1):
            # if the window is bigger than the length of k, we need to have smaller windwo
            if (w > len(bin_k)):
                    continue
            # we check every d in the digit set D
            for d in D:
                bin_d = bin(d)[2:] # get the binary representation of d
                length_bin_d = len(bin_d)
                # extract w bits from bin_k
                k_reg = bin_k[len(bin_k) - w:]
                # compute the negative residue of d, if neg_d is negative, it is ignored by setting it to 0.
                neg_d = 2**w - d
                while neg_d < 0:
                    neg_d = 0
                neg_bin_d = bin(neg_d)[2:] # get the binary representation of neg_d
                length_neg_bin_d = len(neg_bin_d)
                # d cannot be chosen unless the value is less than the extracted window.
                if d <= k_reg:
                    if int(bin_d, 2) ^ int(k_reg, 2) == 0:
                        rdr.insert(0, d)
                        # inserting w-1 zeros
                        for j in range(0, w-1):
                            rdr.insert(0, 0)
                        # update k by shifting it right w bits
                        bin_k = bin_k[:len(bin_k) - w]
                        # set flag_d to 1 to set the window to Wn+1
                        flag_d = 1
                        break
                    elif int(neg_bin_d, 2) ^ int(k_reg, 2) == 0 and neg_d != 1:
                        rdr.insert(0, -d)
                        # Inserting zeros
                        for j in range(0, w-1):
                            rdr.insert(0, 0)
                        # update k by shifting it right w bits
                        bin_k = bin_k[:len(bin_k) - w]
                        # update k after adding a carry to LSB
                        bin_k = add_carry_revised(bin_k)
                        # set flag_d to 1 to set the window to Wn+1
                        flag_d = 1
                        break
            # break out of the for loop to check if we finished k or not
            if flag_d == 1:
                flag_d = 0
                break

    # In the end, there might be some leading zeros which are not needed,
    # this while loop removes the leading zeros and update k accordingly
    while (rdr[0] == 0):
        rdr = rdr[1:]
    # return the result, and length of result
    return [rdr, len(rdr)]

# this function return the value of rdr representation.
def check_num(rdr):
    b = 1
    sum = 0
    for i in range(len(rdr)-1, -1, -1):
        sum = sum + b*rdr[i]
        b = b*2
    return sum

def run_tests_time():
    i = 10
    j = 0
    averageTime = 0
    nist = [651056770906015076056810763456358567190100156695615665659,
            2695995667150639794667015087019625940457807714424391721682712368051,
            115792089210351248362697456949407573528996955234135760342422159061068512044339,
            26959956671506397946670150870196259404578077144243917216827126959956671506397946670150870196259404578077144243917216,
            2695995667150639794667015087019625940457807714424391721682712368058238947189273490172349807129834790127349087129834623486127461012630462184628923461201280461]
    w = [7, 9 , 11]
    index_w = 0
    index_nist = 0
    while index_w < 3:
        while index_nist < 5:
            D = generate_random_D(2**w[index_w], 2**(w[index_w]-3)-1)
            while j < 1000:
                # print j
                startTime = time.time()
                [rdr, min_length] = RDR_algorithm(D, nist[index_nist])
                endTime = time.time()
                averageTime = averageTime + (endTime - startTime)
                j = j+1
            averageTime = averageTime / 1000
            print "Average Time for NIST[", index_nist, "] and w = ", w[index_w], " = ", averageTime
            averageTime = 0
            j = 0
            index_nist = index_nist +1
        index_nist = 0
        index_w = index_w + 1

if __name__ == '__main__':
    print "bin > ", bin(651056770906015076056810763456358567190100156695615665659)
    run_tests_time()
    # [rdr, min_len] = RDR_algorithm([1, 3, 23, 27], 651056770906015076056810763456358567190100156695615665659)
    # print "RDR > ", rdr
    # print "Min_len > ", min_len
    # print "IsRDR > ", check_rdr(rdr)
    # print "check > ", check_num(rdr)