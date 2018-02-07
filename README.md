# Pin My State

Pin My State is a trivia game in which players compete to get ingredients for their recipes by answering questions about states and territories where those ingredients come from.


## Scripts

To generate the TSV files used by InDesign data merge, use the Python 3 script `make_question_csv.py`. It takes two command-line arguments: the name of the input file, expected to be an TSV export of a [Pin My State Google Sheet](https://docs.google.com/spreadsheets/d/1PwKo_1E2EcmDthNvp1DyH3nxZcN1zOH2C0Mjqn2RvPs/edit?usp=sharing), and the output TSV file.

It will cap the number of questions at 7 (first-in, first-out), and print warnings if extra questions are available.

To convert them all, use a command like: 

```
for file in questions/*; do python3 make_question_csv.py $file generated/$(basename $file); done
```

Next, merge the files into one using the merge_question_csv.py. It takes the regional CSV file names as the first parameters, and the merged file name as the last:

```
python3 merge_question_csv.py generated/north.tsv generated/east.tsv generated/west.tsv generated/south.tsv generated/central.tsv generated/north_east.tsv generated/ut.tsv  generated/merged.tsv 
``` 

Finally, the script `find_states.py` simply takes the merged CSV file in the first argument and lists the unique state names along with their region in the second argument. 

```
python3 find_states.py generated/merged.tsv generated/states.tsv
```


## Credits

Initial prototype by Gayathri Gopalakrishnan.
Further game design by Radhika Beaume and Jesse Himmelstein.
Trivia questions by Ameya Murukutla.
Graphic design by Radhika Beaume.

Pin My State was created by the CRI Game Lab and ZMQ as part of the IncLudo project. This work was made possible with the support of the European Instrument for Democracy and Human Rights (EIDHR). 
