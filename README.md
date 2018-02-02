# pdfchallenges
Three challenges including a Bucket challenge, a Number2Words generator, and a file identifier

NumberToWord: 
By far the most difficult of these challenges, just because of the creative aspect. I decided upon a number to color idea, where I will take an input of 10-20 digit number and parse it into respective rgb up to triples. 
Therein lay a problem: not all rgb colors are triples, so I will probably randomly choose two digits from the original number to do that with, or I could do if the original number is not divisible by three, do permutations of the original number so you can actually access an rgb number like (12,34,56). It cannot be random, because then you can never get the same color word back with the same input, so I have to make a consistent way of getting it. 

ANOTHER ISSUE, RGB IS RESTRICTED TO 0-255!!!! how do I make sure the values stay within 0-255??



