import csv
import math

G = 9.8

dinos = {}
with open("t1.csv", newline="", encoding="utf-8") as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    for row in spamreader:
        # print(row)
        if row["Feet"] == "B":
            new_dino = {"Name": row["Name"]}
            dinos[row["id"]] = new_dino

with open("t2.csv", newline="", encoding="utf-8") as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    for row in spamreader:
        # print(row)
        if row["id"] in dinos:
            dinos[row["id"]]["STRIDE_LENGTH"] = float(row["STRIDE_LENGTH"])
            dinos[row["id"]]["LEG_LENGTH"] = float(row["LEG_LENGTH"])
            dinos[row["id"]]["speed"] = (
                (dinos[row["id"]]["STRIDE_LENGTH"] / dinos[row["id"]]["LEG_LENGTH"]) - 1
            ) * math.sqrt(dinos[row["id"]]["LEG_LENGTH"] * G)

byspeed = sorted(dinos.values(), key=lambda x: x["speed"], reverse=True)
for dino in byspeed:
    print(dino)
