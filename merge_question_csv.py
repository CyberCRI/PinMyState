# For Python 3+

import csv
import sys
import itertools
import pathlib


# First arguments are the regional CSV files, last argument is the merged output file
[_, *input_filenames, output_filename] = sys.argv

# Build up list of questions
questions = []

for input_filename in input_filenames:
    # The region name is the "stem" of the filename
    region = pathlib.PurePath(input_filename).stem

    reader = csv.DictReader(open(input_filename), dialect=csv.excel_tab)
    for question in reader:
        question['region'] = region
        question['@region_icon'] = region + '.png'
        questions.append(question)

# Time to write
column_names = questions[0].keys()
writer = csv.DictWriter(open(output_filename, 'w'), fieldnames=column_names, dialect=csv.excel_tab)
writer.writeheader()

for question in questions:
    writer.writerow(question)

