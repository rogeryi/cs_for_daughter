# 游戏主程序 - 蝴蝶冢
# Butterfly's Tomb - Main Game

import sys

class Game:
    def __init__(self):
        self.player_name = "罗罗诺亚·索隆"
        self.companion = "霜月古伊娜"
        self.inventory = []  # 背包
        self.current_location = "入口"
        self.flags = {}  # 剧情标记
        
    def start(self):
        """游戏开始"""
        print("="*60)
        print(" "*18 + "蝴 蝶 冢")
        print("="*60)
        print()
        print("多年以后，面对雪原上飞舞的蓝色蝴蝶，")
        print("罗罗诺亚·索隆将会回想起，他和古伊娜")
        print("踏入蝶栖镇的那个遥远的下午。")
        print()
        input("按回车键继续...")
        print()
        
        # 第一章：进入小镇
        self.chapter_1()
    
    def chapter_1(self):
        """第一章：雪原森林"""
        print("-"*60)
        print("第一章：雪原森林")
        print("-"*60)
        print()
        
        print("雪下了整整一个冬天，森林里的树木都被冻成了")
        print("白色的骨骼。索隆和古伊娜已经在雪地里走了三天。")
        print()
        
        print("「索隆，你看。」古伊娜指着前方。")
        print()
        print("在森林的尽头，出现了一座小镇。烟囱里冒出")
        print("灰色的烟，像是小镇在呼吸。镇口的木牌上")
        print("写着三个字：蝶栖镇。")
        print()
        
        print("奇怪的是，镇子里静得出奇。")
        print("没有狗吠，没有孩童的嬉笑，")
        print("只有几只蓝色的蝴蝶在雪地里缓缓飞舞。")
        print()
        
        # 玩家选择
        print("【选择】")
        print("1. 走进小镇")
        print("2. 在镇外观察")
        print("3. 和古伊娜商量")
        print()
        
        choice = input("请输入你的选择 (1/2/3): ")
        
        if choice == "1":
            self.enter_town()
        elif choice == "2":
            self.observe_town()
        else:
            self.talk_with_guina()
    
    def enter_town(self):
        """进入小镇"""
        print()
        print("索隆迈开脚步，踩在雪地上发出嘎吱嘎吱的声响。")
        print("古伊娜跟在他身后，两人的脚印在雪地里")
        print("像是写给大地的两行诗句。")
        print()
        print("镇子的第一条街道两旁是低矮的木屋。")
        print("窗户都拉着窗帘，但索隆感觉到")
        print("窗帘后面有眼睛在看着他们。")
        print()
        
        self.current_location = "蝶栖镇街道"
        self.explore_street()
    
    def observe_town(self):
        """观察小镇"""
        print()
        print("索隆停下脚步，仔细观察着这座小镇。")
        print()
        print("他注意到几件奇怪的事：")
        print("- 所有的屋顶上都没有积雪")
        print("- 烟囱里冒出的烟是淡蓝色的")
        print("- 那些蝴蝶只在特定的地方飞舞")
        print()
        print("「那些蝴蝶...」古伊娜低声说，")
        print("「好像在守护什么，又好像在等待什么。」")
        print()
        
        print("【获得线索】蝴蝶的异常行为")
        self.flags["观察过小镇"] = True
        self.inventory.append("线索：蓝色蝴蝶")
        
        print("按回车键继续...")
        input()
        self.enter_town()
    
    def talk_with_guina(self):
        """与古伊娜对话"""
        print()
        print("「古伊娜，你觉得这个镇子怎么样？」")
        print()
        print("古伊娜沉默了一会儿。")
        print("「索隆，你还记得我们为什么来这里吗？」")
        print()
        print("索隆愣了一下。他突然发现，")
        print("自己竟然记不清来到这里的初衷。")
        print("记忆像是被什么东西模糊了，")
        print("就像隔着一层结了冰的玻璃看世界。")
        print()
        print("【重要发现】记忆开始模糊")
        self.flags["记忆模糊"] = True
        
        print("按回车键继续...")
        input()
        self.enter_town()
    
    def explore_street(self):
        """探索街道"""
        print("-"*60)
        print(f"当前位置: {self.current_location}")
        print("-"*60)
        print()
        
        print("街道上有三处地方引起了索隆的注意：")
        print()
        print("1. 一座废弃的旅馆，门半开着")
        print("2. 一间亮着灯的酒馆")
        print("3. 一个石碑，立在街道中央")
        print()
        
        choice = input("你想去哪里？(1/2/3): ")
        
        if choice == "1":
            self.abandoned_inn()
        elif choice == "2":
            self.mysterious_tavern()
        elif choice == "3":
            self.ancient_stele()
        
        print("\n(游戏演示结束)")
        print("感谢体验《蝴蝶冢》原型！")
        print("更多剧情和谜题正在开发中...")
    
    def abandoned_inn(self):
        """废弃的旅馆"""
        print("\n" + "="*60)
        print("废弃旅馆：「归蝶客栈」")
        print("="*60)
        print()
        
        print("旅馆的木门发出刺耳的声响。大厅里积满了灰尘，")
        print("但奇怪的是，柜台上放着一杯还在冒热气的茶。")
        print()
        
        print("「欢迎。」一个苍老的声音从楼梯口传来。")
        print()
        
        print("一个穿着灰色长袍的老妇人站在那里，")
        print("她的脸上布满皱纹，但眼睛异常明亮。")
        print("更奇怪的是，她的头发是半透明的蓝色，")
        print("像是由蝴蝶的翅膀编织而成。")
        print()
        
        print("「我是这里的老板娘，你们可以叫我蝶婆婆。」")
        print("「已经很久没有客人来了……准确地说，")
        print("是那些来过的人，都变成了蝴蝶。」")
        print()
        
        # NPC对话
        print("【蝶婆婆】")
        print("1. 询问小镇的历史")
        print("2. 询问古伊娜")
        print("3. 查看旅馆的登记簿")
        print()
        
        choice = input("你想做什么？(1/2/3): ")
        
        if choice == "1":
            self.inn_ask_history()
        elif choice == "2":
            self.inn_ask_about_guina()
        else:
            self.inn_check_register()
    
    def inn_ask_history(self):
        """询问小镇历史"""
        print()
        print("蝶婆婆叹了口气，走到窗边。")
        print()
        print("「蝶栖镇曾经是个热闹的地方。直到三十年前，")
        print("镇上的第一位死者……没有埋葬。」")
        print()
        print("「他的尸体停放在家里，第二天，")
        print("人们发现尸体变成了千百只蓝色的蝴蝶。」")
        print("从那天起，每个死去的人都会变成蝴蝶。」")
        print("渐渐地，没有人再敢埋葬死者，")
        print("也没有人敢离开这个镇子。」")
        print()
        print("「因为离开的人……也会变成蝴蝶。」")
        print()
        
        print("【获得线索】蝴蝶现象的起源")
        self.flags["知道蝴蝶起源"] = True
        self.inventory.append("线索：三十年前的异变")
        
        print("按回车键继续...")
        input()
    
    def inn_ask_about_guina(self):
        """询问古伊娜"""
        print()
        print("蝶婆婆的目光突然变得锐利。")
        print()
        print("「那个女孩……她的身体里，")
        print("已经有一只蝴蝶在沉睡了。」")
        print()
        print("索隆的心猛地一沉。")
        print("「你说什么？」")
        print()
        print("「别紧张，」蝶婆婆缓缓说道，")
        print("「所有人来到这里，身体里都会有蝴蝶的种子。」")
        print("「它什么时候醒来，取决于你们能找到多少真相。」")
        print("「真相越多，蝴蝶醒来得越慢。」")
        print("「无知的人，会变成蝴蝶飞走。」")
        print()
        
        print("【获得线索】古伊娜的状态")
        self.flags["古伊娜有蝴蝶种子"] = True
        self.inventory.append("线索：真相延缓蝴蝶")
        
        print("按回车键继续...")
        input()
    
    def inn_check_register(self):
        """查看登记簿"""
        print()
        print("索隆翻开柜台上的登记簿。")
        print("最后一页的墨迹还是新的。")
        print()
        print("最近的入住记录：")
        print("- 3天前：一个戴帽子的男人（字迹模糊）")
        print("- 7天前：霜月古伊娜（古伊娜的笔迹！）")
        print("- 15天前：空白")
        print("- 30天前：空白")
        print()
        print("更奇怪的是，往前翻的所有记录，")
        print("入住者的名字都在逐渐褪色，")
        print("像是被什么东西从纸上吸走了。")
        print()
        print("【重要发现】古伊娜在7天前就已经来过？")
        self.flags["古伊娜的矛盾记录"] = True
        
        # 解密小游戏
        print("\n【解密】登记簿上有一道密码锁")
        print("锁上刻着：")
        print("「第一个变成蝴蝶的人，死于一月」")
        print("「第三个，死于三月」")
        print("「第七个，死于七月」")
        print("「那第五个，死于几月？」")
        print()
        
        print("提示：答案是一个数字 (1-12)")
        answer = input("你的答案: ")
        
        if answer == "5":
            print("\n「咔哒」一声，抽屉弹开了。")
            print("里面有一把古老的钥匙，")
            print("钥匙上刻着一只蝴蝶。")
            print()
            print("【获得物品】蝴蝶钥匙")
            self.inventory.append("物品：蝴蝶钥匙")
        else:
            print("\n没有任何反应。")
            print("也许答案不对，或者需要更多线索。")
        
        print("\n按回车键继续...")
        input()
    
    def mysterious_tavern(self):
        """神秘的酒馆"""
        print("\n" + "="*60)
        print("神秘酒馆：「蝶梦亭」")
        print("="*60)
        print()
        
        print("推开酒馆的门，温暖的空气扑面而来。")
        print("酒馆里坐着几个客人，但没有人说话。")
        print("他们只是静静地坐着，面前放着没有动过的酒杯。")
        print()
        
        print("更诡异的是，每个人的头顶都飞舞着一只")
        print("半透明的蓝色蝴蝶，像是在守护他们，")
        print("又像是在监视他们。")
        print()
        
        # 走到吧台前
        print("吧台后面站着一个年轻男人，")
        print("他穿着一件白色衬衫，正在擦拭杯子。")
        print("他的动作很机械，像是重复了千百遍。")
        print()
        
        print("「新来的？」男人抬起头，")
        print("「我是这里的酒保，叫我白就好。」")
        print("「想喝点什么？不过我建议你……")
        print("不要喝这里任何东西。」")
        print()
        
        # NPC对话
        print("【白】")
        print("1. 为什么不要喝")
        print("2. 那些客人怎么了")
        print("3. 请求帮助")
        print()
        
        choice = input("你想说什么？(1/2/3): ")
        
        if choice == "1":
            self.tavern_ask_drink()
        elif choice == "2":
            self.tavern_ask_guests()
        else:
            self.tavern_ask_help()
    
    def tavern_ask_drink(self):
        """询问为什么不要喝"""
        print()
        print("白压低声音：")
        print("「这里的酒是用记忆酿的。」")
        print("「每喝一杯，你就会忘记一件事。」")
        print("「那些客人……他们已经忘记了自己是谁，")
        print("只记得要坐在这里，等蝴蝶带他们走。」")
        print()
        print("白的手微微颤抖，")
        print("「我也喝过。我现在只记得自己的名字，")
        print("和一件事……这个镇子是活的。」")
        print()
        print("【获得线索】酒的特殊性质")
        self.flags["知道酒的秘密"] = True
        self.inventory.append("线索：酒会遗忘")
        
        print("按回车键继续...")
        input()
    
    def tavern_ask_guests(self):
        """询问客人"""
        print()
        print("白看了一眼那些沉默的客人。")
        print("「他们不是镇上的居民。」")
        print("他们都是外乡人，和你们一样。」")
        print()
        print("有的人来了几天，有的人来了几年。」")
        print("他们都在寻找离开的办法，但最后……」")
        print("白没有说完，但索隆明白了他的意思。")
        print()
        print("「我之所以还清醒，是因为我找到了」")
        print("一个秘密。」")
        print()
        
        print("【白】要听听我的秘密吗？(yes/no)")
        choice = input()
        
        if choice.lower() == "yes":
            print("\n白从吧台下拿出一张破旧的地图。")
            print("「镇子中央有一口井。」")
            print("井底下……有一扇门。」")
            print("门后面是什么，我不知道。」")
            print("但所有的蝴蝶，最终都会飞向那里。」")
            print()
            print("【获得物品】破旧地图")
            self.inventory.append("物品：破旧地图")
            self.flags["知道井的秘密"] = True
        else:
            print("\n白点点头：")
            print("没关系，等你准备好了再说。」")
        
        print("\n按回车键继续...")
        input()
    
    def tavern_ask_help(self):
        """请求帮助"""
        print()
        print("白沉默了很久。")
        print("「我能帮你们的只有一件事。」")
        print()
        print("他从吧台下拿出一盏蓝色的灯。")
        print("这是蝶灯。点亮它，")
        print("你就能看见蝴蝶的记忆。」")
        print("但警告你们……有些记忆，")
        print("看见了就回不去了。」")
        print()
        
        print("【获得物品】蓝色蝶灯")
        self.inventory.append("物品：蓝色蝶灯")
        self.flags["拥有蝶灯"] = True
        
        print("\n按回车键继续...")
        input()
    
    def ancient_stele(self):
        """古老的石碑"""
        print("\n" + "="*60)
        print("古老石碑：「镇魂碑」")
        print("="*60)
        print()
        
        print("石碑立在街道中央，像是从一开始就长在那里。")
        print("碑身布满青苔，但上面的字迹依然清晰。")
        print()
        
        print("「蝶栖镇镇魂碑」")
        print("立碑者：蝶栖镇全体居民")
        print("立于：蝴蝶元年（即三十年前）")
        print()
        
        print("碑文如下：")
        print("「此地死者不葬，化为飞蝶。」")
        print("「生者不离，离者化蝶。」")
        print("「唯有真相，可破此局。」")
        print("「蝴蝶非死，乃记忆之载体。」")
        print("「集齐七蝶，可开归途之门。」")
        print()
        
        # 解密环节
        print("【解密】石碑底部有一个机关")
        print("机关上有七个凹槽，应该对应「七蝶」。")
        print()
        print("凹槽周围刻着一段话：")
        print("「第一蝶在开始之处」")
        print("第三蝶在记忆之所」")
        print("第五蝶在沉默者手中」")
        print("第七蝶在井底之门」")
        print()
        
        print("索隆摸了摸口袋。")
        print("【当前拥有的蝴蝶相关物品】")
        for item in self.inventory:
            if "蝴蝶" in item or "蝶" in item:
                print(f"  - {item}")
        
        print("\n要继续调查吗？(yes/no)")
        choice = input()
        
        if choice.lower() == "yes":
            print("\n索隆仔细观察石碑的周围。")
            print()
            print("他发现石碑底部有一些新的划痕，")
            print("像是有人最近在这里做过什么。")
            print()
            print("划痕组成了一行小字：")
            print("「古伊娜来过这里——」")
            print("后面的字迹被刻意抹去了。")
            print()
            print("【获得线索】古伊娜调查过石碑")
            self.flags["古伊娜调查过石碑"] = True
        else:
            print("\n索隆决定先离开这里。")
        
        print("\n按回车键继续...")
        input()

# 运行游戏
if __name__ == "__main__":
    game = Game()
    game.start()
