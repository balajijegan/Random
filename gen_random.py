#!/usr/bin/env python

import sys
import random
import string
import time
import datetime
import multiprocessing

int_array= []
str_array1 = []
str_array2 = []
date_array = []

def get_random_string(count):
    word = ''.join([random.choice(string.ascii_letters) for i in range(count)])
    return word

def gen_date():
    now = int(time.time())
    for i in range(0,10000):
        date_array.append(datetime.datetime.fromtimestamp(random.randint(0,now)).strftime('%D'))

def print_random(count):
    for i in range(0,count):
        print random.choice(int_array), random.choice(int_array), random.choice(str_array1), random.choice(str_array2), random.choice(date_array)

def generate():
    for i in range(0,10000):
        int_array.append(random.randint(0,10000000))
        str_array1.append(get_random_string(10))
        str_array2.append(get_random_string(20))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage: %s parallel_process bucket_size no_buckets" % sys.argv[0]
        sys.exit(1)
    generate()
    gen_date()
    jobs = []
    pool = multiprocessing.Pool(processes=int(sys.argv[1]))
    pool.map(print_random,[int(sys.argv[2]) for x in range(int(sys.argv[3]))])
