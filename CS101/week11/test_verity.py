import unittest

from verity import STATE_NORMAL, Verity


class VerityBasicsTests(unittest.TestCase):
    def test_initial_state(self):
        verity = Verity("Verity")

        self.assertEqual("Verity", verity.name)
        self.assertEqual(70, verity.mood)
        self.assertEqual(60, verity.fullness)
        self.assertEqual(70, verity.cleanliness)
        self.assertEqual(70, verity.energy)
        self.assertEqual(20, verity.bond)
        self.assertEqual("无", verity.outfit)
        self.assertEqual(STATE_NORMAL, verity.state)
        self.assertEqual("今天想和我做什么？", verity.message)

    def test_feed_changes_stats_and_dialogue(self):
        verity = Verity("Verity")

        result = verity.feed()

        self.assertTrue(result)
        self.assertEqual(78, verity.mood)
        self.assertEqual(85, verity.fullness)
        self.assertEqual(68, verity.cleanliness)
        self.assertEqual(72, verity.energy)
        self.assertEqual(23, verity.bond)
        self.assertEqual("谢谢！这份点心刚刚好。", verity.message)

    def test_play_changes_stats_and_dialogue(self):
        verity = Verity("Verity")

        self.assertTrue(verity.play())

        self.assertEqual(85, verity.mood)
        self.assertEqual(52, verity.fullness)
        self.assertEqual(65, verity.cleanliness)
        self.assertEqual(55, verity.energy)
        self.assertEqual(30, verity.bond)
        self.assertEqual("再来一次！我还没玩够呢！", verity.message)

    def test_bathe_changes_stats_and_dialogue(self):
        verity = Verity("Verity")

        self.assertTrue(verity.bathe())

        self.assertEqual(75, verity.mood)
        self.assertEqual(100, verity.cleanliness)
        self.assertEqual(67, verity.energy)
        self.assertEqual(26, verity.bond)
        self.assertEqual("泡泡软绵绵的，我变得亮晶晶啦！", verity.message)

    def test_talk_changes_stats_and_dialogue(self):
        verity = Verity("Verity")

        self.assertTrue(verity.talk())

        self.assertEqual(80, verity.mood)
        self.assertEqual(69, verity.energy)
        self.assertEqual(32, verity.bond)
        self.assertEqual(
            "我喜欢听你说话，也喜欢你听我说。",
            verity.message,
        )

    def test_dress_up_cycles_outfits_and_dialogue(self):
        verity = Verity("Verity")

        expected = (
            ("蝴蝶结", "蝴蝶结适合我吗？"),
            ("帽子", "这顶帽子让我像个冒险家！"),
            ("眼镜", "戴上眼镜，我看起来很聪明吧？"),
            ("无", "今天先做原来的自己。"),
        )

        for outfit, message in expected:
            self.assertTrue(verity.dress_up())
            self.assertEqual(outfit, verity.outfit)
            self.assertEqual(message, verity.message)

    def test_leave_temporarily_hurts_mood_and_bond(self):
        verity = Verity("Verity")

        self.assertTrue(verity.leave_temporarily())

        self.assertEqual(45, verity.mood)
        self.assertEqual(10, verity.bond)
        self.assertEqual("你要走了吗……我会在这里等你。", verity.message)

    def test_all_stats_are_clamped_between_zero_and_one_hundred(self):
        verity = Verity("Verity")
        verity.mood = 99
        verity.fullness = 99
        verity.cleanliness = 1
        verity.energy = 99
        verity.bond = 99

        verity.feed()

        self.assertEqual(100, verity.mood)
        self.assertEqual(100, verity.fullness)
        self.assertEqual(0, verity.cleanliness)
        self.assertEqual(100, verity.energy)
        self.assertEqual(100, verity.bond)


if __name__ == "__main__":
    unittest.main()
