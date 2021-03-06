import random
import math

# Configure paths to your dataset files here
DATASET_FILE = 'metadata_mammoset_ddsm_7.csv'
FILE_TRAIN = 'train_metadata_mammoset_ddsm_7.csv'
# FILE_VALID = 'validation.csv'
FILE_TESTS = 'test_metadata_mammoset_ddsm_7.csv'

# Set to true if you want to copy first line from main
# file into each split (like CSV header)
IS_CSV = True

# Make sure it adds to 100, no error checking below
PERCENT_TRAIN = 70
# PERCENT_VALID = 0
PERCENT_TESTS = 30

data = [l for l in open(DATASET_FILE, 'r')]

train_file = open(FILE_TRAIN, 'w')
# valid_file = open(FILE_VALID, 'w')
tests_file = open(FILE_TESTS, 'w')

if IS_CSV:
    train_file.write(data[0])
    # valid_file.write(data[0])
    tests_file.write(data[0])
    data = data[1:len(data)]

num_of_data = len(data)
num_train = int((PERCENT_TRAIN / 100.0) * num_of_data)
# num_valid = int((PERCENT_VALID/100.0)*num_of_data)
num_tests = math.ceil((PERCENT_TESTS / 100.0) * num_of_data)

data_fractions = [num_train, num_tests]
split_data = [[], []]

rand_data_ind = 0

for split_ind, fraction in enumerate(data_fractions):
    for i in range(fraction):
        rand_data_ind = random.randint(0, len(data) - 1)
        split_data[split_ind].append(data[rand_data_ind])
        data.pop(rand_data_ind)

for l in split_data[0]:
    train_file.write(l)

# for l in split_data[1]:
#     valid_file.write(l)

for l in split_data[1]:
    tests_file.write(l)

train_file.close()
# valid_file.close()
tests_file.close()
