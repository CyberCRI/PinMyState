# Pin My State

Pin My State is a trivia game in which players compete to get ingredients for their recipes by answering questions about states and territories where those ingredients come from.


## Scripts

To generate the TSV files used by InDesign data merge, use the Python 3 script `make_question.csv.py`. It takes two command-line arguments: the name of the input file, expected to be an TSV export of a [Pin My State Google Sheet](https://docs.google.com/spreadsheets/d/1PwKo_1E2EcmDthNvp1DyH3nxZcN1zOH2C0Mjqn2RvPs/edit?usp=sharing), and the output TSV file.

It will cap the number of questions at 7 (first-in, first-out), and print warnings if extra questions are available.


## Credits

Initial prototype by Gayathri Gopalakrishnan.
Further game design by Radhika Beaume and Jesse Himmelstein.
Trivia questions by Ameya Murukutla.
Graphic design by Radhika Beaume.

Pin My State was created by the CRI Game Lab and ZMQ as part of the IncLudo project. This work was made possible with the support of the European Instrument for Democracy and Human Rights (EIDHR). 
