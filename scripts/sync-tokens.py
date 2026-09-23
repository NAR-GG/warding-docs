#!/usr/bin/env python3
"""assets/tokens.css 를 앱 색 원천(app_colors.dart)에서 다시 만든다. 앱 색이 바뀌면 실행한다.

    python3 scripts/sync-tokens.py
"""
import pathlib
import re
import urllib.request

SRC = "https://raw.githubusercontent.com/NAR-GG/warding-mobile-repo/main/lib/styles/app_colors.dart"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "tokens.css"
DIRECTION = {"centerLeft": "90deg", "topCenter": "180deg", "topLeft": "135deg"}


def css(argb):
    a, r, g, b = (int(argb[i:i + 2], 16) for i in (0, 2, 4, 6))
    return f"#{argb[2:].upper()}" if a == 255 else f"rgba({r},{g},{b},{a / 255:.2f})"


dart = urllib.request.urlopen(SRC).read().decode()
lines = [f"  --{name}: {css(v)};"
         for name, v in re.findall(r"static const Color (\w+) = Color\(\s*0x([0-9A-Fa-f]{8})", dart)]
# 별칭(narPlayedChampBg = narDark800)은 원래 토큰을 가리킨다
lines += [f"  --{name}: var(--{ref});"
          for name, ref in re.findall(r"static const Color (\w+) = (\w+);", dart)]

for name, body in re.findall(r"static const LinearGradient (\w+) = LinearGradient\((.*?)\);", dart, re.S):
    colors = [css(v) for v in re.findall(r"Color\(\s*0x([0-9A-Fa-f]{8})", body)]
    stops = re.search(r"stops: \[(.*?)\]", body)
    if stops:
        colors = [f"{c} {float(s) * 100:.2f}%" for c, s in zip(colors, stops.group(1).split(","))]
    begin = re.search(r"begin: Alignment\.(\w+)", body)
    deg = DIRECTION.get(begin.group(1) if begin else "centerLeft", "90deg")
    lines.append(f"  --{name}: linear-gradient({deg}, {', '.join(colors)});")

OUT.write_text("/* 자동 생성 — scripts/sync-tokens.py. 손으로 고치지 않는다.\n"
               f"   원천: {SRC} */\n:root {{\n" + "\n".join(lines) + "\n}\n")
print(f"{OUT.name}: 토큰 {len(lines)}개")
