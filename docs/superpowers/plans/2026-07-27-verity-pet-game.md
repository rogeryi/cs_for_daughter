# Verity Pet Game Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Pygame Zero virtual-pet game in which the `Verity` object responds to six daily interactions, tracks five attributes, becomes a monster at zero mood, and recovers after an apology or show of weakness.

**Architecture:** Keep all state and behavior in a Pygame-independent `Verity` class, including dialogue and the three-state machine. Keep rendering and mouse input in a separate Pygame Zero module so the object logic can be tested without opening a window.

**Tech Stack:** Python 3, standard-library `unittest`, Pygame, Pygame Zero.

## Global Constraints

- Create files only under `CS101/week11/`.
- Use `Verity("Verity")` as the single game object.
- Track `mood`, `fullness`, `cleanliness`, `energy`, and `bond`, each clamped to `0..100`.
- Initial values are mood `70`, fullness `60`, cleanliness `70`, energy `70`, and bond `20`.
- State changes happen only because of player interactions; there is no automatic decay.
- Use exactly three states: `normal`, `monster`, and `recovering`.
- Mood `0` changes `normal` to `monster`.
- `apologize()` and `show_weakness()` change `monster` to `recovering`.
- Recovery lasts `1.0` second and returns to `normal` with mood `30`.
- Draw Verity with Pygame primitives so the game does not depend on color-Emoji font support.
- Store interaction dialogue in `verity.py`; rendering code only displays `verity.message`.
- Preserve unrelated working-tree changes.

---

## File Map

| File | Responsibility |
|---|---|
| `CS101/week11/verity.py` | Verity attributes, dialogue, actions, outfit cycle, state transitions, recovery timer |
| `CS101/week11/test_verity.py` | Unit tests for all pure object behavior |
| `CS101/week11/verity_game.py` | Pygame Zero window, room drawing, status bars, character drawing, buttons, input and update loop |

---

### Task 1: Create the Verity Object and First Interaction

**Files:**
- Create: `CS101/week11/verity.py`
- Create: `CS101/week11/test_verity.py`

**Interfaces:**
- Produces: `Verity(name: str)`, `Verity.feed() -> bool`
- Produces attributes: `name`, `mood`, `fullness`, `cleanliness`, `energy`, `bond`, `outfit`, `state`, `message`

- [ ] **Step 1: Write failing initialization and feeding tests**

Create `CS101/week11/test_verity.py`:

```python
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
```

- [ ] **Step 2: Run the tests and verify the expected failure**

Run from `CS101/week11`:

```powershell
python test_verity.py
```

Expected: `ModuleNotFoundError: No module named 'verity'`.

- [ ] **Step 3: Implement the minimal Verity class**

Create `CS101/week11/verity.py`:

```python
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
```

- [ ] **Step 4: Run the tests and verify they pass**

Run:

```powershell
python test_verity.py
```

Expected: `Ran 3 tests` and `OK`.

- [ ] **Step 5: Commit the first working object**

```powershell
git add CS101/week11/verity.py CS101/week11/test_verity.py
git commit -m "Week 11: add Verity object and feeding"
```

---

### Task 2: Add Daily Interactions and Dialogue

**Files:**
- Modify: `CS101/week11/verity.py`
- Modify: `CS101/week11/test_verity.py`

**Interfaces:**
- Consumes: `Verity`, `_can_do_daily_action()`, `_finish_daily_action(message)`
- Produces: `play()`, `bathe()`, `talk()`, `dress_up()`, `leave_temporarily()`, all returning `bool`

- [ ] **Step 1: Add failing tests for all remaining daily actions**

Add these methods to `VerityBasicsTests`:

```python
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
```

- [ ] **Step 2: Run the tests and verify they fail**

Run:

```powershell
python test_verity.py
```

Expected: five errors reporting that the new methods do not exist.

- [ ] **Step 3: Implement the remaining daily interactions**

Add to `Verity`:

```python
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
```

- [ ] **Step 4: Run the complete daily-action test suite**

Run:

```powershell
python test_verity.py
```

Expected: `Ran 8 tests` and `OK`.

- [ ] **Step 5: Commit daily interactions**

```powershell
git add CS101/week11/verity.py CS101/week11/test_verity.py
git commit -m "Week 11: add Verity interactions and dialogue"
```

---

### Task 3: Implement Monster and Recovery States

**Files:**
- Modify: `CS101/week11/verity.py`
- Modify: `CS101/week11/test_verity.py`

