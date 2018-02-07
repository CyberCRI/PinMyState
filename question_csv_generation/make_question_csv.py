# For Python 3+

import csv
import sys
import itertools

### Constants
column_names_per_question = ([
    'question_{0}_category', 
    '@question_{0}_category_icon', 
    'question_{0}_text', 
    'question_{0}_choice_a',
    'question_{0}_choice_b',
    'question_{0}_choice_c',
    'question_{0}_choice_d',
    'question_{0}_answer_letter', 
    'question_{0}_answer_text' 
    ])

category_to_icon_filenames = {
    'Movies & Music': 'movies.png',
    'Politics & Activism': 'politics.png',
    'Architecture & Artwork': 'architecture.png',
    'Literature': 'literature.png',
    'Clothes & Jewelry': 'clothes.png',
    'Food': 'food.png',
    'Nature & Geography': 'nature.png',
    'Wild': 'wild.png'
} 

question_limit = 7


### Program

# 1st argument is input filename, 2nd argument is output filename
input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Build up list of questions
reader = csv.DictReader(open(input_filename), dialect=csv.excel_tab)
questions = list(reader) 

# Remove empty questions 
questions = (q for q in questions if q['ID'] != '')
# Remove extra whitespace in all fields
questions = (dict(zip(q.keys(), (v.strip() for v in q.values()))) for q in questions)


# Break into sub-lists by state
questions_by_state = {}
for state, state_questions in itertools.groupby(questions, key=lambda q: q['State']):
    questions_by_state[state] = list(state_questions)


# Prepare to write questions
question_column_names = [name.format(i) for i in range(1, question_limit + 1) for name in column_names_per_question]
column_names = ['state'] + question_column_names
writer = csv.DictWriter(open(output_filename, 'w'), fieldnames=column_names, dialect=csv.excel_tab)
writer.writeheader()

# Go through states in alphabetical order
states = sorted(questions_by_state.keys())

for state in states:
    # Build up list of data
    row = {'state': state}
    for i, question in zip(itertools.count(), questions_by_state[state]):
        if i >= question_limit: 
            print("WARNING: Extra (unused) questions for state", state, file=sys.stderr)
            break

        row['question_{0}_category'.format(i+1)] = question['Category']
        row['@question_{0}_category_icon'.format(i+1)] = category_to_icon_filenames[question['Category']]
        row['question_{0}_text'.format(i+1)] = question["Question"]
        row['question_{0}_choice_a'.format(i+1)] = question["A"]
        row['question_{0}_choice_b'.format(i+1)] = question["B"]
        row['question_{0}_choice_c'.format(i+1)] = question["C"]
        row['question_{0}_choice_d'.format(i+1)] = question["D"]
        row['question_{0}_answer_letter'.format(i+1)] = question["Answer"]
        row['question_{0}_answer_text'.format(i+1)] = question[question["Answer"]]
    writer.writerow(row)

