from turtle import *
from collections import defaultdict
import random


speed(0)
count = 0 # 紀錄是第幾個詞
words_dict = defaultdict(int)   # 用來記錄詞頻  =>words_dict{(詞:詞頻)}
useless = [".",",","'","[","]"] # 把不需要的標點符號列出來

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



# 用來存放已放置單詞的"位置清單"  => placed_positions = [(x = 單詞的中心X座標, y = 單詞的中心y座標, word_width, word_height)]
placed_positions = []


# 詞雲的顏色列表
# 45階藍色漸層，由深到淺
color_list = [
    "#00030A", "#000510", "#000714", "#00091A", "#000B1F", "#000D24", "#001029", "#00132F", "#001635", "#00193B",
    "#001C42", "#001F49", "#002250", "#002558", "#002960", "#002C68", "#003070", "#003479", "#003882", "#003C8B",
    "#004094", "#00449E", "#0048A8", "#004CB2", "#0050BC", "#0055C6", "#005AD0", "#0060DA", "#0065E4", "#006BEF",
    "#0070F9", "#1A75FF", "#3380FF", "#4D8CFF", "#6697FF", "#80A3FF", "#99AEFF", "#B2BAFF", "#CCC5FF", "#D6D1FF",
    "#E0DCFF", "#E9E6FF", "#F0EFFF", "#F5F3FF", "#F9F6FF"
    ]


words_dict = sorted(words_dict.items(), key=lambda x:x[1], reverse=True)  # 詞頻由大到小排列
max_freq = words_dict[0][1]  # 頻率最高的次數
min_freq = words_dict[-1][1] # 頻率最低的次數 


for key in words_dict:  
    if key[0] in stop_list:  #若key值是stop_list中的詞，跳過該單詞，不將其加入詞雲
        continue

    color(color_list[count%45])     #依照詞頻高到低=>深到淺。原turtle.color()


    while True:                          # 設定詞雲顯示範圍在半徑=200的圓圈內
        x = random.uniform(-200, 200)    # 在 (-200, 200) 之間隨機選擇x和y的位子，讓單詞可以放在這個範圍內。
        y = random.uniform(-200, 200)
        if x**2 + y**2 >= 200**2:        # 圓的標準方程式  =>  確保計算(x,y)與(0,0)的距離，超出設定的畫面範圍(圓圈)則重random一次
            continue


        if max_freq == min_freq:  # 避免分母為 0
            max_freq += 1  
        font_size = int(20 * (1 + 4 * (key[1] - min_freq) / (max_freq - min_freq)))   # 根據該單詞出現的頻率，來設定字體大小: 採線性縮放模型
        

        # 檢查單詞的放置位子是否與其他單詞重疊
        word_width = len(key[0]) * font_size * 0.6
        word_height = font_size
        overlap = False
        # 如果新單詞的X座標與已放置的單詞的X座標之間的距離，小於它們總寬度的一半，那麼它們在 X 軸上有重疊。y軸也是相同道理
        for i in range(len(placed_positions)):   
            if abs(x - placed_positions[i][0]) < ((word_width + placed_positions[i][2]) / 2)  and  \
                abs(y - placed_positions[i][1]) < ((word_height + placed_positions[i][3]) / 2):
                overlap = True
                break        # 如有重疊，就回到while loop重新random一對(x, y)，直到找到不重疊的位置

        if not overlap:    # 單詞未重疊
            penup()
            goto(x, y)
            pendown()
            write(key[0], align="center", font=("Arial", font_size, "normal"))  #在畫面上寫上單詞
            placed_positions.append((x, y, word_width, word_height))   # 把位子資訊紀錄進去placed_positions
            count += 1     
            break  

    print(count)  #顯示印到第幾個

    # 限制最多顯示 45 個單詞，避免詞雲過於密集
    if count == 45:     
        break

hideturtle()
done()
