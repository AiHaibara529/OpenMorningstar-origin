import random

DATASET = {
    "noun": list({
        "树懒","貂熊","猎犬","黑狗","灵猫","鸭嘴兽","刺猬","北极狐","无尾熊","北极熊","袋鼠","犰狳","河马","海豹","臭鼬","青蛙","松鼠","豹子","老虎",
        "水鹿","岩羊","盘羊","雪兔","猕猴","棕熊","黑熊","蜂猴","熊猴","叶猴","紫貂","熊狸","云豹","雪豹","野马","豚鹿","麋鹿","野牛","藏羚","河狸","金丝猴","长臂猿","大熊猫","白暨豚","亚洲象","骆驼","梅花鹿","牦牛","扬子鳄",
        "蝴蝶","蜻蜓","珊瑚","蟋蟀",
        "草履虫","海参","水母","海星","乌贼",
        "苍鹰","白鹭","企鹅","血雉","山鸡","勺鸡","雪鸡","犀鸟","松鸡","鹦鹉","鸳鸯","啄木鸟","鸵鸟","翠鸟","天鹅","灰鹤","蜂鸟","信天翁","夜鹰","海鸥",
        "海狮","海豚","鲨鱼","海龟","海象","蜥蜴","恐龙","地龟","玳瑁","大鲵","绿海龟","壁虎","虎纹蛙",
        "鲸鱼","龙鱼","鲶鱼","章鱼","鳅鱼","鳟鱼","锦鲤","神仙鱼","鳄鱼","鲈鱼","鲤鱼","金枪鱼","鲟鱼","鲑鱼","孔雀鱼",
    }),
    "adjective": list({
        "谦逊",
        "瑟琴",
        "俏皮",
        "天真",
        "敏捷","灵敏","灵巧",
        "温柔","柔顺","柔和","乖巧","听话","顺从","温驯","温和",
        "胆小",
        "贪吃",
        "调皮","活泼","淘气","顽皮",
        "细腻",
        "勇敢",
        "干净",
        "友善",
        "雪白",
        "骄傲",
        "柔弱",
        "利索",
        "优雅",
        "威武",
        "安详",
        "神气",
        "可爱",
        "迅猛",
        "友好",
        "柔软",
        "美丽",
        "安静",
        "愤怒",
        "孤独",
        "伶俐",
        "安稳",
        "灵活",
        "忠心",
        "壮实",
        "灵性",
        "轻巧",
        "忠厚",
        "结实",
        "嬉戏",
        "坚强",
        "健壮",
        "贪玩",
    }) 
}


def get_random_nickname():
    noun = DATASET["noun"][random.randint(0, len(DATASET["noun"])-1)]
    adjective = DATASET["adjective"][random.randint(0, len(DATASET["adjective"])-1)]
    
    return f"{adjective}的{noun}"


if __name__ == "__main__":
    print(get_random_nickname())