import sys

def nsubstrings(s:str, n:int):
    '''
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
    '''

    tuples = list()
    for i in range(1, len(s)):
       pre = s[0:i] 
       post = s[i:] 

       if n == 2:
           tuples.append( (pre, post) )
       else:
           subs = nsubstrings(post, n - 1)
           p = (pre,)
           for t in subs:
               tuples.append(p + t)

    return tuples


def main(args):
    n = int(args[1])
    for arg in args[2:]:
        tuples = nsubstrings(arg, n)
        print(str(tuples))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))