import sys
import numpy as np


'''
The Kernel function takes in two strings and an integer p.
p denotes the length of a substring, which is contained in both sequences s and t.

Returns the total count of the substrings that are common to both sequence s and t.
'''
def M(s: str, t: str, p: int) -> int:
    observed = []
    for i in range(len(s)-p+1):
        substring = s[i:i+p]
        if substring in t:
            if substring not in observed:
                observed.append(substring)
    return len(observed)

def Kperceptron(trainx, trainy, num):
    I = []
    for t in range(0, len(trainx)):
        dotproduct = 0
        for i in I: 
            dotproduct += int(trainy[i])*M(trainx[i], trainx[t], num)
        if int(trainy[t])*dotproduct <= 0:
            I.append(t)
    return I

def calculateError(list, trainx, trainy, testx, testy, num):
    errorCount = 0
    for t in range(len(testx)):
        sum = 0
        for i in range(len(list)):
            ind = list[i]
            sum += int(trainy[ind])*M(trainx[ind], testx[t], num)
        if np.sign(int(testy[t])) != np.sign(sum):
            errorCount += 1
    return float(float(errorCount)/float(len(testy)))
            
if __name__ == "__main__":

    args = sys.argv
    # sys.argv : [<trainingdata filename>, <testdata filename>]
    train_path = args[1]
    test_path = args[2]

    # Lists of training/test features and labels
    train_f = []
    train_l = []
    test_f = []
    test_l = []

    with open(train_path, 'r') as f:
        train_data = f.readlines()

    train_data = [x.strip() for x in train_data]
    for i in range(len(train_data)):
        train_f.append(train_data[i].split(" ")[0])
        train_l.append(train_data[i].split(" ")[1])

    with open(test_path, 'r') as k:
        test_data = k.readlines()

    test_data = [x.strip() for x in test_data]
    for j in range(len(test_data)):
        test_f.append(test_data[j].split(" ")[0])
        test_l.append(test_data[j].split(" ")[1])
    

    list_3 = Kperceptron(train_f, train_l, 3)
    print("First List Generated")
    list_4 = Kperceptron(train_f, train_l, 4)
    print("Second List Generated")
    list_5 = Kperceptron(train_f, train_l, 5)
    print("Third List Generated")
    print('\n')

    print("Printing Train Error for p=3, p=4, p=5:")
    print("---------------------------------------")
    print("Training Error p=3: ", calculateError(list_3, train_f, train_l, train_f, train_l, 3))
    print("Training Error p=4: ", calculateError(list_4, train_f, train_l, train_f, train_l, 4))
    print("Training Error p=5: ", calculateError(list_5, train_f, train_l, train_f, train_l, 5))
    print('\n')

    print("Printing Test Error for p=3, p=4, p=5:")
    print("---------------------------------------")
    print("Test Error p=3: ", calculateError(list_3, train_f, train_l, test_f, test_l, 3))
    print("Test Error p=4: ", calculateError(list_4, train_f, train_l, test_f, test_l, 4))
    print("Test Error p=5: ", calculateError(list_5, train_f, train_l, test_f, test_l, 5))