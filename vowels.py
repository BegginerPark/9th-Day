vowels = ['a', 'e', 'i', 'o', 'u']

word = "Milliways"

for letter in word:
    if letter in vowels:
        print(letter)


found = []
len(found)
found.append('a')
len(found)
found.append('e')
found.append('i')
len(found)

if 'u' not in found:
    found.append('u')

len(found)
found

######################################

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to serch for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

#####################################

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to serch for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

#####################################
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)