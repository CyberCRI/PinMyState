# For Python 3+

import csv
import sys
import itertools
import pathlib


# 1st argument is input filename, 2nd argument is output filename
input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Build up set of (state, region) tuples
states_and_regions = set()

reader = csv.DictReader(open(input_filename), dialect=csv.excel_tab)
for question in reader:
    states_and_regions.add((question['state'], question['region']))

# Time to write
column_names = ['state', 'region', '@region_icon']
writer = csv.DictWriter(open(output_filename, 'w'), fieldnames=column_names, dialect=csv.excel_tab)
writer.writeheader()

for (state, region) in states_and_regions:
    writer.writerow({
        'state': state, 
        'region': region, 
        '@region_icon': region + '.png'
    })

