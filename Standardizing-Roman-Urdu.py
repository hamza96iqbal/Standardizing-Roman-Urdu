
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
for index in range(0,len(text)):
#rule 1
    text[index] = re.sub('ain$', 'ein', text[index])
    
#rule 2
    text[index]=text[index][0]+text[index][1:].replace("ar","r")

#rule 3
    text[index]=text[index].replace("ai","ae")

#rule 4
    text[index] = re.sub('iy+', 'I', text[index])
    
#rule 5
    text[index] = re.sub('ay$', 'e', text[index])

#rule 6
    text[index] = re.sub('ih+', 'eh', text[index])
    
#rule 7
    text[index] = re.sub('ey$', 'e', text[index])

#rule 8
    text[index] = re.sub('s+', 's', text[index])

#rule 9
    text[index] = re.sub('ie$', 'y', text[index])
    
#rule 10
    text[index]=text[index][:-1].replace("ry","ri")+text[index][-1]

#rule 11
    text[index] = re.sub('^es', 'is', text[index])
    
#rule 12
    text[index]=text[index][:-1].replace("sy","si")+text[index][-1]
    
#rule 13
    text[index] = re.sub('a+', 'a', text[index])
    
#rule 14    
    text[index]=text[index][:-1].replace("ty","ti")+text[index][-1]
    
#rule 15
    text[index] = re.sub('j+', 'j', text[index])
    
#rule 16
    text[index] = re.sub('o+', 'o', text[index])
    
#rule 17
    text[index] = re.sub('(ee)+', 'i', text[index])

#rule 18
    if(len(text[index])>1):
        if text[index][-1] in 'i' and text[index][-2] in procededbyI:
            text[index]=text[index][:-1]+"y"

#rule 19s
    text[index] = re.sub('d+', 'd', text[index])
    
#rule 20
    text[index] = re.sub('u', 'o', text[index])
    
#rule 21
    if(len(text[index])>1):
        if text[index][-1] in 'h' and text[index][-2] in procededbyH:
            text[index]=text[index][:-1]

text=" ".join(text)