**Interfaces:**
- Consumes: `STATE_NORMAL`, `STATE_MONSTER`, `STATE_RECOVERING`
- Produces: `apologize() -> bool`, `show_weakness() -> bool`, `update_recovery(dt: float) -> bool`

- [ ] **Step 1: Add failing state-machine tests**

Update the import in `test_verity.py`:

```python
from verity import (
    STATE_MONSTER,
    STATE_NORMAL,
    STATE_RECOVERING,
    Verity,
)
```

Add a new test class:

```python
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
```

- [ ] **Step 2: Run tests and verify state-machine failures**

Run:

```powershell
python test_verity.py
```

Expected: failures because recovery methods do not exist.

- [ ] **Step 3: Implement monster recovery methods**

Add to `Verity`:

```python
    def apologize(self):
        if self.state != STATE_MONSTER:
            return False

        self.state = STATE_RECOVERING
        self.recovery_elapsed = 0.0
        self.message = "我听见你的道歉了……再给我们一次机会。"
        return True

    def show_weakness(self):
        if self.state != STATE_MONSTER:
            return False

        self.state = STATE_RECOVERING
        self.recovery_elapsed = 0.0
        self.message = "原来你也会难过……我愿意再相信你。"
        return True

    def update_recovery(self, dt):
        if self.state != STATE_RECOVERING:
            return False

        self.recovery_elapsed += dt
        if self.recovery_elapsed < 1.0:
            return False

        self.state = STATE_NORMAL
        self.mood = 30
        self.recovery_elapsed = 0.0
        self.message = "我回来了，但请再温柔一点。"
        return True
```

- [ ] **Step 4: Run all logic tests**

Run:

```powershell
python test_verity.py
```

Expected: `Ran 14 tests` and `OK`.

- [ ] **Step 5: Commit the state machine**

```powershell
git add CS101/week11/verity.py CS101/week11/test_verity.py
git commit -m "Week 11: add Verity monster state machine"
```

---

### Task 4: Build the Pygame Zero Interface

**Files:**
- Create: `CS101/week11/verity_game.py`

**Interfaces:**
- Consumes: `Verity`, `STATE_NORMAL`, `STATE_MONSTER`, `STATE_RECOVERING`
- Produces Pygame Zero callbacks: `draw()`, `update(dt)`, `on_mouse_down(pos)`

- [ ] **Step 1: Check the graphical runtime**

Run with the Python installation used for CS101 games:

```powershell
python -c "import pygame, pgzrun; print('Pygame Zero ready')"
```

Expected: `Pygame Zero ready`.

If imports fail, install into that same Python:

```powershell
python -m pip install pygame pgzero
```

Then repeat the import check before continuing.

- [ ] **Step 2: Verify the UI file does not exist yet**

Run from `CS101/week11`:

```powershell
python -m py_compile verity_game.py
```

Expected: failure reporting that `verity_game.py` does not exist.

- [ ] **Step 3: Create the window constants, fonts and button contracts**

Create `CS101/week11/verity_game.py` with:

```python
import pygame
from pygame import Rect

from verity import (
    STATE_MONSTER,
    STATE_NORMAL,
    STATE_RECOVERING,
    Verity,
)

WIDTH = 960
HEIGHT = 640
TITLE = "Verity 的温馨小屋"

BACKGROUND = (207, 234, 241)
FLOOR = (214, 168, 111)
PANEL = (255, 249, 229)
INK = (43, 58, 65)
YELLOW = (255, 216, 61)
PURPLE = (109, 44, 117)

verity = Verity("Verity")

DAILY_BUTTONS = (
    ("喂食", "feed", Rect(22, 558, 140, 56)),
    ("玩耍", "play", Rect(175, 558, 140, 56)),
    ("洗澡", "bathe", Rect(328, 558, 140, 56)),
    ("聊天", "talk", Rect(481, 558, 140, 56)),
    ("装扮", "dress_up", Rect(634, 558, 140, 56)),
    ("暂时离开", "leave_temporarily", Rect(787, 558, 150, 56)),
)

RECOVERY_BUTTONS = (
    ("道歉", "apologize", Rect(210, 558, 240, 56)),
    ("示弱", "show_weakness", Rect(510, 558, 240, 56)),
)

pygame.font.init()


def make_font(size):
    for name in ("Microsoft YaHei", "SimHei", "Arial"):
        path = pygame.font.match_font(name)
        if path:
            return pygame.font.Font(path, size)
    return pygame.font.Font(None, size)


FONTS = {
    18: make_font(18),
    22: make_font(22),
    28: make_font(28),
}


def draw_text(text, center, size=22, color=INK):
    surface = FONTS[size].render(text, True, color)
    rect = surface.get_rect(center=center)
    screen.surface.blit(surface, rect)
```

