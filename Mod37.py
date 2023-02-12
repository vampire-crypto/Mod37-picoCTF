# Code to solve picoctf Basic-mod1
# 54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 

list = [54, 396, 131, 198, 225, 258, 87, 258, 128, 211, 57, 235, 114, 258, 144, 220, 39, 175, 330, 338, 297, 288]
data = "ABCDEFGHIJKLMNOPQRSTUVEQYZ0123456789_"
for item in list :
    entry = (item%37)
    print (data[entry], end="")


