data = [
    {"index": 0, "outlook": "Sunny", "play": "Yes"},
    {"index": 1, "outlook": "Rainy", "play": "No"},
    {"index": 2, "outlook": "Overcast", "play": "Yes"},
    {"index": 3, "outlook": "Sunny", "play": "No"},
    {"index": 4, "outlook": "Rainy", "play": "No"},
    {"index": 5, "outlook": "Sunny", "play": "Yes"},
    {"index": 6, "outlook": "Overcast", "play": "Yes"},
    {"index": 7, "outlook": "Rainy", "play": "Yes"},
    {"index": 8, "outlook": "Sunny", "play": "No"},
    {"index": 9, "outlook": "Sunny", "play": "Yes"},
    {"index": 10, "outlook": "Rainy", "play": "Yes"},
    {"index": 11, "outlook": "Overcast", "play": "Yes"},
    {"index": 12, "outlook": "Sunny", "play": "No"},
    {"index": 13, "outlook": "Overcast", "play": "No"}
]

play_yes_count = len([item for item in data if item["play"] == "Yes"])
play_no_count = len(data) - play_yes_count

outlook_sunny = len([item for item in data if item["outlook"] == "Sunny"])
sunny_yes = len([item for item in data if item["outlook"] == "Sunny" and item["play"] == "Yes"])
sunny_no = outlook_sunny - sunny_yes

outlook_rainy = len([item for item in data if item["outlook"] == "Rainy"])
rainy_yes = len([item for item in data if item["outlook"] == "Rainy" and item["play"] == "Yes"])
rainy_no = outlook_rainy - rainy_yes

outlook_overcast = len([item for item in data if item["outlook"] == "Overcast"])
overcast_yes = len([item for item in data if item["outlook"] == "Overcast" and item["play"] == "Yes"])
overcast_no = outlook_overcast - overcast_yes

c1 = play_yes_count / len(data)
c2 = play_no_count / len(data)

x1 = sunny_yes / play_yes_count
x2 = sunny_no / play_no_count

f1 = c1 * x1
f2 = c2 * x2

if f1 > f2:
    print("PLAY = YES")
else:
    print("PLAY = NO")