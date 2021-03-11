s = '''漢皇重色思傾國，御宇多年求不得。
楊家有女初長成，養在深閏人未識。
天生麗質難自棄，一朝選在君王側。
回眸一笑百媚生，六宮粉黛無顏色。
春寒賜浴華清池，溫泉水滑洗凝脂；
侍兒扶起嬌無力，始是新承恩澤時。
雲鬢花顏金步搖，芙蓉帳暖度春宵；
春宵苦短日高起，從此君王不早朝。
承歡侍宴無閑暇，春從春遊夜專夜。
後宮佳麗三千人，三千寵愛在一身。
金屋妝成嬌侍夜，玉樓宴罷醉和春。
姊妹弟兄皆列士，可憐光彩生門戶。
遂令天下父母心，不重生男重生女。
驪宮高處入青雲，仙樂風飄處處聞。
緩歌慢舞凝絲竹，盡日君王看不足。
漁陽鼙鼓動地來，驚破霓裳羽衣曲。
九重城闕煙塵生，千乘萬騎西南行。
翠華搖搖行復止，西出都門百餘里；
六軍不發無奈何？宛轉蛾眉馬前死。
花鈿委地無人收，翠翹金雀玉搔頭。
君王掩面救不得，回看血淚相和流。
黃埃散漫風蕭索，雲棧縈紆登劍閣。
峨嵋山下少人行，旌旗無光日色薄。
蜀江水碧蜀山青，聖主朝朝暮暮情。
行宮見月傷心色，夜雨聞鈴腸斷聲。
天旋地轉迴龍馭，到此躊躇不能去。
馬嵬坡下泥土中，不見玉顏空死處。
君臣相顧盡霑衣，東望都門信馬歸。
歸來池苑皆依舊，太液芙蓉未央柳；
芙蓉如面柳如眉，對此如何不淚垂？
春風桃李花開日，秋雨梧桐葉落時。
西宮南內多秋草，落葉滿階紅不掃。
梨園子弟白髮新，椒房阿監青娥老。
夕殿螢飛思悄然，孤燈挑盡未成眠。
遲遲鐘鼓初長夜，耿耿星河欲曙天。
鴛鴦瓦冷霜華重，翡翠衾寒誰與共？
悠悠生死別經年，魂魄不曾來入夢。
臨邛道士鴻都客，能以精誠致魂魄；
為感君王輾轉思，遂教方士殷勤覓。
排空馭氣奔如電，升天入地求之遍；
上窮碧落下黃泉，兩處茫茫皆不見。
忽聞海上有仙山，山在虛無縹緲間。
樓閣玲瓏五雲起，其中綽約多仙子。
中有一人字太真，雪膚花貌參差是。
金闕西廂叩玉扃，轉教小玉報雙成。
聞道漢家天子使，九華帳裡夢魂驚；
攬衣推枕起徘徊，珠箔銀屏迤邐開。
雲鬢半偏新睡覺，花冠不整下堂來。
風吹仙袂飄飄舉，猶似霓裳羽衣舞。
玉容寂寞淚闌干，梨花一枝春帶雨。
含情凝睇謝君王，一別音容兩渺茫。
昭陽殿裡恩愛絕，蓬萊宮中日月長。
回頭下望人寰處，不見長安見塵霧。
唯將舊物表深情，鈿合金釵寄將去。
釵留一股合一扇，釵擘黃金合分鈿。
但教心似金鈿堅，天上人間會相見。
臨別殷勤重寄詞，詞中有誓兩心知，
七月七日長生殿，夜半無人私語時：「
在天願作比翼鳥，在地願為連理枝。」
天長地久有時盡，此恨綿綿無絕期。
'''
s1 =['漢皇', '重色思', '傾國', '御宇', '多年', '求', '不得', '楊家', '有', '女', '初長', '成養', '在', '深閏人', '未識', '天生', '麗質', '難', 
'自棄', '一朝', '選在', '君王', '側', '回眸', '回眸一笑', '百媚生', '六宮', '粉黛', '無顏色', '春寒', '賜', '浴華清', '池溫', '泉水', '滑洗', 
'凝脂', '侍兒', '扶', '起嬌', '無力始', '是', '新承恩澤時', '雲鬢花', '顏金步搖', '芙蓉', '帳暖', '春宵', '度春宵', '春宵', '苦短', '春宵苦短', 
'日高起', '從', '此', '君王', '不早', '朝承歡', '侍宴', '無', '閑', '暇', '春', '從', '春遊夜', '專夜', '後', '宮佳麗', '三千', '人', '三千', 
'寵愛在', '一身', '金屋', '妝', '成嬌', '侍夜', '玉樓', '宴', '罷醉', '和', '春', '姊妹', '弟兄', '皆', '列士', '可憐', '光彩', '生門戶', '遂', 
'令', '天下', '父母', '天下父母', '心', '不', '重生', '男', '重生', '女驪宮', '高處入', '青雲仙樂', '風飄處', '處聞', '緩歌', '慢舞', '凝絲竹', 
'盡日', '君王', '看', '不足', '漁陽', '鼙', '鼓動', '地來', '驚破', '霓裳', '羽衣', '羽衣曲', '九重', '城闕', '煙塵', '生千乘', '萬', '騎', '西南', 
'行翠華搖搖行', '復', '止', '西出', '都', '門百餘里', '六軍不發', '無', '奈何', '宛轉', '蛾眉', '馬', '前', '死', '花鈿委地', '無人', '收翠翹', 
'金雀玉', '搔頭', '君王', '掩面', '救', '不得', '回看', '血淚', '相', '和', '流黃埃', '散漫', '風蕭索', '雲棧', '縈', '紆', '登劍閣', '峨嵋', 
'峨嵋山', '下少', '人行', '旌旗', '無光', '日色', '薄', '蜀', '江水', '碧', '蜀山', '青聖主', '朝暮', '朝朝暮暮', '情行', '宮見', '月', '傷心色', 
'夜雨', '聞鈴腸', '斷聲', '天旋', '地轉', '迴', '龍馭', '到', '此', '躊躇', '不能', '去', '馬', '嵬', '坡', '下', '泥土', '中不見', '玉顏空', '死', 
'處', '君臣', '相顧', '盡霑', '衣東望', '都', '門信', '馬', '歸歸來', '池苑', '皆', '依舊', '太液', '芙蓉', '未央', '柳', '芙蓉', '如面', '柳如眉', 
'對此', '如何', '不淚', '垂春風', '桃李', '花開', '日', '秋雨', '梧桐', '葉落', '時西宮', '南內', '多秋草', '落葉', '滿階紅', '不', '掃梨園', '子弟', 
'白', '髮', '新椒房', '阿監', '青娥', '老夕殿', '螢飛思', '悄然', '孤燈', '挑', '盡', '未', '成眠', '遲遲', '鐘鼓', '初長', '夜', '耿耿', '星河', 
'耿耿星河', '欲曙天', '鴛鴦', '瓦', '冷霜', '華重', '翡翠', '衾', '寒', '誰', '與', '共', '悠悠', '生死', '別經', '年', '魂魄', '不曾', '來入', '夢臨', 
'邛', '道士', '鴻', '都', '客能', '以', '精誠致', '魂魄', '為感', '君王', '輾轉思', '遂', '教', '方士', '殷勤', '覓', '排空', '馭', '氣奔', '如電', 
'升天', '入', '地求', '之遍', '上', '窮', '碧', '落下', '黃', '泉', '兩處', '茫茫', '皆', '不見', '忽聞', '海上', '有', '仙山', '山在', '虛無縹緲', 
'間', '樓', '閣玲瓏', '五雲起', '其中', '綽約', '多', '仙子', '中有', '人字', '一人字', '太', '真雪膚', '花貌', '參差', '是', '金', '闕', '西廂', 
'叩玉', '扃', '轉教', '小玉報', '雙成', '聞道', '漢家', '天子', '使九華', '帳裡', '夢魂', '推枕起', '徘徊', '珠箔', '銀屏', '迤邐', '開雲鬢', '半偏', 
'新', '睡覺', '花冠', '不整', '下堂', '來風', '吹', '仙袂', '飄飄舉', '猶似', '霓裳', '羽衣', '舞', '玉容', '寂寞', '淚闌干', '梨花', '一枝', '一枝春', 
'帶雨', '含情', '凝睇', '謝', '君王', '一別', '音容', '兩', '渺茫', '昭陽', '殿裡', '恩愛絕', '蓬萊宮', '中', '日月', '長', '回頭', '下望', '人', '寰', 
'處', '不見長', '安見', '塵霧', '唯將', '舊物表', '深情', '鈿', '合金', '釵', '寄將', '去', '釵', '留', '一股', '合', '一扇', '釵', '擘', '黃', '金合', 
'分鈿', '但', '教心', '似金鈿堅', '天上', '人間', '會', '相見', '臨別', '殷勤', '重寄詞', '詞中', '有', '誓', '心知', '兩心知', '七月', '七日', 
'七月七日', '長', '生殿', '夜半', '無人', '私語', '時', '在', '天願作', '比翼', '比翼鳥', '在', '地願', '為', '連理枝', '天長', '地久', '有', '時', 
'盡', '此恨', '綿綿', '無', '絕期']
s = s.replace('，', '').replace('。', '').replace('「', '').replace('」', '').replace('；', '').replace('？', '').replace('：', '').replace('\n', '')


