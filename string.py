#Write a program to input a string and display its length without using the len() function.
# text="hello, world"
# count=0
# for i in text:
#     count+=1
# print("length of string is:",count)     

#Count the number of vowels, consonants, digits, spaces, and special characters in a given string.
# text="Hellow,@world 123"
# vowels=0
# consonants=0
# digits=0
# spaces=0
# special=0
# for i in text:
#     if i in 'aeiouAEIOU':
#         vowels+=1
#     elif i.isalpha():
#         consonants+=1
#     elif i.isdigit():
#         digits+=1
#     elif i.isspace():
#         spaces+=1
#     else:
#         special+=1

# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)
# print("Number of digits:", digits)
# print("Number of spaces:", spaces)
# print("Number of special characters:", special)

#Reverse the given string without using built-in reverse functions. 
# text="Hello, World!"
# reversed_str=""
# for i in text:
#     reversed_str=i+reversed_str
# print("Reversed string:", reversed_str)

#check if string is palindrome or not
# text="tat"
# reversed_str=text[::-1]
# if text==reversed_str:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#uppercase and lowercase count
# text="I am a DYP student"
# count1=0
# count2=0
# for i in text:
#     if i.isupper():
#         count1+=1
#     elif i.islower():
#         count2+=1
# print("Number of uppercase letters:", count1)
# print("Number of lowercase letters:", count2)

#Replace all occurrences of a given character with another character.
# text="Hello, World!"
# ch='o'
# new_ch='a'
# text=text.replace(ch, new_ch)
# print("Modified string:", text)

#remove spaces from the input string
# text="welcome to python"
# text=text.strip()
# print("String after removing spaces:", text)

#frequency of each character
# text="i am a nnice little girl"
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print("Frequency of each character:", freq)

#first and last character
# text =input("Enter a string: ")
# print("First character of the string:", text[0])
# print("Last character of the string:", text[-1])

#ASCII values
# for i in range(65,91):
#     print(i,"=",chr(i))

#word count in a sentence
# text=input("Enter a sentence: ")
# words=text.split()
# count=0
# for i in words:
#     count+=1
# print(count)    

#longest word
# text=input("Enter a sentence: ")
# words=text.split()
# longest_word=words[0]
# for i in words:
#     if len(i)>len(longest_word):
#         longest_word=i
#     else:
#         pass
# print(longest_word) 

#shortest word
# text=input("Enter a sentence: ")
# words=text.split()
# shortest_word=words[0]
# for i in words:
#     if len(i)<len(shortest_word):
#         shortest_word=i
#     else:
#         pass
# print(shortest_word)

#tittle case
# text=input("Enter a sentence: ")
# tittle_case=text.title()
# print(tittle_case)

# print non duplicate characters
# text=input("Enter a string: ")
# text=text.replace(" ","")
# new_text=""
# for i in text:
#     if i not in new_text:
#         new_text+=i
#     else:
#         pass
# print(new_text)        

#character frequency
# text=input("Enter a string: ")
# freq={}
# text=text.replace(" ","")
# for i in text:
#     if i not in freq:
#         freq[i]=1
#     elif i in freq:
#         freq[i]+=1
# print(freq)    

#anagram check
# text1=input("Enter first string: ")
# text2=input("Enter second string: ")
# text1=text1.replace(" ","")
# text2=text2.replace(" ","")
# if sorted(text1)==sorted(text2):
#     print("The strings are anagrams.")
# else:                                 
#     print("The strings are not anagrams.")

#print duplicate characters
# text=input("Enter a string: ")
# freq={}
# dups=[]
# text=text.replace(" ","")
# for i in text:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
#         if i not in dups:
#          dups.append(i)  
# print(dups)

#Check whether a given substring exists in the main string.     
# text=input("Enter the main string: ")
# substring=input("Enter the substring: ")
# if substring in text:
#     print("The substring exists in the main string.")
# else:
#     print("The substring does not exist in the main string.")   

#Count how many times a specific word appears in a sentence. 
# text=input("Enter a sentence: ")
# word=input("Enter the word to count: ")
# count=0
# text=text.split()
# for i in text:
#     if i==word:
#         count+=1
#     else:
#         pass
# print(word,"=",count)    

#password validation
password=input("Enter a password: ")
password=password.replace(" ","")
if len(password)>=8:
    for i in password:
        if i.isupper():
            for j in password:
                if j.islower():
                    for k in password:
                        if k.isdigit():
                            for l in password:
                                if l in "!@#$%^&*()_+-=~`":
                                    print("Valid password")
                                    break
                            else:
                                print("Invalid password: must contain at least one special character.")
                                break
                    else:
                        print("Invalid password: must contain at least one digit.")
                        break
            else:
                print("Invalid password: must contain at least one lowercase letter.")
                break
    else:
        print("Invalid password: must contain at least one uppercase letter.")
else:
    print("Invalid password: must be at least 8 characters long.")  
        