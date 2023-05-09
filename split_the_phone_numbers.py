import re


N = int(input())
for _ in range(N):
    number = input()
    match = re.match(r"(\d{3})[- ](\d{3})[- ](\d{4,10})", number)
    print(match)
    print(f"CountryCode={match.groups(1)},LocalAreaCode={match.groups(2)},Number={match.groups(3)}")
