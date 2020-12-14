import numpy as np
import pandas as pd
import random

df = pd.read_csv("smokers.csv")

# Gather initial data
numOfYes = df['smoke'].values.sum()
numOfNo = (~df['smoke']).values.sum()
diffInYesAndNo = abs(numOfYes - numOfNo)


def generator(x):
    firstOutcome = random.uniform(0, 1)
    if (firstOutcome > 0.6):
        return x
    else:
        secondOutcome = random.uniform(0, 1)
        if (secondOutcome > 0.5):
            return True
        else:
            return False


df['smoke'] = df['smoke'].apply(generator)


privateNumOfYes = df['smoke'].values.sum()
privateNumOfNo = (~df['smoke']).values.sum()
privateDiffInYesAndNo = abs(privateNumOfYes - privateNumOfNo)

percentageErrorInYes = (abs(privateNumOfYes - numOfYes) / numOfYes) * 100
percentageErrorInNo = (abs(privateNumOfNo - numOfNo) / numOfNo) * 100
percentageErrorInDiff = (abs(
    privateDiffInYesAndNo - diffInYesAndNo) / diffInYesAndNo) * 100

print("Before numOfYes:" + str(numOfYes))
print("Before numOfNo:" + str(numOfNo))
print("Before diffInYesAndNo:" + str(diffInYesAndNo))
print("-------------------------------------------")
print("After numOfYes:" + str(privateNumOfYes))
print("After numOfNo:" + str(privateNumOfNo))
print("After diffInYesAndNo:" + str(privateDiffInYesAndNo))
print("-------------------------------------------")
print("Percentage error in Yes is: " + str(percentageErrorInYes))
print("Percentage error in No is: " + str(percentageErrorInNo))
print("Percentage error in Diff is: " + str(percentageErrorInDiff))

# Epsilon is 3 to the ratio is ln(3)
