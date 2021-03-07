x = 5; y = 7

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x equals y")

print("-"*80)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for char in quote:
    if char.isupper():
        print(char)

print("-"*80)

for i in range(0, 10):
    print(i)

print("-"*80)

for i in range(0, 101, 7):
    print(i)

print("-" * 80)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

print("-" * 80)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)