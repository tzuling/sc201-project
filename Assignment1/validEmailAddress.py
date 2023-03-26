"""
File: validEmailAddress.py
Name: 
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO:
"""

WEIGHT = [                           # The weight vector selected by Jerry
    [0.4],                           # (see assignment handout for more details)
    [0.4],
    [0.2],
    [0.2],
    [0.9],
    [-0.65],
    [0.1],
    [0.1],
    [0.1],
    [-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
    maybe_email_list = read_in_data()
    y = [0] * 13 + [1] * 13
    predict_y = []
    rightNum= 0
    for enum, maybe_email in enumerate(maybe_email_list):
        feature_vector = feature_extractor(maybe_email)
        score = 0
        for i in range(len(WEIGHT)):
            score += sum(feature_vector[i] * WEIGHT[i])

        if score > 0:
            predict_y.append(1)
        else:
            predict_y.append(0)
        # print(f"score: {score}")

        if predict_y[enum] == y[enum]:
            rightNum+= 1

    #Accuracy of this model
    # print(y)
    # print(predict_y)
    print(f"Accuracy of this model: {rightNum/len(y)}")


def feature_extractor(maybe_email):
    """
    :param maybe_email: str, the string to be processed
    :return: list, feature vector with 10 values of 0's or 1's
    """
    print(maybe_email)
    feature_vector = [0] * len(WEIGHT)
    for i in range(len(feature_vector)):
        if i == 0:
            feature_vector[i] = 1 if '@' in maybe_email else 0
            # print(f"'@' in the string: {feature_vector[i]}")
        elif i == 1:
            if feature_vector[0]:
                feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
            # print(f"No '.' before '@': {feature_vector[i]}")
        elif i == 2:
            if feature_vector[0]:
                feature_vector[i] = 1 if maybe_email.find('@')>0 else 0
            # print(f"Some strings before '@': {feature_vector[i]}")
        elif i == 3:
            if feature_vector[0]:
                feature_vector[i] = 1 if len(maybe_email)-maybe_email.rfind('@')-1>0 else 0
            # print(f"Some strings after '@': {feature_vector[i]}")
        elif i == 4:
            if feature_vector[0] and '.' in maybe_email:
                feature_vector[i] = 1 if '.' in maybe_email[maybe_email.find('@'):] else 0
            # print(f"There is '.' after '@': {feature_vector[i]}")
        elif i == 5:
            feature_vector[i] = 1 if ' ' not in maybe_email else 0
            # print(f"There is no white space: {feature_vector[i]}")
        elif i == 6:
            feature_vector[i] = 1 if maybe_email.endswith('.com') else 0
            # print(f"Ends with '.com': {feature_vector[i]}")
        elif i == 7:
            feature_vector[i] = 1 if maybe_email.endswith('.edu') else 0
            # print(f"Ends with '.edu': {feature_vector[i]}")
        elif i == 8:
            feature_vector[i] = 1 if maybe_email.endswith('.tw') else 0
            # print(f"Ends with '.tw': {feature_vector[i]}")
        elif i == 9:
            feature_vector[i] = 1 if len(maybe_email) > 10 else 0
            # print(f"Length > 10: {feature_vector[i]}")
        
    # print(f'feature_vector: {feature_vector}')
    return feature_vector


def read_in_data():
    """
    :return: list, containing strings that might be valid email addresses
    """
    valid_email_list = []
    with open(DATA_FILE) as f:
        valid_email_list = [line.strip('\n') for line in f]
    return valid_email_list


if __name__ == '__main__':
    main()
