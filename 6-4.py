word = raw_input('Enter string: ')
find = raw_input('Enter character to found: ')

count = 0
for letter in word:
    if letter == find:
        count = count + 1
print count

