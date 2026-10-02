# Read the sentence
sentence = input().strip()

# Reverse the words and print
word_list = sentence.split()

word_list.reverse()
# print(word_list)
reversed_sentence = ""
for word in word_list:
  reversed_sentence += word + " "
#print(word_list)
print(reversed_sentence)