from difflib import SequenceMatcher
with open("demo1.txt") as first:
    with open("demo2.txt") as second:
        d1 = first.read()
        d2 = second.read()
check = SequenceMatcher(None, d1, d2).ratio()
match = check * 100
print(f"The percent of plagiarism is {match}")