book1_file = open('kak.txt', 'r')
book2_file = open('goodhunting.txt', 'r')
book1 = book1_file.read()
book2 = book2_file.read()

book1 = book1.lower()
words = book1.split()
words = [word.strip('.,!;()[]?') for word in words]
words = [word.replace("'s", '') for word in words]

book2 = book2.lower()
words2 = book2.split()
words2 = [word2.strip('.,!;()[]?') for word2 in words2]
words2 = [word2.replace("'s", '') for word2 in words2]

unique1 = []
for word in words:
    if word not in unique1:
        unique1.append(word)

unique2 = []
for word2 in words2:
    if word2 not in unique2:
        unique2.append(word2)

unique1.sort()
unique2.sort()

print("The total amount of unique words in the first book are: ", len(unique1))
print("The total amount of unique words in the second book are: ", len(unique2))

if len(unique1) > len(unique2):
    print("it seems like the first book has more unique words than the second book")
elif len(unique1) < len(unique2):
    print("it seems like the second book has more unique words than the first book")
elif len(unique1) == len(unique2):
    print("it seems like both books have the same amount of unique words")


distinct1 = []
for word in unique1:
    if len(word) >= 7:
        distinct1.append(word)

distinct2 = []
for word2 in unique2:
    if len(word2) >= 7:
        distinct2.append(word2)

distinct2.sort()
distinct1.sort()

print("The total amount of distinct words in the first book that has more than 7 characters is: ", len(distinct1))
print("The total amount of distinct words in the second book that has more than 7 characters is: ", len(distinct2))

if len(distinct1) > len(distinct2):
    print("it seems like the first book has more unique words that contains 7 or more characters than the second book")
elif len(distinct1) < len(distinct2):
    print("it seems like the second book has more unique words that contains 7 or more characters than the first book")
elif len(distinct1) == len(distinct2):
    print("it seems like both books have the same amount of unique words that contains 7 or more characters")

div1 = int(len(unique1))
div2 = int(len(unique2))
div_1 = int(len(words))
div_2 = int(len(words2))

wide_vocab = div1/div_1
wide_vocab2 = div2/div_2

print("The result of the division between the number of distinct words and the total number of words in the first book: ", wide_vocab)
print("The result of the division between the number of distinct words and the total number of words in the second book: ", wide_vocab2)

if wide_vocab > wide_vocab:
    print("No, this does not change the previous answer, the first book disposes the wider vocabulary compared to the number of words")
else:
    print("Yes, this does change the previous answer, the second book has a wider vocabulary compared to the number of words")








