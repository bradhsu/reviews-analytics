data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count  += 1
		if count % 1000 == 0:
			print(len(data))

print('Finish reading', 'Total ', len(data), 'lines')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('The average length of the reviews is ', sum_len/len(data))

wc = {} # word count
for d in data :
	words = d.split() # = split(' ')
	for word in words:
		if word in wc:  # if word not in wc
			wc[word] += 1 # valve + 1 

		else:
			wc[word] = 1 # add new key

for word in wc:
	if wc[word] > 100:
		print(word, wc[word])
print(len(wc))


while True:
	word = input('Enter a word: ')
	if word == 'q':
		break
	if word in wc:
		print(word, ':',  wc[word], 'times')
	else:
		print('Count = 0')

print('Thanks for using')