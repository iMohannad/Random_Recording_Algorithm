import sys
import time
import l_naf
import revisited_rdr
import bit_wise_rdr

# m is the upper bound of random digit set
# l is the length of the digit set
def ifrdr_test(k, m, l):
    # generate a random digit set
    D = bit_wise_rdr.generate_random_D(m, l)
    startTime = time.time()
    [rdr, min_length] = bit_wise_rdr.RDR_algorithm(D, k)
    endTime = time.time()

# m is the upper bound of random digit set
# l is the length of the digit set
def rdr_test(k, m, l):
    # generate a random digit set
    D = bit_wise_rdr.generate_random_D(m, l)
    startTime = time.time()
    [rdr, min_length] = bit_wise_rdr.RDR_algorithm(D, k)
    endTime = time.time()
