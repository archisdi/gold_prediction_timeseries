author = "AI research team"

import numpy as np
from operator import truediv
lr = 0.01


def initWeight(inputSize, series, outputSize):
    weight = []
    for i in range(inputSize):
        weight.append([[np.random.random() for i in range(series)] for i in range(outputSize)])
    return weight

def initBias(inputSize,series,outputSize):
    bias =[]
    for i in range(inputSize) :
        # masih salah
        bias.append([np.random.random() for i in range(outputSize)])
    return bias

def activFunction(l, w, b):
    z = np.dot(w,l)
    a=np.exp(-(z + b))
    sig = 1 / (1 + a)
    # print sig
    return sig

def forward(l0, w0, w1, b0, b1):
    l1 =[]
    output = []
    for i in range(len(l0)):
        l1.append(activFunction(l0[i], w0[i], b0[i]))
        output.append(activFunction(l1[i], w1[i], b1[i]))
    return l1, output

def backward(output, w1, l1, b1, w0, l0, b0, error):
    d1 = output * (1 - output).T * error
    d0 = l1 * (1 - l1).T * d1 *w1.T
    dw1 = lr * d1.T * l1
    dw0 = lr * d0.T * l0
    db1 = lr * d1
    db0 = lr * b0
    w1 = w1 + dw1.T
    w0 = w0 + dw0.T
    b1 = b1 + db1
    b0 = b0 + db0
    return w0, w1, b0, b1

def MAPEcalc(output, target):
    print output
    selisih = [x - y for x, y in zip(target, output)]
    print selisih
    print target
    return map(truediv,selisih,target)

def errorCalc(output, target):
    error = [x - y for x, y in zip(target, output)]
    return error

def train(atribut, target, epoch):
    inputSize = len(atribut)
    series = len(atribut[0])
    MAPE = 0
    outputSize = 1
    l0 = atribut
    b0 = initBias(inputSize,series,3)
    b1 = initBias(inputSize,series,1)
    w0 = initWeight(inputSize, series, 3)
    w1 = initWeight(inputSize, series, 1)
    # print target

    for i in range(epoch):
        l1, output = forward(l0, w0, w1, b0, b1)
        print output
        error = errorCalc(output, target)
        MAPE = MAPEcalc(output, target)
        w0, w1, b0, b1 = backward(output, w1, l1, b1, w0, l0, b0, error)
    return MAPE
