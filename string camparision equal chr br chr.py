def stringcampare(s1,s2):
    if len(s1)<len(s2):
        print('string not same')
    elif len(s2)<len(s1):
        print('string are not same')
    else:
        resul=True
        for a in range (len(s1)):
            if s1[a]!=s2[a]:
                result=False
        if result==True:
            print('string are same')
        else:
            print('string are not same')
str1=input('enter the first string=')
str2=input('enter the second string=')
stringcampare(str1,str2)
         
        