text = [] #詞
num = []  #出現次數
dict = {}
lst = []
text_1 = []
text_2 = []
text_3 = []
text_4 = []
text_5 = []
text_6 = []

text_1t = []
text_1n = []
text_1n_s = []
text_2t = []
text_2n = []
text_2n_s = []
text_3t = []
text_3n = []
text_3n_s = []
text_4t = []
text_4n = []
text_4n_s = []
text_5t = []
text_5n = []
text_5n_s = []
text_6t = []
text_6n = []
text_6n_s = []

t1 = []
n1 = []
tt1 = []
tt1_sort = []
t2 = []
n2 = []
tt2 = []
tt2_sort = []
t3 = []
n3 = []
tt3 = []
tt3_sort = []
t4 = []
n4 = []
tt4 = []
tt4_sort = []
t5 = []
n5 = []
tt5 = []
tt5_sort = []
t6 = []
n6 = []
tt6 = []
tt6_sort = []

for i in range(len(s1)):
    qct = s.count(s1[i]) #算各個詞出現次數
    text.append(s1[i])
    num.append(qct)
    dict[s1[i]] = qct


for i in range(len(text)):    ######依照字詞長度 分別存到list
    if len(text[i]) == 1:
        if text[i] not in text_1:
            text_1.append(text[i])
    elif len(text[i]) == 2:
        if text[i] not in text_2:
            text_2.append(text[i])
    elif len(text[i]) == 3:
        if text[i] not in text_3:
            text_3.append(text[i])
    elif len(text[i]) == 4:
        if text[i] not in text_4:
            text_4.append(text[i])
    elif len(text[i]) == 5:
        if text[i] not in text_5:
            text_5.append(text[i])
    else:
        if text[i] not in text_6:
            text_6.append(text[i])
