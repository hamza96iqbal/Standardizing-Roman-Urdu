
#please refer to readme file for details of every step 

#importing libraries
import math
import re

#using a custom text for standardizing, it can be any thing
text="mera naam hamzah hai me lahore se ho me ne parhai bhi lahoree ssse hih ki hay mera piyo tajarat krta hai meryi ma ghar sambhalti hai mene camputer scaince parhi hoi hai or main abh nauakari dhoondh raha ho"

#predefined variable
procededbyI="bcdefghijklmnopqrtuvwxyz"
procededbyH="acefghijlmnoqrstuvwxyz"

#creating list of substring by using split function so we apply rules word by word
text=text.split(" ")

#using for loop to pick words from list one by one
for length in range(0,len(text)):
#rule 1
    text[length] = re.sub('ain$', 'ein', text[length])
    
#rule 2
    text[length]=text[length][0]+text[length][1:].replace("ar","r")

#rule 3
    text[length]=text[length].replace("ai","ae")

#rule 4
    text[length] = re.sub('iy+', 'I', text[length])
    
#rule 5
    text[length] = re.sub('ay$', 'e', text[length])

#rule 6
    text[length] = re.sub('ih+', 'eh', text[length])
    
#rule 7
    text[length] = re.sub('ey$', 'e', text[length])

#rule 8
    text[length] = re.sub('s+', 's', text[length])

#rule 9
    text[length] = re.sub('ie$', 'y', text[length])
    
#rule 10
    text[length]=text[length][:-1].replace("ry","ri")+text[length][-1]

#rule 11
    text[length] = re.sub('^es', 'is', text[length])
    
#rule 12
    text[length]=text[length][:-1].replace("sy","si")+text[length][-1]
    
#rule 13
    text[length] = re.sub('a+', 'a', text[length])
    
#rule 14    
    text[length]=text[length][:-1].replace("ty","ti")+text[length][-1]
    
#rule 15
    text[length] = re.sub('j+', 'j', text[length])
    
#rule 16
    text[length] = re.sub('o+', 'o', text[length])
    
#rule 17
    text[length] = re.sub('(ee)+', 'i', text[length])

#rule 18
    if(len(text[length])>1):
        if text[length][-1] in 'i' and text[length][-2] in procededbyI:
            text[length]=text[length][:-1]+"y"

#rule 19s
    text[length] = re.sub('d+', 'd', text[length])
    
#rule 20
    text[length] = re.sub('u', 'o', text[length])
    
#rule 21
    if(len(text[length])>1):
        if text[length][-1] in 'h' and text[length][-2] in procededbyH:
            text[length]=text[length][:-1]

text=" ".join(text)

