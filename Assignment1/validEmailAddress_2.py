"""
File: validEmailAddress_2.py
Name: 
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.

feature1:  contains symbol list=[!,#,$,%,^,&,",*,(,),/,=,?,{,},|,\\]: -0.4
feature2:  Only one '@' in the string and not in "": 0.1
feature3:  if feature2 is true and there are some strings before '@' and after '@': 0.1
feature4:  if feature3 is true and len of string after '@' must above 8 and the string after '@' can't contain any symbol_list: 0.2
feature5:  feature4 is true and Ends with either '.com','.tw','.edu','.org','.net': 0.2
feature6:  if feature3 is not true: -0.9
feature7:  if feature2 is true and if the string before '@' contains "", "" previous must be '.': -0.6
feature8:  if feature3 is true and '@' previous element and next element is not '.': -0.7
feature9:  There is white space: -0.9
feature10:  There is no string before or after in every '.' and '.' can't be the first or end: -0.7
feature11:  the string before '@' must contains at least two feature (symbol(weight=1),letters(weight=2),numbers(weight=2))


Accuracy of your model: 1.0
"""

import numpy as np
import re

WEIGHT = [                           # The weight vector selected by you
	[-0.3],                              # (Please fill in your own weights)
	[0.1],
	[0.1],
	[0.2],
	[0.2],
	[-0.9],
	[-0.6],
	[-0.7],
	[-0.9],
	[-0.7],
	[-0.4]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	y = [0] * 13 + [1] * 13
	predict_y = []
	weight_vector = np.array(WEIGHT).T
	score = 0
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		score = weight_vector.dot(feature_vector)
		# for i in range(len(WEIGHT)):
		# 	score += sum(feature_vector[i] * WEIGHT[i])

		if score > 0:
			predict_y.append(1)
		else:
			predict_y.append(0)
        # print(f"score: {score}")

	rightNum= 0
	for i in range(len(y)):
		if predict_y[i] == y[i]:
			rightNum+= 1

    #Accuracy of this model
	print(y)
	print(predict_y)
	print(f"Accuracy of this model: {rightNum/len(y)}")


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	# Initialize an array with 11 rows, 1 col
	feature_vector = np.zeros((11,1))
	# Remove every thing in ""
	maybe_email_ori = maybe_email
	maybe_email = re.sub(r"\".*\"","\"\"",maybe_email)
	# symbol_list
	symbol_list = ['!','#','$','%','^','&','\"','*','(',')','/','=','?','{','}','|','\\']
	endswith_list = ['.com','.tw','.edu','.org','.net']
	# print(maybe_email)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i][0] = 1 if bool(len([ele for ele in symbol_list if(ele in maybe_email)])) else 0
			# print(f"contains symbol list: {feature_vector[i][0]}")
		elif i == 1:
			feature_vector[i][0] = 1 if maybe_email.count('@')==1 else 0
			# print(f"Only one '@' in the string: {feature_vector[i][0]}")
		elif i == 2: 
			if feature_vector[1]:
				feature_vector[i][0] = 1 if (len(maybe_email.split('@')[0]) > 0 and len(maybe_email.split('@')[1]) > 0) else 0
			# print(f"There are some strings before '@' and after '@': {feature_vector[i][0]}")
		elif i == 3:
			if feature_vector[2]:
				feature_vector[i][0] = 1 if ( len(maybe_email.split('@')[1]) >= 8 and len([ele for ele in symbol_list if(ele in maybe_email.split('@')[1])])==0 ) else 0
			# print(f"len of string after '@' >=8 and the string after '@' didn't contains symbol list: {feature_vector[i][0]}")
		elif i == 4:
			if feature_vector[3]:
				feature_vector[i][0] = 1 if bool(len([ele for ele in endswith_list if(maybe_email.split('@')[1].endswith(ele))])) else 0
			# print(f"Ends with endswith_list: {feature_vector[i][0]}")
		elif i == 5:
			feature_vector[i][0] = 1 if not feature_vector[2] else 0
			# print(f"feature3 is not true: {feature_vector[i][0]}")
		elif i == 6:
			if feature_vector[1]:
				if maybe_email.split('@')[0].find('\"\"') > 0:
					feature_vector[i][0] = 0 if (maybe_email[maybe_email.split('@')[0].find('\"\"')-1] == '.') else 1
			# print(f" if feature2 is true and if the string before '@' contains "", "" previous must be '.': {feature_vector[i][0]}")
		elif i == 7:
			if feature_vector[3]:
				feature_vector[i][0] = 1 if (maybe_email[maybe_email.find('@')-1] == '.' or maybe_email[maybe_email.find('@')+1] == '.') else 0
			# print(f"'@' previous element and next element is '.': {feature_vector[i][0]}")
		elif i == 8:
			feature_vector[i][0] = 1 if ' ' in maybe_email else 0
			# print(f"There is white space: {feature_vector[i][0]}")
		elif i == 9:
			feature_vector[i][0] = 0
			dots_index = []
			for ele in range(len(maybe_email)):
				if maybe_email[ele] == '.':
					dots_index.append(ele)
					if ele==0 or ele==len(maybe_email)-1:
						feature_vector[i][0] = 1
			if len(dots_index) > 1:
				for idx in range(len(dots_index)-1):
					if dots_index[idx+1]-dots_index[idx] ==1:
						feature_vector[i][0] = 1
			# print(f"There is no string before or after in every '.': {feature_vector[i][0]}")
		elif i == 10:
			features = 0
			if bool(re.search('[a-zA-Z]', maybe_email_ori.split('@')[0])):
				features+=2
			if bool(re.search(r'\d', maybe_email_ori.split('@')[0])):
				features+=2
			if bool(len([ele for ele in symbol_list if(ele in maybe_email_ori.split('@')[0])])):
				features+=1
			feature_vector[i][0] = 1 if features < 2 else 0
			# print(f"the string before '@' must contains at least two feature: {feature_vector[i][0]}")
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	valid_email_list = []
	with open(DATA_FILE) as f:
		valid_email_list = [line.strip('\n') for line in f]
	return valid_email_list


if __name__ == '__main__':
	main()
