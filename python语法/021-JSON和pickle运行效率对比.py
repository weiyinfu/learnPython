import pickle

import json

import numpy as np
import timeit
import msgpack

a = np.random.random((200, 200))
b = a.tolist()


def use_json():
    bb = json.dumps(b)
    return bb


def use_pickle():
    aa = pickle.dumps(a)
    return aa


def use_msgpack():
    return msgpack.dumps(b)


n = 100
for f in (use_msgpack, use_json, use_pickle):
    print(f.__name__, 'memory =', len(f()),
          'time=', timeit.timeit(f, number=n))
