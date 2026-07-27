STATE_NORMAL = "normal"
STATE_MONSTER = "monster"
STATE_RECOVERING = "recovering"

OUTFITS = ("无", "蝴蝶结", "帽子", "眼镜")


class Verity:
    """黄色小球养成角色。"""

    def __init__(self, name):
        self.name = name
        self.mood = 70
        self.fullness = 60
        self.cleanliness = 70
        self.energy = 70
        self.bond = 20
        self.outfit = "无"
        self.state = STATE_NORMAL
        self.message = "今天想和我做什么？"
        self.recovery_elapsed = 0.0

    def _clamp_stats(self):
        self.mood = max(0, min(100, self.mood))
        self.fullness = max(0, min(100, self.fullness))
        self.cleanliness = max(0, min(100, self.cleanliness))
        self.energy = max(0, min(100, self.energy))
        self.bond = max(0, min(100, self.bond))

    def _can_do_daily_action(self):
        return self.state == STATE_NORMAL

    def _finish_daily_action(self, message):
        self._clamp_stats()
        self.message = message
        self._check_state()
        return True

    def _check_state(self):
        if self.state == STATE_NORMAL and self.mood == 0:
            self.state = STATE_MONSTER
            self.message = "你真的还在乎我吗？"

    def feed(self):
        if not self._can_do_daily_action():
            return False

        self.mood += 8
        self.fullness += 25
        self.cleanliness -= 2
        self.energy += 2
        self.bond += 3
        return self._finish_daily_action("谢谢！这份点心刚刚好。")

    def play(self):
        if not self._can_do_daily_action():
            return False

        self.mood += 15
        self.fullness -= 8
        self.cleanliness -= 5
        self.energy -= 15
        self.bond += 10
        return self._finish_daily_action("再来一次！我还没玩够呢！")

    def bathe(self):
        if not self._can_do_daily_action():
            return False

        self.mood += 5
        self.cleanliness += 30
        self.energy -= 3
        self.bond += 6
        return self._finish_daily_action(
            "泡泡软绵绵的，我变得亮晶晶啦！"
        )

    def talk(self):
        if not self._can_do_daily_action():
            return False

        self.mood += 10
        self.energy -= 1
        self.bond += 12
        return self._finish_daily_action(
            "我喜欢听你说话，也喜欢你听我说。"
        )

    def dress_up(self):
        if not self._can_do_daily_action():
            return False

        current_index = OUTFITS.index(self.outfit)
        next_index = (current_index + 1) % len(OUTFITS)
        self.outfit = OUTFITS[next_index]
        self.mood += 12
        self.energy -= 4
        self.bond += 8

        messages = {
            "蝴蝶结": "蝴蝶结适合我吗？",
            "帽子": "这顶帽子让我像个冒险家！",
            "眼镜": "戴上眼镜，我看起来很聪明吧？",
            "无": "今天先做原来的自己。",
        }
        return self._finish_daily_action(messages[self.outfit])

    def leave_temporarily(self):
        if not self._can_do_daily_action():
            return False

        self.mood -= 25
        self.bond -= 10
        return self._finish_daily_action(
            "你要走了吗……我会在这里等你。"
        )
