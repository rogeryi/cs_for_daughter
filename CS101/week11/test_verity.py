import unittest
from types import SimpleNamespace
from unittest.mock import patch

import pygame

import verity_game
from verity import (
    STATE_MONSTER,
    STATE_NORMAL,
    STATE_RECOVERING,
    Verity,
)


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


class VerityStateMachineTests(unittest.TestCase):
    def make_monster(self):
        verity = Verity("Verity")
        verity.leave_temporarily()
        verity.leave_temporarily()
        verity.leave_temporarily()
        return verity

    def test_zero_mood_turns_verity_into_monster(self):
        verity = self.make_monster()

        self.assertEqual(0, verity.mood)
        self.assertEqual(STATE_MONSTER, verity.state)
        self.assertEqual("你真的还在乎我吗？", verity.message)

    def test_monster_rejects_daily_actions_without_changes(self):
        verity = self.make_monster()
        before = (
            verity.mood,
            verity.fullness,
            verity.cleanliness,
            verity.energy,
            verity.bond,
            verity.outfit,
        )

        self.assertFalse(verity.feed())

        after = (
            verity.mood,
            verity.fullness,
            verity.cleanliness,
            verity.energy,
            verity.bond,
            verity.outfit,
        )
        self.assertEqual(before, after)

    def test_apology_starts_recovery(self):
        verity = self.make_monster()

        self.assertTrue(verity.apologize())

        self.assertEqual(STATE_RECOVERING, verity.state)
        self.assertEqual(0.0, verity.recovery_elapsed)
        self.assertEqual(
            "我听见你的道歉了……再给我们一次机会。",
            verity.message,
        )

    def test_showing_weakness_starts_recovery(self):
        verity = self.make_monster()

        self.assertTrue(verity.show_weakness())

        self.assertEqual(STATE_RECOVERING, verity.state)
        self.assertEqual(
            "原来你也会难过……我愿意再相信你。",
            verity.message,
        )

    def test_recovery_finishes_after_one_second(self):
        verity = self.make_monster()
        verity.apologize()

        self.assertFalse(verity.update_recovery(0.9))
        self.assertEqual(STATE_RECOVERING, verity.state)

        self.assertTrue(verity.update_recovery(0.11))
        self.assertEqual(STATE_NORMAL, verity.state)
        self.assertEqual(30, verity.mood)
        self.assertEqual(0.0, verity.recovery_elapsed)
        self.assertEqual(
            "我回来了，但请再温柔一点。",
            verity.message,
        )

    def test_recovery_actions_are_rejected_in_normal_state(self):
        verity = Verity("Verity")

        self.assertFalse(verity.apologize())
        self.assertFalse(verity.show_weakness())
        self.assertFalse(verity.update_recovery(1.0))


class VerityExpressionRenderTests(unittest.TestCase):
    def test_high_and_low_moods_use_matching_mouth_directions(self):
        verity_game.screen = SimpleNamespace(surface=pygame.Surface((960, 640)))

        high_mood_verity = Verity("Verity")
        high_mood_verity.mood = 70
        verity_game.verity = high_mood_verity
        with patch.object(verity_game, "draw_outfit"), patch.object(
            verity_game.pygame.draw,
            "arc",
        ) as high_mood_arc:
            verity_game.draw_normal_face((480, 350), verity_game.YELLOW)

        low_mood_verity = Verity("Verity")
        low_mood_verity.mood = 0
        verity_game.verity = low_mood_verity
        with patch.object(verity_game, "draw_outfit"), patch.object(
            verity_game.pygame.draw,
            "arc",
        ) as low_mood_arc:
            verity_game.draw_normal_face((480, 350), verity_game.YELLOW)

        self.assertEqual((3.14, 6.28), high_mood_arc.call_args.args[3:5])
        self.assertEqual((0, 3.14), low_mood_arc.call_args.args[3:5])


if __name__ == "__main__":
    unittest.main()
