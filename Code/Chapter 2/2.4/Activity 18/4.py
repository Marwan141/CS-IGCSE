gameScores = [["Alex", 1, 19], ["Seema", 1, 29], ["Seema", 2, 29], ["Lois", 1, 10], ["Alex", 2, 17], ["Alex", 3, 36], ["Dion", 1, 23], ["Emma", 1, 27], ["Emma", 2, 48]]

hs1 = 0
hsp1 = ""
hs2 = 0
hsp2 = ""
hs3 = 0
hsp3 = ""


for row in gameScores:
    player = row[0]
    level = row[1]
    score =  row[2]
    if level == 1 and hs1 < score:
        hs1 = score
        hsp1 = player
    elif level == 2 and hs2 < score:
        hs2 = score
        hsp2 = player
    elif level == 3 and hs3 < score:
        hs3 = score
        hsp3 = player
        
print("The highest score for level 1 was " + str(hs1))
print("Player " + hsp1 + " archieved this score")
print("The highest score for level 2 was " + str(hs2))
print("Player " + hsp2 + " archieved this score")
print("The highest score for level 3 was " + str(hs3))
print("Player " + hsp3 + " archieved this score")
