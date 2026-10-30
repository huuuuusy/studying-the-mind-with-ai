"""Write banner.svg and route.svg here, with their Chinese versions (*.zh.svg):

    python3 docs/figures/make_diagrams.py

Standard library only. The drawings in talk/ (plate1-4.svg, cover.svg) are the chapter
plates of the talk; this script places them and draws the diagrams around them in the
talk's palette: NTU navy for structure and text, one colour per part of the talk
(Part 1 blue, Part 2 teal, Part 3 amber).
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY, INK, INK2, MUTE, RULE, PAPER = "#1E2A5E", "#16213D", "#465069", "#8A91A3", "#DDE1EA", "#F5F6FA"
CHECK = {1: "#1F4FA3", 2: "#0E8C7E", 3: "#9A6700"}
WASH = {1: "#EBEFF7", 2: "#ECF4F4", 3: "#F6F1E8", 4: "#EBECF1"}       # the plates' own background washes
FONT = "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "SFMono-Regular, Menlo, Consolas, monospace"
FONT_ZH = FONT.replace(", sans-serif", ", 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Noto Sans CJK SC', 'Source Han Sans SC', sans-serif")

LANG = "en"   # set by main() while each language is drawn


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, fill=INK2, weight=400, anchor="start", family=None, extra=""):
    family = family or (FONT_ZH if LANG == "zh" else FONT)
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{extra}>{esc(s)}</text>')


def plate(name, x, y, w):
    """Inline one of the talk's plate SVGs at (x, y), width w, keeping its aspect ratio."""
    src = open(os.path.join(HERE, "talk", f"{name}.svg"), encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    vw, vh = (float(v) for v in vb.split()[2:])
    body = src[src.index(">") + 1:src.rindex("</svg>")]
    return f'<svg x="{x}" y="{y}" width="{w}" height="{w * vh / vw:.1f}" viewBox="{vb}">{body}</svg>'


def badge(cx, cy, n, r=13):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CHECK[n]}" stroke="#FFFFFF" stroke-width="2"/>'
            + text(cx, cy + 5, str(n), 14, "#FFFFFF", 700, "middle"))


def arrow(x1, y1, x2, y2, col=MUTE, w=1.6):
    """A line with a drawn triangular head (no SVG markers, so every renderer shows it)."""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 9 * math.cos(a), y2 - 9 * math.sin(a)
    p1 = (hx + 4.5 * math.sin(a), hy - 4.5 * math.cos(a))
    p2 = (hx - 4.5 * math.sin(a), hy + 4.5 * math.cos(a))
    return (f'<line x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>')


def box(x, y, w, h, fill="#FFFFFF", stroke=None, sw=2, r=10):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{s}/>'


def kicker(x, y, s, col=NAVY):
    if LANG == "zh":
        return text(x, y, s, 13.5, col, 700, extra=' letter-spacing="0.6"')
    return text(x, y, s.upper(), 12.5, col, 700, extra=' letter-spacing="1.2"')


def svg(w, h, title, parts):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'<title>{esc(title)}</title>\n<rect width="{w}" height="{h}" fill="#FFFFFF"/>\n'
            + "\n".join(parts) + "\n</svg>\n")


T = {   # V8 of the talk: the first three questions and their checks
    "en": dict(
        habits={1: (("Compare the mistakes,", "not only the scores"), "Right answer, right reason?", "Part 1 · One person"),
                2: (("Compare with a group,", "not one person"), "Whose standard does it follow?", "Part 2 · A group"),
                3: (("Compare with", "real people"), "Like us enough to study us?", "Part 3 · A society")},
        in_talk="In the talk: ",
        banner_title="Checks from the talk Studying the Human Mind with AI",
    ),
    "zh": dict(
        habits={1: (("比错误，不只比分数",), "答对了，理由也对吗？", "第 1 部分 · 一个人"),
                2: (("拿一群人比，不拿一个人比",), "它遵循谁的标准？", "第 2 部分 · 一群人"),
                3: (("拿真实的人比",), "它像我们，像到能研究我们吗？", "第 3 部分 · 一个社会")},
        in_talk="讲座里：",
        banner_title="讲座 Studying the Human Mind with AI 中的检验",
    ),
}