- [ ] **Step 4: Add room, status-bar and speech drawing**

Add these functions:

```python
def draw_room():
    screen.fill(BACKGROUND)
    screen.draw.filled_rect(Rect(0, 500, WIDTH, 140), FLOOR)
    screen.draw.filled_rect(Rect(65, 180, 120, 125), (118, 184, 210))
    screen.draw.rect(Rect(65, 180, 120, 125), (255, 249, 229))

    pygame.draw.rect(screen.surface, (112, 78, 49), Rect(820, 430, 58, 70))
    pygame.draw.circle(screen.surface, (78, 139, 82), (849, 415), 42)


def draw_status_bars():
    stats = (
        ("心情", verity.mood, (239, 97, 122)),
        ("饱食", verity.fullness, (233, 168, 58)),
        ("清洁", verity.cleanliness, (86, 185, 211)),
        ("体力", verity.energy, (105, 175, 103)),
        ("亲密", verity.bond, (166, 120, 201)),
    )

    for index, (label, value, color) in enumerate(stats):
        x = 20 + index * 186
        draw_text(f"{label} {value}", (x + 75, 42), 18)
        screen.draw.filled_rect(Rect(x, 62, 150, 10), (215, 221, 224))
        screen.draw.filled_rect(
            Rect(x, 62, int(150 * value / 100), 10),
            color,
        )


def draw_speech():
    bubble = Rect(270, 105, 420, 64)
    screen.draw.filled_rect(bubble, (255, 255, 255))
    screen.draw.rect(bubble, INK)
    draw_text(verity.message, bubble.center, 18)
```

- [ ] **Step 5: Add Verity, facial expression and outfit drawing**

Add:

```python
def blend_color(start, end, amount):
    return tuple(
        int(a + (b - a) * amount)
        for a, b in zip(start, end)
    )


def draw_outfit(center):
    x, y = center

    if verity.outfit == "蝴蝶结":
        pygame.draw.circle(screen.surface, (234, 91, 123), (x - 25, y - 56), 15)
        pygame.draw.circle(screen.surface, (234, 91, 123), (x + 25, y - 56), 15)
        pygame.draw.circle(screen.surface, (255, 179, 195), (x, y - 56), 10)
    elif verity.outfit == "帽子":
        pygame.draw.rect(screen.surface, (80, 124, 170), Rect(x - 48, y - 75, 96, 15))
        pygame.draw.rect(screen.surface, (80, 124, 170), Rect(x - 32, y - 118, 64, 45))
    elif verity.outfit == "眼镜":
        pygame.draw.circle(screen.surface, INK, (x - 27, y - 9), 19, 3)
        pygame.draw.circle(screen.surface, INK, (x + 27, y - 9), 19, 3)
        pygame.draw.line(screen.surface, INK, (x - 8, y - 9), (x + 8, y - 9), 3)


def draw_normal_face(center, color):
    x, y = center
    pygame.draw.circle(screen.surface, color, center, 72)
    pygame.draw.circle(screen.surface, INK, (x - 25, y - 13), 6)
    pygame.draw.circle(screen.surface, INK, (x + 25, y - 13), 6)

    if verity.mood >= 60:
        pygame.draw.arc(screen.surface, INK, Rect(x - 28, y - 5, 56, 38), 0, 3.14, 4)
    elif verity.mood >= 30:
        pygame.draw.line(screen.surface, INK, (x - 20, y + 22), (x + 20, y + 22), 4)
    else:
        pygame.draw.arc(screen.surface, INK, Rect(x - 28, y + 10, 56, 38), 3.14, 6.28, 4)

    draw_outfit(center)


def draw_monster(center):
    x, y = center
    points = (
        (x, y - 82),
        (x + 58, y - 60),
        (x + 78, y),
        (x + 50, y + 72),
        (x, y + 60),
        (x - 50, y + 72),
        (x - 78, y),
        (x - 58, y - 60),
    )
    pygame.draw.polygon(screen.surface, PURPLE, points)
    pygame.draw.line(screen.surface, (255, 255, 255), (x - 42, y - 25), (x - 12, y - 10), 5)
    pygame.draw.line(screen.surface, (255, 255, 255), (x + 42, y - 25), (x + 12, y - 10), 5)
    pygame.draw.line(screen.surface, (255, 255, 255), (x - 28, y + 30), (x + 28, y + 30), 5)


def draw_verity():
    center = (WIDTH // 2, 350)

    if verity.state == STATE_MONSTER:
        draw_monster(center)
    elif verity.state == STATE_RECOVERING:
        progress = min(1.0, verity.recovery_elapsed / 1.0)
        color = blend_color(PURPLE, YELLOW, progress)
        draw_normal_face(center, color)
    else:
        draw_normal_face(center, YELLOW)
```