###先考慮字詞長度，分為長度1到6來處理
##########1
for i in range(len(text_1)):       ###找出長度為1的字詞，在最原本list的位置
    j = 0
    while text_1[i] != text[j]:
        j = j + 1
    text_1t.append(text_1[i])
    text_1n.append(num[j])
    #print(text_1[i], num[j])
text_1n_s = sorted(text_1n, reverse = True)  
for i in range(len(text_1n_s)):       #####在長度皆為1的list裡，按照出現次數多到少排列
    j = 0
    while text_1n_s[i] != text_1n[j]:
        j = j + 1
    t1.append(text_1t[j])
    n1.append(text_1n[j])

    #print(text_1t[j], text_1n[j])

    del text_1t[j]
    del text_1n[j]

for j in range(max(n1), 0, -1):                   #################
    for i in range(len(n1)):
        if j == n1[i]:
            tt1.append(t1[i])   
    tt1_sort = sorted(tt1)
    tt1 = []       
    for i in range(len(tt1_sort)):
        print(tt1_sort[i], end = ' ')
        print(j)                               #####################
    

########2
for i in range(len(text_2)):
    j = 0
    while text_2[i] != text[j]:
        j = j + 1
    text_2t.append(text_2[i])
    text_2n.append(num[j])

text_2n_s = sorted(text_2n, reverse = True)
for i in range(len(text_2n_s)):
    j = 0
    while text_2n_s[i] != text_2n[j]:
        j = j + 1
    t2.append(text_2t[j])
    n2.append(text_2n[j])
    #print(text_2t[j], text_2n[j])

    del text_2t[j]
    del text_2n[j]

