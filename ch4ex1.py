#!/usr/bin/python

#Excercise 1 from Chapter 4
spam = ['apples','bananas','tofu','cats']

def structlist(lists):
    sstring = ""
    for i in range(len(lists)):
        if i == len(lists)-1:
            sstring +="and "+lists[i]
            print(sstring)
            break
        else:
            sstring += lists[i]+", "

structlist(spam)
spam.append("lions")
#This should prove that the size of the list wont matter.
structlist(spam)
