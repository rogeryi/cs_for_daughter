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
