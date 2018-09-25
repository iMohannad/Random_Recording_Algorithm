import math
import random
import time

carry = 0

def average_density(rdr):
    countZeros = 0
    length = 0
    for i in rdr:
        length = length + 1
        if (i == 0):
            countZeros = countZeros + 1
    return [length - countZeros, length]


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

def add_carry_revised(bin_k, W):
    global carry

    len_k = len(bin_k)
    # convert bin_k to an array to allow change of one bit easily
    bin_s = list(bin_k)
    # if carry is 0, return
    if (carry == 0):
        return bin_k
    # if carry is 2, then, add carry and check if there's any more carry
    if (carry == 2):
        if (bin_k == '' or bin_k == '0'):
            carry = 0
            return '10'
        if (bin_k == '1'):
            carry = 0
            return '11'
        if (bin_k[len_k-2] == '0'):
            bin_s[len_k-2] = '1'
            carry = 0
        else:
            bin_s[len_k-2] = '0'
            carry = 1
        count = 2
        # index is set to the second LSB
        index = len_k-3
    elif(carry == 1):
        # If k is empty, Then carry needs to be added last.
        if (bin_k == ''):
            return '1'

        # If LSB is 0, we just add carry to make it one. If it's 1, we make it 0 and carry is set to 1
        if(bin_k[len_k-1] == '0'):
            bin_s[len_k-1] = '1'
            carry = 0
        else:
            bin_s[len_k-1] = '0'
            carry = 1
        count = 1
        # index is set to the second LSB
        index = len_k-2



    while carry == 1 and count <= W:
        # if k was only 1 bit, we just append the carry
        if index == -1:
            carry = 0
            bin_s.insert(0, '1')
        # if we reached the MSB and it's 1, then we make it 0 and append 1,
        # if it is 0, it is just set to 1.
        elif index == 0:
            carry = 0
            if (bin_s[index] == '1'):
                bin_s[index] = '0'
                bin_s.insert(0, '1')
            else:
                bin_s[index] = '1'
        # if the bit is neither of the last two cases, it's set to 1 when it is 0,
        # or it is set to 0, and carry is still 1
        elif(bin_k[index] == '0'):
            bin_s[index] = '1'
            carry = 0
        else:
            bin_s[index] = '0'
        # Update the index
        index = index - 1
        count = count + 1
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
    c = 0
    # global carry
    while bin_k != '' or c > 0:
        if bin_k == '': # carry is 1
            rdr.insert(0, 1)
            c = 0
            continue
        # if LSB(k) xor c = 0, zero is appened to rdr and k is shifted right 1 bit
        if (bin_k[len(bin_k)-1] == '0' and c == 0 ) or (bin_k[len(bin_k)-1] == '1' and c == 1):
            rdr.insert(0, 0)
            bin_k = bin_k[:len(bin_k)-1]
            continue
        # if LSB(k) xor c = 1, we extract w bit
        # convert bin_k to an array to allow change of one bit easily
        bin_s = list(bin_k)
        bin_s[len(bin_k)-1] = '1'
        bin_k = "".join(bin_s)
        c = 0
        for w in range(Wn + 2, 0, -1):
            # if the window is bigger than the length of k, we need to have smaller windwo
            if (w > len(bin_k)):
                    continue
            # extract w bits from bin_k
            k_reg = bin_k[len(bin_k) - w:]
            for d in D:
                # we check every d in the digit set D
                bin_d = bin(d)[2:] # get the binary representation of d
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
            if flag_d == 1:
                flag_d = 0
                break
            for d in D:
                # we check every d in the digit set D
                bin_d = bin(d)[2:] # get the binary representation of d
                # compute the negative residue of d, if neg_d is negative, it is ignored by setting it to 0.
                neg_d = 2**w - d
                while neg_d < 0:
                    neg_d = 0
                neg_bin_d = bin(neg_d)[2:] # get the binary representation of neg_d
                if int(neg_bin_d, 2) ^ int(k_reg, 2) == 0 and neg_d != 1:
                    rdr.insert(0, -d)
                    # Inserting zeros
                    for j in range(0, w-1):
                        rdr.insert(0, 0)
                    # update k by shifting it right w bits
                    bin_k = bin_k[:len(bin_k) - w]
                    c = 1
                    # update k after adding a carry to LSB
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
    return rdr

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
    w = [5, 7, 9 , 11]
    index_w = 0
    index_nist = 0
    while index_w < 3:
        while index_nist < 5:
            D = generate_random_D(2**w[index_w], 2**(w[index_w]-3)-1)
            while j < 1000:
                # print j
                startTime = time.time()
                rdr = RDR_algorithm(D, nist[index_nist])
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
    # print "bin > ", bin(651056770906015076056810763456358567190100156695615665659)
    # run_tests_time()
    # nist = [651056770906015076056810763456358567190100156695615665659,
    #         2695995667150639794667015087019625940457807714424391721682712368051,
    #         115792089210351248362697456949407573528996955234135760342422159061068512044339,
    #         26959956671506397946670150870196259404578077144243917216827126959956671506397946670150870196259404578077144243917216,
    #         2695995667150639794667015087019625940457807714424391721682712368058238947189273490172349807129834790127349087129834623486127461012630462184628923461201280461]

    # D = [1, 7, 23, 25, 33, 37, 39, 43, 49, 53, 63, 65, 67, 71, 75, 77, 85, 89, 97, 99, 103, 107, 113, 115, 117, 119, 127, 131, 133, 135, 145, 151, 153, 157, 163, 165, 171, 181, 183, 185, 189, 191, 197, 199, 201, 203, 207, 211, 213, 219, 221, 225, 227, 229, 233, 235, 237, 243, 247, 255, 257, 259, 269, 283, 287, 295, 307, 311, 321, 329, 333, 335, 339, 341, 345, 349, 351, 371, 373, 381, 385, 393, 403, 405, 411, 419,421, 429, 431, 433, 435, 437, 441, 459, 471, 489, 503, 519, 521, 523, 527, 529, 535, 537, 543, 547, 549, 563, 567, 577, 585, 589, 601, 603, 609, 615, 619, 627, 633, 635, 641, 643, 655, 659, 665, 671, 675, 681, 687, 709, 711, 719, 727, 729, 731, 733, 735, 737, 741, 743, 745, 747, 749, 751, 755, 761, 763, 765, 771, 777, 779, 783, 785, 789, 797, 803, 807, 813, 817, 827, 839, 841, 845, 853, 859, 863, 865, 871, 873, 875, 883, 887, 889, 891, 895, 897, 899, 901, 905, 909, 915, 925, 927, 933, 935, 945, 949, 961, 963, 967, 977, 983, 985, 987, 989, 995]
    # k = nist[4]
    # rdr = RDR_algorithm(D, k)
    # print "IFRA > ", rdr
    rdr = RDR_algorithm([1, 3, 23, 27], 1023)
    print "RDR > ", rdr
    print "Min_len > ", len(rdr)
    print "IsRDR > ", check_rdr(rdr)
    print "check > ", check_num(rdr)