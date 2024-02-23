import pprint
massage_lines = []
print('Enter your massage (type "done" on a new line when finished):')
while True:
    line = input()
    if line.lower() == 'done':
        break
    massage_lines.append(line)

massage = '\n'.join(massage_lines)

count = {}

for character in massage.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
total_count = sum(count.values())
print('Total count of characters:' , total_count)