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
        try:
            path = pygame.font.match_font(name)
        except TypeError:
            # pygame-ce 2.5.7 cannot enumerate Windows fonts on Python 3.14.
            return pygame.font.Font("C:/Windows/Fonts/msyh.ttc", size)
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


def draw_room():
    screen.fill(BACKGROUND)
    screen.draw.filled_rect(Rect(0, 500, WIDTH, 140), FLOOR)
    screen.draw.filled_rect(Rect(65, 180, 120, 125), (118, 184, 210))
    screen.draw.rect(Rect(65, 180, 120, 125), PANEL)

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
        pygame.draw.arc(screen.surface, INK, Rect(x - 28, y - 5, 56, 38), 3.14, 6.28, 4)
    elif verity.mood >= 30:
        pygame.draw.line(screen.surface, INK, (x - 20, y + 22), (x + 20, y + 22), 4)
    else:
        pygame.draw.arc(screen.surface, INK, Rect(x - 28, y + 10, 56, 38), 0, 3.14, 4)

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
    pygame.draw.line(
        screen.surface,
        (255, 255, 255),
        (x - 42, y - 25),
        (x - 12, y - 10),
        5,
    )
    pygame.draw.line(
        screen.surface,
        (255, 255, 255),
        (x + 42, y - 25),
        (x + 12, y - 10),
        5,
    )
    pygame.draw.line(
        screen.surface,
        (255, 255, 255),
        (x - 28, y + 30),
        (x + 28, y + 30),
        5,
    )


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

    buttons = DAILY_BUTTONS if verity.state == STATE_NORMAL else RECOVERY_BUTTONS
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
