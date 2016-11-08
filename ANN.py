author = "AI research team"

import numpy as np

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
    print(l)
    print(w)
    print(b)
    b= 0.5
    # masih salah
    a=np.exp(sum(np.dot(w, l)) + b)
    print(a)
    sig = 1 / (1 + a)
    print(sig)
    print('-----------------')
    return sig

def forward(l0, w0, w1, b0, b1):
    l1 =[]
    output = []
    for i in range(len(l0)):
        l1.append(activFunction(l0[i], w0[i], b0[i]))
        output.append(activFunction(l1[i], w1[i], b1[i]))
    # print(output)
    return l1, output

def backward(output, w1, l1, b1, w0, l0, b0, error):
    d1 = output * (1 - output).T * error
    d0 = l1 * (1 - l1).T * (d1 * lr).T
    dw1 = w1 + (lr * d1 * l1)
    dw0 = w0 + (lr * d0 * l0)
    db1 = b1 + (lr * d1)
    db0 = b0 + (lr * b0)
    return dw0, dw1, db0, db1

def MAPEcalc(output, target):
    MAPE = np.abs((output - target) / target)
    return MAPE

def errorCalc(output, target):
    error = np.abs(output - target)
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

    for i in range(epoch):
        l1, output = forward(l0, w0, w1, b0, b1)
        break
        error = errorCalc(output, target)
        MAPE = MAPEcalc(output, target)
        print(MAPE)
        print(error)
        w0, w1, b0, b1 = backward(output, w1, l1, b1, w0, l0, b0, error)

    return MAPE