def banner():
    """The talk's three habits, with its three plates (public reading companion)."""
    L = T[LANG]
    p = []
    for i, n in enumerate((1, 2, 3)):
        x = 24 + i * 312
        title, q, talk = L["habits"][n]
        p.append(box(x, 16, 288, 236, WASH[n], r=14))
        p.append(plate(f"plate{n}", x + 12, 24, 264))
        p.append(badge(x + 22, 284, n, 14))
        if len(title) == 2:
            p.append(text(x + 44, 282, title[0], 16, INK, 700))
            p.append(text(x + 44, 302, title[1], 16, INK, 700))
        else:
            p.append(text(x + 44, 290, title[0], 17, INK, 700))
        p.append(text(x + 8, 330, q, 12.8, INK2))
        p.append(text(x + 8, 351, L["in_talk"] + talk, 13, MUTE))
    return svg(960, 366, L["banner_title"], p)


R = {   # the route of the talk, V8 (2026-10-25): four questions; the arrow turns from psychology-for-AI to AI-for-psychology
    "en": dict(
        k="AI learns from people; checked against people, it can help us study people",
        stops=[("One person", "Right answer,", "right reason?"), ("A group", "Whose standard", "does it follow?"),
               ("A society", "Like us enough", "to study us?"), ("Your research", "How can you", "use it?")],
        left="Psychology helps AI", right="AI helps psychology",
        left2="Behavioral analysis", right2="Role simulation",
        title="The route of the talk: four questions, from one person to your own research"),
    "zh": dict(
        k="AI 向人学习；经过人的检验之后，它也能帮助我们研究人",
        stops=[("一个人", "答对了，", "理由也对吗？"), ("一群人", "它遵循", "谁的标准？"),
               ("一个社会", "像我们，像到", "能研究我们吗？"), ("你的研究", "你可以", "怎样用它？")],
        left="心理学帮 AI", right="AI 帮心理学",
        left2="行为分析", right2="角色模拟",
        title="讲座的路线：四个问题，从一个人到你自己的研究"),
}


def route():
    """The talk's four questions on one path, and the arrow that turns from psychology-for-AI to AI-for-psychology."""
    L = R[LANG]
    p = [kicker(24, 34, L["k"])]
    p.append(f'<line x1="130" y1="186" x2="829" y2="186" stroke="{RULE}" stroke-width="3" stroke-linecap="round"/>')
    for i, (name, q1, q2) in enumerate(L["stops"]):
        cx = 130 + i * 233
        n = i + 1
        col = CHECK.get(n, NAVY)
        p += [box(cx - 110, 56, 220, 108, WASH[n], r=12), plate(f"plate{n}", cx - 104, 62, 92),
              text(cx - 2, 92, name, 14, INK, 700), text(cx - 2, 116, q1, 12, INK2), text(cx - 2, 134, q2, 12, INK2),
              f'<circle cx="{cx}" cy="186" r="9" fill="{col}" stroke="#FFFFFF" stroke-width="2"/>',
              text(cx, 190.5, str(n), 11, "#FFFFFF", 700, "middle")]
    # the arrow underneath: psychology helps AI (parts 1-2), then AI helps psychology (parts 3-4)
    p += [arrow(130, 222, 462, 222, NAVY, 2), text(130, 244, L["left"], 13, INK, 700),
          arrow(497, 222, 829, 222, CHECK[3], 2), text(829, 244, L["right"], 13, INK, 700, "end"),
          text(130, 263, L["left2"], 12.5, INK2), text(829, 263, L["right2"], 12.5, INK2, anchor="end"),
          f'<line x1="479" y1="208" x2="479" y2="236" stroke="{RULE}" stroke-width="1.5" stroke-dasharray="3 3"/>']
    return svg(960, 278, L["title"], p)


def main():
    global LANG
    for LANG, suffix in (("en", ".svg"), ("zh", ".zh.svg")):
        for name, make in (("banner", banner), ("route", route)):
            path = os.path.join(HERE, name + suffix)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(make())
            print(os.path.relpath(path))


if __name__ == "__main__":
    main()