for j in range(max(n2), 0, -1):
    for i in range(len(n2)):
        if j == n2[i]:
            tt2.append(t2[i])   
    tt2_sort = sorted(tt2)
    tt2 = []       
    for i in range(len(tt2_sort)):
        print(tt2_sort[i], end = ' ')
        print(j)

########3
for i in range(len(text_3)):
    j = 0
    while text_3[i] != text[j]:
        j = j + 1
    text_3t.append(text_3[i])
    text_3n.append(num[j])

text_3n_s = sorted(text_3n, reverse = True)
for i in range(len(text_3n_s)):
    j = 0
    while text_3n_s[i] != text_3n[j]:
        j = j + 1
    t3.append(text_3t[j])
    n3.append(text_3n[j])
    #print(text_3t[j], text_3n[j])

    del text_3t[j]
    del text_3n[j]

for j in range(max(n3), 0, -1):
    for i in range(len(n3)):
        if j == n3[i]:
            tt3.append(t3[i])   
    tt3_sort = sorted(tt3)
    tt3 = []       
    for i in range(len(tt3_sort)):
        print(tt3_sort[i], end = ' ')
        print(j)

########4
for i in range(len(text_4)):
    j = 0
    while text_4[i] != text[j]:
        j = j + 1
    text_4t.append(text_4[i])
    text_4n.append(num[j])

text_4n_s = sorted(text_4n, reverse = True)
for i in range(len(text_4n_s)):
    j = 0
    while text_4n_s[i] != text_4n[j]:
        j = j + 1
    t4.append(text_4t[j])
    n4.append(text_4n[j])
    #print(text_4t[j], text_4n[j])

    del text_4t[j]
    del text_4n[j]
for j in range(max(n4), 0, -1):
    for i in range(len(n4)):
        if j == n4[i]:
            tt4.append(t4[i])   
    tt4_sort = sorted(tt4)
    tt4 = []       
    for i in range(len(tt4_sort)):
        print(tt4_sort[i], end = ' ')
        print(j)

########5
for i in range(len(text_5)):
    j = 0
    while text_5[i] != text[j]:
        j = j + 1
    text_5t.append(text_5[i])
    text_5n.append(num[j])

text_5n_s = sorted(text_5n, reverse = True)
for i in range(len(text_5n_s)):
    j = 0
    while text_5n_s[i] != text_5n[j]:
        j = j + 1
    t5.append(text_5t[j])
    n5.append(text_5n[j])
    #print(text_5t[j], text_5n[j])

    del text_5t[j]
    del text_5n[j]

for j in range(max(n5), 0, -1):
    for i in range(len(n5)):
        if j == n5[i]:
            tt5.append(t5[i])   
    tt5_sort = sorted(tt5)
    tt5 = []       
    for i in range(len(tt5_sort)):
        print(tt5_sort[i], end = ' ')
        print(j)

########6
for i in range(len(text_6)):
    j = 0
    while text_6[i] != text[j]:
        j = j + 1
    text_6t.append(text_6[i])
    text_6n.append(num[j])

text_6n_s = sorted(text_6n, reverse = True)
for i in range(len(text_6n_s)):
    j = 0
    while text_6n_s[i] != text_6n[j]:
        j = j + 1
    t6.append(text_6t[j])
    n6.append(text_6n[j])
    #print(text_6t[j], text_6n[j])

    del text_6t[j]
    del text_6n[j]

for j in range(max(n6), 0, -1):
    for i in range(len(n6)):
        if j == n6[i]:
            tt6.append(t6[i])   
    tt6_sort = sorted(tt6)
    tt6 = []       
    for i in range(len(tt6_sort)):
        print(tt6_sort[i], end = ' ')
        print(j)