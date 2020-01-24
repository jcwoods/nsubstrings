# nsubstrings
Utility module to split an input string 's' into all possible sets of 'n' non-overlapping substrings.  

Splits the string 's' into all possible sets of 'n' non-overlapping
substrings.  The order of charaters in the input string is preserved
(eg, no permutations on the input).
    
Result is returned as a list of tuples.

For example:

    substrings('foobard', 3):
    [(f o obard),  (fo o bard),  (foo b ard),  (foob a rd),  (fooba r d),
     (f oo bard),  (fo ob ard),  (foo ba rd),  (foob ar d),       
     (f oob ard),  (fo oba rd),  (foo bar d),
     (f ooba rd),  (fo obar d),
     (f oobar d)]
