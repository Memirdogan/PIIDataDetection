"""
In our example, we are evaluating the performance of a medical test. Assuming our model has a precision of 0.1 and a
recall of 0.9, we can calculate the F-beta score (beta=5) using the following steps:

True Positives (TP): 90 (Correctly estimated number of people with true disease)
False Positives (FP): 810 (Number of actually healthy people incorrectly predicted to be diseased)
False Negatives (FN): 10 (Number of people mistakenly estimated as healthy who were actually diseased)
True Negatives (TN): 90 (Correctly estimated number of actually healthy people)
"""
TP = 90 # True Positive
FP = 810 # False Positive
FN = 10 # False Negative

# First step, lets calculate Precision
precision = TP / (TP + FP)

# now let's calculate recall
recall = TP / (TP + FN)

# Let's assign our beta value given in the example
beta = 5

# calculate the F-Score
Fbeta = (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)

# Print values
print("Precision:", precision)
print("Recall:", recall)
print("F-beta Score (beta={}):".format(beta), Fbeta)

#################
# example 2
#################
"""
I also wanted to share a guide on evaluating model performance using the F-beta score with an example where precision 
is 0.9 and recall is 0.1. In this example, we are assessing a model's performance in a medical test. The given values are as follows:

True Positives (TP): 90
False Positives (FP): 10
False Negatives (FN): 810
True Negatives (TN): 90
"""
TP = 90 # True Positive
FP = 10 # False Positive
FN = 810 # False Negative

# Calculate precision
Precision = TP / (TP + FP)

# Calculate Recall
Recall = TP / (TP + FN)

# Beta
Beta = 5

# F-Score
FScore = (1 + Beta**2) * (Precision * Recall) / ((Beta**2 * Precision) + Recall)

# Print
print("Precision: ", Precision)
print("Recall: ", Recall)
print("F-beta Score (beta={}): ".format(Beta), FScore)