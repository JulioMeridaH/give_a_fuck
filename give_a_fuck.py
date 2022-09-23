""" This code is intended to summarize in Python programming language
the content of the book "The Subtle Art of Not Giving a Fuck" by Mark Manson.
Although the main purpose is the eye-reading of the code, it can be used
for real if you set your own list in things_that_matter and try to run
the code with a thing that you could be considering if its worthy of
giving a fuck, if you respect the syntax, obviously.

Coded by @JulioMeridaH
https://linktr.ee/juliomeridah
"""

def give_a_fuck(thing):
    give_a_fuck=False
    things_that_matter=["vit1","vit2","..."]
    for vit in things_that_matter:    
        if thing==vit:
            give_a_fuck=True
            break
    if give_a_fuck==True:
        return "Yes, give a fuck!"
    else:
        return "Don't give a fuck!"

if __name__=='__main__':
    print(give_a_fuck(thing))