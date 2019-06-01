import sys
import numpy as np

'''
The Kernel function takes in two strings and an integer p.
p denotes the length of a substring, which is contained in both sequences s and t.
'''
def K(s, t, p):
    s_dict = {}
    t_dict = {}
    for i in range(len(s)-p+1):
        if s[i:i+p] not in s_dict:
            s_dict[s[i:i+p]] = 1
        else:
            s_dict[s[i:i+p]] += 1
    for j in range(len(t)-p+1):
        if t[j:j+p] not in t_dict:
            t_dict[t[j:j+p]] = 1
        else:
            t_dict[t[j:j+p]] += 1
    val = 0
    for key in s_dict.keys():
        if key in t_dict.keys():
            val += s_dict[key]*t_dict[key]
    return val

def Kperceptron(trainx, trainy, num):
    I = []
    for t in range(0, len(trainx)):
        dotproduct = 0
        for i in I: 
            dotproduct += int(trainy[i])*K(trainx[i], trainx[t], num)
        if int(trainy[t])*dotproduct <= 0:
            I.append(t)
    return I

def calculateError(list, trainx, trainy, testx, testy, num):
    errorCount = 0
    for t in range(len(testx)):
        sum = 0
        for i in range(len(list)):
            ind = list[i]
            sum += int(trainy[ind])*K(trainx[ind], testx[t], num)
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
    
    list_1 = Kperceptron(train_f, train_l, 5)
    print("List generated")
    print('\n')
    
    fivemer_dict = {}
    for ind in list_1:
        curr_seq = train_f[ind]
        label = int(train_l[ind])
        if label == 1:
            for k in range(0, len(curr_seq)-5+1):
                fivemer = curr_seq[k:k+5]
                if fivemer not in fivemer_dict.keys():
                    fivemer_dict[fivemer] = 1
                else:
                    fivemer_dict[fivemer] += 1

        else:
            for k in range(0, len(curr_seq)-5+1):
                fivemer = curr_seq[k:k+5]
                if fivemer not in fivemer_dict.keys():
                    fivemer_dict[fivemer] = -1
                else:
                    fivemer_dict[fivemer] -= 1

    maxList = [0,0]
    maxfivemer = ["RANDO", "RANDO"]
    for key, value in fivemer_dict.items():
        if value > maxList[0]:
            maxList[1] = int(maxList[0])
            maxList[0] = value
            maxfivemer[1] = str(maxfivemer[0])
            maxfivemer[0] = key
        
        elif value > maxList[1]:
            maxList[1] = value
            maxfivemer[1] = key

    print(maxfivemer[0], maxfivemer[1])