- [ ] **Step 6: Add button drawing and input dispatch**

Add:

```python
def draw_button(label, rect, enabled=True):
    fill = (255, 255, 255) if enabled else (205, 205, 205)
    border = (185, 155, 80) if enabled else (145, 145, 145)
    screen.draw.filled_rect(rect, fill)
    screen.draw.rect(rect, border)
    draw_text(label, rect.center, 18)


def draw_buttons():
    if verity.state == STATE_NORMAL:
        for label, _method_name, rect in DAILY_BUTTONS:
            draw_button(label, rect)
    elif verity.state == STATE_MONSTER:
        for label, _method_name, rect in RECOVERY_BUTTONS:
            draw_button(label, rect)
    else:
        draw_button("正在恢复……", Rect(330, 558, 300, 56), enabled=False)


def on_mouse_down(pos):
    if verity.state == STATE_RECOVERING:
        return

    buttons = (
        DAILY_BUTTONS
        if verity.state == STATE_NORMAL
        else RECOVERY_BUTTONS
    )
    for _label, method_name, rect in buttons:
        if rect.collidepoint(pos):
            method = getattr(verity, method_name)
            method()
            return


def update(dt):
    verity.update_recovery(dt)


def draw():
    draw_room()
    draw_status_bars()
    draw_speech()
    draw_verity()
    draw_buttons()
```

- [ ] **Step 7: Compile both modules**

Run:

```powershell
python -m py_compile verity.py verity_game.py
```

Expected: exit code `0` with no output.

- [ ] **Step 8: Launch the game for a smoke test**

Run:

```powershell
pgzrun verity_game.py
```

Expected: a `960 x 640` window titled `Verity 的温馨小屋`, showing five status bars, Verity, a dialogue bubble and six buttons.

- [ ] **Step 9: Commit the interface**

```powershell
git add CS101/week11/verity_game.py
git commit -m "Week 11: build Verity Pygame Zero interface"
```

---

### Task 5: Complete End-to-End Verification

**Files:**
- Verify: `CS101/week11/verity.py`
- Verify: `CS101/week11/test_verity.py`
- Verify: `CS101/week11/verity_game.py`

**Interfaces:**
- Consumes the complete logic and UI.
- Produces a verified classroom project.

- [ ] **Step 1: Run all unit tests**

Run from `CS101/week11`:

```powershell
python test_verity.py
```

Expected: `Ran 14 tests` and `OK`.

- [ ] **Step 2: Compile all Python files**

Run:

```powershell
python -m py_compile verity.py verity_game.py test_verity.py
```

Expected: exit code `0` with no output.

- [ ] **Step 3: Verify the graphical dependencies**

Run:

```powershell
python -c "import pygame, pgzrun; print(pygame.version.ver)"
```

Expected: a Pygame version number and exit code `0`.

- [ ] **Step 4: Verify normal interactions manually**

Launch:

```powershell
pgzrun verity_game.py
```

Confirm:

1. Each of the six normal buttons changes the exact values from the design.
2. The speech bubble shows the matching Verity dialogue.
3. Four dress-up clicks cycle through bow, hat, glasses and no outfit.
4. No value exceeds `100` or falls below `0`.

- [ ] **Step 5: Verify monster and recovery flow manually**

In the running game:

1. Click “暂时离开” three times.
2. Confirm mood becomes `0`.
3. Confirm Verity becomes a purple monster.
4. Confirm normal buttons disappear.
5. Click “道歉”.
6. Confirm input is disabled for approximately one second.
7. Confirm Verity returns to a yellow ball with mood `30`.
8. Repeat the monster flow and verify “示弱” also recovers.

- [ ] **Step 6: Review the working-tree scope**

Run:

```powershell
git status --short
git diff -- CS101/week11
```

Expected: no changes outside `CS101/week11` were introduced by implementation.

- [ ] **Step 7: Commit any final focused corrections**

Only if verification required corrections:

```powershell
git add CS101/week11/verity.py CS101/week11/verity_game.py CS101/week11/test_verity.py
git commit -m "Week 11: finish Verity interaction game"
```
