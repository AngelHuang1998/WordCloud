from turtle import *
import math
import random
speed(0)
line_num = 1
total_words = 0
words_dict = {}
useless = [".",",","'"]
with open("long.txt", "r", encoding="utf-8") as f:
    for line in f:
        words_list = line.split()
        for word in words_list:
            if word[-1] in useless:
                word = word[:-1]
            if word[0] in useless:
                word = word[1:]
            word = word.lower()

            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += 1

count = 1
penup()
goto(-250,200)
pendown()

stop_list = [ "i", "you", "he", "she", "it", "we", "they", "me", "him", "her",
    "us", "them", "my", "your", "his", "their", "mine", "yours", "hers",
    "ours", "theirs", "a", "an", "the", "and", "but", "if", "or", "because",
    "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after",
    "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
    "over", "under", "again", "further", "then", "once", "here", "there",
    "when", "where", "why", "how", "all", "any", "both", "each", "few",
    "more", "most", "other", "some", "such", "no", "nor", "not", "only",
    "own", "same", "so", "than", "too", "very", "can", "will", "just", "is", 
    "be", "are", "am", "was", "i’ll", "o", "this", "that", "have", "do", "what",
    "let", "may", "did", "must", "sir", "’tis", "had", "were", "much", "thou", "thy"]
color_list = ['#2E0854', '#4B0082', '#6A0DAD', '#800080', '#8B008B', '#8A2BE2', '#9370DB', '#9400D3', '#BA55D3', '#C71585', '#DA70D6', '#D8BFD8', '#DDA0DD', '#EE82EE', '#FF00FF', '#E6E6FA', '#F8F8FF', '#F5F5F5', '#FAE6FA', '#FFF0F5']
placed_positions = []
for key in sorted(words_dict.items(), key=lambda x:x[1], reverse=True):
# for key in words_dict.items():
    if key[0] in stop_list:
        continue
    if count % 2 == 0:
        count += 1
        continue
    color(color_list[count//12])
    while True:
        x = random.uniform(-200, 200)
        y = random.uniform(-200, 200)
        if x**2 + y**2 >= 200**2:
            continue

        font_size = int( 20*(1 + 4*(key[1]-45)/355))
        word_width = len(key[0]) * font_size * 0.6
        word_height = font_size
        overlap = False
        for i in range(len(placed_positions)):
            if abs(x - placed_positions[i][0]) < (word_width + placed_positions[i][2]) / 2 and abs(y - placed_positions[i][1]) < (word_height + placed_positions[i][3]) / 2:
                overlap = True
                break
        if not overlap:
            print("not overlap")
            penup()
            goto(x, y)
            pendown()
            write(key[0], align="center", font=("Arial", font_size, "normal"))
            placed_positions.append((x, y, word_width, word_height))
            count += 1     
            break  
    print(count)
    if count == 220:
        break
hideturtle()
done()

