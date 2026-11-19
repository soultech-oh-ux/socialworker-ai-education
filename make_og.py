# -*- coding: utf-8 -*-
"""공유용 썸네일(OG 이미지) 생성 — 1200x630 PNG. 맑은 고딕."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BD = "C:/Windows/Fonts/malgunbd.ttf"
RG = "C:/Windows/Fonts/malgun.ttf"
WHITE = (255, 255, 255)
GOLD = (255, 224, 138)

def f(path, size): return ImageFont.truetype(path, size)

def vgrad(top, bot):
    img = Image.new("RGB", (W, H), top); px = img.load()
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] + (bot[i]-top[i])*t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    return img

def tw(draw, text, font):
    b = draw.textbbox((0,0), text, font=font); return b[2]-b[0]

def make(fn, top, bot, badge, title_lines, subtitle, chips):
    img = vgrad(top, bot); d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([28,28,W-28,H-28], radius=26, outline=(255,255,255,70), width=2)
    # 배지 (테두리 pill)
    bf = f(BD,24); bw = tw(d, badge, bf)
    d.rounded_rectangle([70,84,70+bw+44,84+58], radius=29, outline=(255,255,255,230), width=2)
    d.text((70+22, 84+16), badge, font=bf, fill=(255,255,255))
    # 타이틀
    y = 182; fo = f(BD,72)
    for ln in title_lines:
        x = 70
        for seg, col in ln:
            d.text((x, y), seg, font=fo, fill=col); x += tw(d, seg, fo)
        y += 92
    # 서브타이틀
    d.text((72, y+12), subtitle, font=f(RG,31), fill=(228,244,234))
    # 하단 칩
    cx = 70; cy = H-120; cf = f(BD,27)
    for ctext, cbg, cfg in chips:
        w = tw(d, ctext, cf)
        d.rounded_rectangle([cx,cy,cx+w+40,cy+52], radius=26, fill=cbg)
        d.text((cx+20, cy+11), ctext, font=cf, fill=cfg)
        cx += w+40+14
    # 우하단
    d.text((W-352, H-74), "AI EDUCATION", font=f(BD,22), fill=(255,255,255))
    d.text((W-352, H-46), "for Social Workers", font=f(RG,20), fill=(222,236,228))
    img.save(fn, "PNG"); print("saved", fn)

# 메인
make("og-cover.png", (23,58,40), (47,125,79),
     "AI EDUCATION FOR SOCIAL WORKERS",
     [[("현장에서 바로 쓰는 ", WHITE)],
      [("사회복지사 ", WHITE), ("실무 AI", GOLD), (" 교육", WHITE)]],
     "상담·기록·기획·홍보·평가에 바로 쓰는 AI  |  토요일 2시간 × 4주",
     [("기초반", (255,255,255,40), WHITE), ("중급반", (255,255,255,40), WHITE), ("고급반", (255,255,255,40), WHITE)])

# 기초반
make("gicho-og.png", (27,58,40), (47,125,79),
     "기초반 · BASIC",
     [[("AI 처음이어도 OK", WHITE)],
      [("매일의 글쓰기가 ", WHITE), ("10분", GOLD), ("으로", WHITE)]],
     "안내문·문자·요약·상담일지  |  토요일 2시간 × 4주",
     [("프롬프트 기초", (255,255,255,38), WHITE), ("정보검색", (255,255,255,38), WHITE), ("개인정보 안전", (255,255,255,38), WHITE)])

# 중급반
make("junggeup-og.png", (19,58,58), (31,125,125),
     "중급반 · INTERMEDIATE",
     [[("실무 산출물을 ", WHITE), ("AI", GOLD), ("로", WHITE)],
      [("질과 속도를 동시에", WHITE)]],
     "사례기록·사업계획서·홍보물·데이터  |  토요일 2시간 × 4주",
     [("사례기록", (255,255,255,38), WHITE), ("카드뉴스", (255,255,255,38), WHITE), ("설문·녹취", (255,255,255,38), WHITE)])

# 고급반
make("gogeup-og.png", (42,36,64), (90,63,125),
     "고급반 · ADVANCED",
     [[("반복 업무를 ", WHITE), ("자동화", GOLD), ("하고", WHITE)],
      [("기관의 역량으로", WHITE)]],
     "AI 비서·공모 제안서·평가·기관 가이드  |  토요일 2시간 × 4주",
     [("자동화", (255,255,255,38), WHITE), ("공모·평가", (255,255,255,38), WHITE), ("기관 확산", (255,255,255,38), WHITE)])
