from turtle import *
from collections import defaultdict
import random


speed(0)
count = 0 # 紀錄是第幾個詞
words_dict = defaultdict(int)   # 用來記錄詞頻  =>words_dict{(詞:詞頻)}
useless = [".",",","'","[","]"] # 把不需要的標點符號列出來


# 讀取"long.txt"，統計檔案中每個單詞的出現次數，並將結果儲存在 words_dict
with open("long.txt", "r", encoding="utf-8") as f:
    for line in f:                   # 一次讀取檔案的一行內容
        words_list = line.split()    # 根據"空格"來分割字串，將該行句子拆解成 list

        for word in words_list:      # 遍歷list，處理不必要的標點符號
            if word[-1] in useless:  # 去除結尾的標點符號
                word = word[:-1]
            if word[0] in useless:   # 去除開頭的標點符號
                word = word[1:]

            word = word.lower()      # 轉成小寫

            words_dict[word] += 1    # 把處理好的word(去標點符號、轉小寫)，存到words_dict，來記錄頻率  =>words_dict{(詞:詞頻)}



# 把常見詞（停用詞）列出來，以便忽略
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


# 用來存放已放置單詞的"位置清單"  => placed_positions = [(x = 單詞的中心X座標, y = 單詞的中心y座標, word_width, word_height)]
placed_positions = []


# 詞雲的顏色列表
color_list = [
    '#00030A',
    '#000611',
    '#000D1A',
    '#00132A',
    '#001F40',
    '#002855',
    '#003D7A',
    '#0052A3',
    '#0066CC',
    '#007FFF',
    '#3399FF',
    '#66B2FF',
    '#99CCFF',
    '#C2E0FF',
    '#E6F2FF'
]



for key in sorted(words_dict.items(), key=lambda x:x[1], reverse=True):  # 先對words_dict中的value進行降序排序(出現頻率由大到小)
# for key in words_dict.items():
    if key[0] in stop_list:  #若key值是stop_list中的詞，跳過該單詞，不將其加入詞雲
        continue


    color(color_list[count%15])     #為了詞雲美觀用: 讓顏色在 color_list 中循環選擇，使不同的單詞有不同的顏色。原turtle.color()
    
    while True:                          # 設定詞雲顯示範圍在半徑=200的圓圈內
        x = random.uniform(-200, 200)    # 在 (-200, 200) 之間隨機選擇x和y的位子，讓單詞可以放在這個範圍內。
        y = random.uniform(-200, 200)
        if x**2 + y**2 >= 200**2:        # 圓的標準方程式  =>  確保計算(x,y)與(0,0)的距離，超出設定的畫面範圍(圓圈)則重random一次
            continue

        font_size = int( 20*(1 + 4*(key[1]-45)/355))   # 根據該單詞出現的頻率，來設定字體大小。
        

        # 檢查單詞的放置位子是否與其他單詞重疊
        word_width = len(key[0]) * font_size * 0.6
        word_height = font_size
        overlap = False
        for i in range(len(placed_positions)):       # 如果新單詞的X座標與已放置的單詞的X座標之間的距離，小於它們總寬度的一半，那麼它們在 X 軸上有重疊。y軸也是相同道理
            if abs(x - placed_positions[i][0]) < ((word_width + placed_positions[i][2]) / 2)  and  \
                abs(y - placed_positions[i][1]) < ((word_height + placed_positions[i][3]) / 2):
                overlap = True
                break        # 如有重疊，就回到while loop重新random一對(x, y)，直到找到不重疊的位置

        if not overlap:    # 單詞未重疊
            #print("not overlap")
            penup()
            goto(x, y)
            pendown()
            write(key[0], align="center", font=("Arial", font_size, "normal"))  #在畫面上寫上單詞
            placed_positions.append((x, y, word_width, word_height))   # 把位子資訊紀錄進去placed_positions
            count += 1     
            break  

    print(count)  #顯示印到第幾個

    # 限制最多顯示 70 個單詞，避免詞雲過於密集
    if count == 70:     
        break

hideturtle()
done()

