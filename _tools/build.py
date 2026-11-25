# -*- coding: utf-8 -*-
"""jokeR site generator
使い方（リポジトリの一番上で）: python3 _tools/build.py .
ページの中身・ナビ・画像の差し替えはこのファイルを直してから実行する。
HTML を直接直すと、次に実行したとき上書きされるので注意。"""
import os, sys
OUT = sys.argv[1]
SITE = "https://joker.lecrin.biz"
VER = "20261125o"
CUR = ' aria-current="page"'

# ---- image slots (写真AC が届いたらここを .jpg に差し替える) ----
IMG = {
  "roulette": "img/ph/roulette.svg",
  "dealer":   "img/photo/store-shuffle.jpg",
  "blackjack":"img/photo/bet-chips.jpg",
  "baccarat": "img/photo/store-dealing.jpg",
  "poker":    "img/photo/royal-flush.jpg",
  "hands":    "img/photo/casino-dealer.jpg",
  "chips":    "img/photo/chips-dice.jpg",
  "highball": "img/photo/cocktails.jpg",
  "hero":     "img/photo/casino-dealer.jpg",
  "lounge":   "img/photo/store-welcome.jpg",
  "rband":    "img/photo/store-dealer.jpg",
  "bjreal":   "img/photo/store-blackjack.jpg",
  "room":     "img/photo/store-photo-tall.jpg",
  "table":    "img/photo/store-table.jpg",
  "shelf":    "img/photo/bar-bottles.jpg",
  "cocktail2":"img/photo/chips-dice.jpg",
  "store":    "img/photo/store-roulette.jpg",
  "bar":      "img/photo/store-bar.jpg",
  "cake":     "img/photo/party-cake.jpg",
  "wine":     "img/photo/party-wine.jpg",
  "bottles":  "img/photo/party-bottles.jpg",
  "pasta":    "img/photo/food-pasta.jpg",
  "ham":      "img/photo/food-ham.jpg",
  "cheese":   "img/photo/food-cheese.jpg",
  "sausage":  "img/photo/food-sausage.jpg",
  "pizza":    "img/photo/food-pizza.jpg",
  "veg":      "img/photo/food-veg.jpg",
  "glasses":  "img/photo/drink-glasses.jpg",
  "whisky":   "img/photo/drink-whisky.jpg",
}

NAV = [  # (path, EN, JP, in side nav)
  ("", "HOME", "ホーム", True),
  ("system/", "SYSTEM", "料金システム", True),
  ("menu/", "MENU", "フード・ドリンク", True),
  ("casino-games/", "CASINO GAMES", "ゲーム解説", True),
  ("access/", "ACCESS", "アクセス", True),
  ("recruit/", "RECRUIT", "スタッフ募集", True),
  ("contact/", "CONTACT", "お問い合わせ", True),
]
TEL = "042-512-9385"
MAIL = "tatikawajoker@gmail.com"
X_URL = "https://x.com/JokerTachikawa"
LINE_URL = "https://lin.ee/YkVqiiWJ"
# 公式SNS（URL が空のものはサイトに出さない。アカウントができたら URL を入れて build し直す）
INSTAGRAM_URL = "https://www.instagram.com/joker_tachikawa_poker/"
TIKTOK_URL = ""
YOUTUBE_URL = ""
THREADS_URL = ""
MAP_EMBED = "https://maps.google.com/maps?q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E7%AB%8B%E5%B7%9D%E5%B8%82%E9%8C%A6%E7%94%BA1-2-13&z=17&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E7%AB%8B%E5%B7%9D%E5%B8%82%E9%8C%A6%E7%94%BA1-2-13+%E4%B8%AD%E5%B3%B6%E3%83%93%E3%83%AB"

IC_X = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.9 2H22l-7.6 8.7L23.3 22h-7l-5.5-7.2L4.5 22H1.4l8.1-9.3L1 2h7.2l5 6.6L18.9 2zm-1.2 18h1.7L7.4 3.9H5.6L17.7 20z"/></svg>'
IC_LINE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.5 2 2 5.6 2 10.1c0 4 3.6 7.4 8.4 8 .3.1.8.2.9.5.1.3.1.7 0 1l-.1.9c0 .3-.2 1 .9.5s5.9-3.5 8-6C21.4 13.4 22 11.8 22 10.1 22 5.6 17.5 2 12 2z"/></svg>'
IC_TEL = '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 013 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>'

def logo(sub=True):
    s = '<span class="logo" aria-label="jokeR"><span class="logo__word">j<span class="logo__chip"></span>ke<span class="R">R</span></span>'
    if sub: s += '<span class="logo__sub">AMUSEMENT CASINO</span>'
    return s + '</span>'

IC_IG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
IC_TT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.7 5.7 0 1 0 4.9 5.7V9.1a7.3 7.3 0 0 0 4.3 1.4V7.4a4.3 4.3 0 0 1-3.2-1.6z"/></svg>'
IC_YT = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l5.8 3.1-5.8 3.1z"/></svg>'

IC_TH = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.7 11.1c-.1 0-.2-.1-.3-.1-.2-3.2-2-5-4.9-5-1.8 0-3.2.8-4.1 2.1l1.6 1.1c.7-1 1.7-1.2 2.5-1.2 1 0 1.8.3 2.2.9.3.4.6 1.1.6 1.8-.9-.2-1.8-.2-2.8-.2-2.8.2-4.6 1.8-4.5 4.1.1 1.2.7 2.2 1.7 2.8.8.5 1.9.8 3 .7 1.5-.1 2.6-.6 3.4-1.7.6-.8 1-1.8 1.1-3.1.7.4 1.2 1 1.5 1.6.5 1.2.5 3.1-1 4.6-1.4 1.4-3 2-5.5 2-2.8 0-4.9-.9-6.2-2.6C4.8 17.1 4.2 15 4.2 12.3s.6-4.8 1.8-6.3C7.4 4.3 9.4 3.4 12.2 3.4s4.9.9 6.3 2.6c.7.9 1.2 1.9 1.5 3.1l1.9-.5c-.4-1.5-1-2.8-1.9-3.9-1.8-2.3-4.4-3.4-7.8-3.4-3.4 0-6 1.2-7.8 3.4C2.8 6.7 2 9.2 2 12.3s.8 5.6 2.4 7.6C6.2 22.2 8.8 23.4 12.2 23.4c3 0 5.1-.8 6.9-2.6 2.4-2.4 2.3-5.3 1.5-7.1-.5-1.3-1.6-2.3-2.9-2.6zm-5.1 4.8c-1.2.1-2.4-.5-2.5-1.5 0-.8.6-1.7 2.5-1.8h.6c.7 0 1.3.1 1.9.2-.2 2.6-1.5 3-2.5 3.1z"/></svg>'

def sns_icons():
    items = [("Instagram", INSTAGRAM_URL, IC_IG, "ig"), ("TikTok", TIKTOK_URL, IC_TT, "tt"), ("YouTube", YOUTUBE_URL, IC_YT, "yt"), ("Threads", THREADS_URL, IC_TH, "th")]
    return '<div class="sns-icons">' + "".join(f'<a class="sns-ic {c}" href="{u}" target="_blank" rel="noopener" aria-label="公式{n}">{ic}<span>{n}</span></a>' for n,u,ic,c in items if u) + '</div>'

def nlogo(sub=True):
    s = '<span class="nlogo" aria-label="jokeR"><span class="nlogo__word">j<span class="nlogo__chip"></span>ke<span class="R">R</span></span>'
    if sub: s += '<span class="nlogo__sub">AMUSEMENT CASINO</span>'
    return s + '</span>'

def card(rank, suit, w=None):
    red = suit in "♥♦"
    st = f' style="--w:{w}px"' if w else ""
    return f'<span class="pcard{" r" if red else ""}" data-c="{rank}\n{suit}"{st}>{suit}</span>'

def cards(spec, w=None):
    # spec "10♣ J♣ Q♣"
    return '<div class="cards-row">' + "".join(card(t[:-1], t[-1], w) for t in spec.split()) + '</div>'

def band(en, jp, cls=""):
    en_s = "".join(f"<span>{en}</span>" for _ in range(8))
    jp_s = "".join(f"<span>{jp}</span>" for _ in range(16))
    return f'''<div class="band {cls}" aria-hidden="true">
  <div class="band__row jp">{jp_s}</div>
  <div class="band__row">{en_s}</div>
  <div class="band__row jp rev">{jp_s}</div>
  <div class="band__row rev">{en_s}</div>
</div>'''

def layout(path, title, desc, body, top=False, og="img/photo/store-table.jpg"):
    depth = path.count("/")
    P = "../" * depth
    def u(p): return P + p if p else (P or "./")
    navside = "".join(
        f'<li><a href="{u(p)}"{CUR if p==path else ""}>{en}</a></li>' for p,en,jp,s in NAV if s)
    navmenu = "".join(
        f'<li><a href="{u(p)}" style="--i:{i}"><b data-t="{en}">{en}</b><small>{jp}</small></a></li>' for i,(p,en,jp,s) in enumerate(NAV))
    full_title = title if top else f"{title}｜立川 jokeR（ジョーカー）アミューズメントカジノバー"
    loader = '''<div class="loader" aria-hidden="true"><div class="loader__in">
  <p class="loader__txt">SHUFFLING<span>.</span><span>.</span><span>.</span></p>
  <div class="loader__cards"><span class="lcard">A</span><span class="lcard r">♥</span><span class="lcard">♠</span><span class="lcard r">♦</span></div>
</div><button class="loader__skip" type="button">SKIP →</button></div>''' if top else ""
    html = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="{'website' if top else 'article'}">
<meta property="og:site_name" content="立川 jokeR（ジョーカー）">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:image" content="{SITE}/{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@JokerTachikawa">
<meta name="theme-color" content="#1c1c1e">
<link rel="icon" href="{P}img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{P}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bodoni+Moda:opsz,wght@6..96,500;6..96,700&family=Dela+Gothic+One&family=Monoton&family=Yellowtail&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/css/style.css?v={VER}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BarOrPub","name":"立川 jokeR（ジョーカー）","alternateName":"Amusement Bar jokeR","url":"{SITE}/","telephone":"{TEL}","email":"{MAIL}","image":"{SITE}/img/photo/store-table.jpg","address":{{"@type":"PostalAddress","postalCode":"190-0022","addressRegion":"東京都","addressLocality":"立川市","streetAddress":"錦町1-2-13 中島ビル2F","addressCountry":"JP"}},"openingHours":"Mo-Su 17:00-23:00","sameAs":[{",".join('"'+u+'"' for u in [X_URL, INSTAGRAM_URL, TIKTOK_URL, YOUTUBE_URL, THREADS_URL] if u)}]}}</script>
</head>
<body class="{'is-top' if top else 'is-sub'}">
{loader}
<button class="hb" type="button" aria-label="メニュー" aria-expanded="false" aria-controls="menu"><i class="hb__ring"></i><span class="hb__lines"><span></span></span><b class="hb__txt">MENU</b></button>
<nav class="menu" id="menu" aria-label="メニュー">
  <div class="menu__img"><img src="{P}{IMG['room']}" alt="" loading="lazy"></div>
  <div class="menu__body">
    <a href="{u('')}" class="menu__logo">{nlogo()}</a>
    <ul class="menu__list">{navmenu}</ul>
    <div class="menu__sns"><a class="xb" href="{X_URL}" target="_blank" rel="noopener">{IC_X} 公式X</a><a class="lineb" href="{LINE_URL}" target="_blank" rel="noopener">{IC_LINE} 公式LINE</a><a class="xb" href="tel:{TEL}">{IC_TEL} {TEL}</a></div>
    {sns_icons()}
  </div>
</nav>
<nav class="gnav" aria-label="サイト内">
  <a class="gnav__logo" href="{u('')}">{nlogo()}</a>
  <ul>{navside}</ul>
</nav>
<main>
{body.replace("{P}", P)}
</main>
{footer(P, u)}
<a class="totop" href="#" aria-label="ページの先頭へ"><span><i>▲</i>TOP</span></a>
<div class="spcta"><a href="tel:{TEL}">{IC_TEL} 電話する</a><a href="{LINE_URL}" target="_blank" rel="noopener">{IC_LINE} LINE</a></div>
<script src="{P}assets/js/main.js?v={VER}" defer></script>
</body>
</html>
'''
    d = os.path.join(OUT, path)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)

def footer(P, u):
    nav = "".join(f'<a href="{u(p)}">{en}</a>' for p,en,jp,s in NAV)
    marq = "".join('<svg class="mqs" height="1" width="1"><text x="2" y="50%" dominant-baseline="central">jokeR AMUSEMENT CASINO BAR —</text></svg>' for _ in range(4))
    marq_defs = '''<svg class="mq-defs" width="0" height="0" aria-hidden="true" focusable="false"><defs>
<linearGradient id="mqGrad" x1="0" y1="0" x2="1" y2="0" spreadMethod="repeat">
<stop offset="0" stop-color="#ff2bd6"/><stop offset=".25" stop-color="#3ee8ff"/><stop offset=".5" stop-color="#ffd23f"/><stop offset=".75" stop-color="#5dff9d"/><stop offset="1" stop-color="#ff2bd6"/>
<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1 0" dur="5s" repeatCount="indefinite"/>
</linearGradient></defs></svg>'''
    return f'''<footer class="foot">
  <div class="foot__marq" aria-hidden="true">{marq_defs}<div class="band__row">{marq}</div></div>
  <div class="wrap">
    <div class="foot__grid">
      <div>
        <a href="{u('')}">{logo()}</a>
        <p class="foot__info">〒190-0022 東京都立川市錦町1-2-13 中島ビル2F<br>JR「立川駅」南口から徒歩3分<br>TEL <a href="tel:{TEL}">{TEL}</a>　営業時間 17:00〜23:00　定休日 なし</p>
      </div>
      <nav class="foot__nav" aria-label="フッター">{nav}</nav>
      <div>
        <div class="foot__sns"><a class="xb" href="{X_URL}" target="_blank" rel="noopener">{IC_X} 公式X</a><a class="lineb" href="{LINE_URL}" target="_blank" rel="noopener">{IC_LINE} 公式LINE</a></div>
        {sns_icons()}
        <div class="foot__sister">リンク紹介<a href="https://hearts-gekijo.jp/" target="_blank" rel="noopener">HeaRTS劇場 ドン・キホーテ立川店<br><small>エンターテイメントレストラン</small></a></div>
      </div>
    </div>
    <p class="notice foot__no">当店はゲームカジノのため、換金や景品交換は行っておりません。あらかじめご了承ください。</p>
    <p class="foot__copy">© 立川 jokeR（ジョーカー）</p>
  </div>
</footer>'''

def phead(en, jp, img, crumbs, tint="tint-red"):
    cr = '<a href="{P}">HOME</a>' + "".join(f'<span>/</span>{c}' for c in crumbs)
    words = en.split(" ")
    en_html = " ".join(f'<span class="o">{w}</span>' if i % 2 else w for i, w in enumerate(words))
    return f'''<header class="phead">
  <div class="phead__bg stripe {tint}"><img src="{{P}}{IMG[img]}" alt=""></div>
  <div class="phead__shade"></div>
  <div class="phead__in wrap"><h1><span class="phead__en">{en_html}</span><br><span class="phead__jp">{jp}</span></h1></div>
</header>
<div class="wrap crumb">{cr}</div>'''

# ===================================================== TOP
GAME_SVG = {
 "bj": '<svg viewBox="0 0 64 64"><path d="M32 6C24 18 10 24 10 36a11 11 0 0020 5l-4 15h12l-4-15a11 11 0 0020-5C54 24 40 18 32 6z"/></svg>',
 "bac": '<svg viewBox="0 0 64 64"><rect x="8" y="12" width="28" height="40" rx="4" transform="rotate(-10 22 32)"/><rect x="28" y="12" width="28" height="40" rx="4" transform="rotate(10 42 32)"/><path d="M42 26l5 6-5 6-5-6z"/></svg>',
 "poker": '<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="24"/><circle cx="32" cy="32" r="13"/><path d="M32 8v8M32 48v8M8 32h8M48 32h8M15 15l6 6M43 43l6 6M49 15l-6 6M21 43l-6 6"/></svg>',
 "rl": '<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="25"/><circle cx="32" cy="32" r="17"/><circle cx="32" cy="32" r="4"/><path d="M32 15v13M32 36v13M15 32h13M36 32h13M20 20l9 9M35 35l9 9M44 20l-9 9M29 35l-9 9"/><circle cx="44" cy="14" r="3"/></svg>',
}

def top():
    pickups = [
      ("system/#student","STUDENT","期間限定　学割（22歳以下）","平日19時まで。2,000円で10,000 Point＋ワンドリンク付き。", '<div class="pk__art" style="--nc:#ffd23f"><b>学割</b><span>WEEKDAY ～19:00 / UNDER 22</span></div>', "#ffd23f"),
      ("system/#ladies","LADIES","女性限定　飲み放題付きプラン","2,000円で10,000 Point＋飲み放題。女性ひとりでも気軽に。", '<div class="pk__art" style="--nc:#ff4fd8"><b>女性限定</b><span>CHIPS + FREE DRINK</span></div>', "#ff4fd8"),
      ("#party","PARTY","お誕生日・二次会・貸切","お祝い事のお手伝い、各種貸切パーティーも承ります。", f'<img src="{{P}}{IMG["cake"]}" alt="お誕生日のデザートプレート" loading="lazy">', "#3ee8ff"),
      ("menu/","BAR","バーカウンターのみもOK","ゲームをしない方も、1時間1,000円＋ワンドリンク制でご利用いただけます。", f'<img src="{{P}}{IMG["shelf"]}" alt="バーのボトル棚" loading="lazy">', "#ff7a2e"),
      ("recruit/","RECRUIT","ディーラー・スタッフ募集","未経験OK。資格を持った講師が基本から教えます。", f'<img src="{{P}}{IMG["dealer"]}" alt="" loading="lazy">', "#5dff9d"),
    ]
    pk_html = "".join(f'''<a class="pk" href="{{P}}{h}" style="--nc:{nc}"><div class="pk__img">{art}<span class="pk__no">0{i+1}</span></div><div class="pk__body"><p class="pk__cat">{cat}</p><p class="pk__ttl">{t}</p><p class="pk__txt">{d}</p><span class="pk__go">MORE <i>→</i></span></div></a>''' for i,(h,cat,t,d,art,nc) in enumerate(pickups))
    bokeh = "".join(f'<i style="--x:{(i*37)%100}%;--y:{(i*53)%100}%;--s:{8+(i*7)%26}px;--d:{6+(i*3)%9}s;--dl:-{(i*1.3)%8:.1f}s;--c:{["#ff2bd6","#3ee8ff","#ffd23f","#5dff9d","#ff4f4f"][i%5]}"></i>' for i in range(12))

    games_sel = "".join(f'''<a class="game" href="{h}" data-reveal data-delay="{i*0.1:.1f}"><span class="game__en">{en}</span><span class="game__ring">{GAME_SVG[k]}</span><span class="game__jp">・{jp}・</span></a>''' for i,(k,en,jp,h) in enumerate([
        ("bj","BLACKJACK","ブラックジャック","#g-bj"),("bac","BACCARAT","バカラ","#g-bac"),("poker","POKER","ポーカー","#g-poker"),("rl","ROULETTE","ルーレット","#g-rl")]))

    def gsec(id_, cls, en, jp, img, txt, link, tall=False, wipe="#fff"):
        btn = f'<a class="btn{" w" if cls=="c-gold" else ""}" href="{{P}}{link}">ルールを見る</a>' if link else '<a class="btn" href="{P}system/">料金システムへ</a>'
        return f'''<section class="gsec {cls}" id="{id_}">
  {band(en, jp)}
  <figure class="gsec__photo{" tall" if tall else ""} wipe stripe" style="--wipe:{wipe}"><img src="{{P}}{IMG[img]}" alt="{jp}" loading="lazy"></figure>
  <div class="gsec__body">
    <h3 class="gsec__name" data-reveal="left">{en}<small>{jp}</small></h3>
    <div class="gsec__txt" data-reveal="right"><p>{txt}</p>{btn}</div>
  </div>
</section>'''

    body = f'''
<section class="hero" aria-label="メインビジュアル">
  <div class="hero__media">
    <div class="hero__slide is-on"><video class="hero__video" muted loop playsinline autoplay preload="auto" poster="{{P}}{IMG['table']}" data-wide="{{P}}img/video/hero-wide.mp4" data-tall="{{P}}img/video/hero-tall.mp4" aria-hidden="true"></video></div>
    <div class="hero__slide"><picture><source media="(max-width:767px) and (orientation:portrait)" srcset="{{P}}img/photo/hero-2-tall.jpg"><img src="{{P}}img/photo/hero-2-wide.jpg" alt="テーブルに置かれたエースのカードとチップ" decoding="async" style="object-position:30% 60%"></picture></div>
    <div class="hero__slide"><picture><source media="(max-width:767px) and (orientation:portrait)" srcset="{{P}}img/photo/hero-3-tall.jpg"><img src="{{P}}img/photo/hero-3-wide.jpg" alt="ネオンに照らされたバーのボトル棚" decoding="async"></picture></div>
  </div>
  <div class="hero__shade"></div>
  <div class="fx" aria-hidden="true">
    <span class="beam b1"></span><span class="beam b2"></span><span class="beam b3"></span><span class="beam b4"></span>
    <span class="laser l1"></span><span class="laser l2"></span><span class="laser l3"></span>
    <div class="bokeh">{bokeh}</div>
    <span class="scan"></span><span class="strobe"></span>
  </div>
  <div class="hero__dots"></div>
  <div class="hero__copy">
    <p class="hero__night" aria-hidden="true">CASINO NIGHT</p>
    <h1 class="hero__title"><span class="nj">立川で、<br class="sp">カジノ遊び。</span></h1>
    <p class="hero__tag"><span>はじめてでも、ルールを忘れても大丈夫！</span></p>
    <p class="hero__sub">立川駅南口 徒歩3分 ／ AMUSEMENT CASINO BAR jokeR</p>
  </div>
  <a class="hero__first" href="#games"><span><b>FIRST TIME?</b><small>はじめての方へ</small></span><i>›</i></a>
  <span class="scroll-cue">SCROLL</span>
</section>

<div class="club">
  <div class="club__lights" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <div class="club__spot" aria-hidden="true"></div>

<section class="brand">
  <div class="brand__ghost" aria-hidden="true">AMUSEMENT<br>CASINO BAR<br>TACHIKAWA</div>
  <div class="brand__sign" data-reveal="zoom">{nlogo()}</div>
  <p class="brand__lead" data-reveal><span class="s1">♠</span> ブラックジャック <span class="s2">♥</span> バカラ <span class="s3">♦</span> ポーカー <span class="s4">♣</span> ルーレット</p>
</section>

<section class="sec intro">
  <span class="vword o l" aria-hidden="true">PLAY</span>
  <span class="vword o rr" aria-hidden="true">JOKER</span>
  <span class="float chip" data-px=".22" data-rot="-12" style="--s:110px;left:6%;top:8%"></span>
  <span class="float chip k" data-px=".35" data-rot="20" style="--s:70px;right:12%;top:4%"></span>
  <span class="float pcard" data-px=".18" data-rot="14" data-c="A\n♠" style="--w:86px;right:5%;bottom:10%">♠</span>
  <span class="float chip g" data-px=".28" data-rot="0" style="--s:60px;left:44%;bottom:4%"></span>
  <div class="wrap intro__grid">
    <div>
      <p class="kicker" data-reveal>WELCOME TO jokeR</p>
      <h2 class="ttl intro__h"><span class="pop-in">立川でのカジノ遊びは</span><br><span class="pop-in"><span class="nr">jokeR</span>で！</span></h2>
      <div class="lead" data-reveal>
        <p>立川jokeRは、ディーラー講師の資格を持ったディーラーが在籍するアミューズメント・カジノバーです。</p>
        <p><a href="{{P}}casino-games/black-jack/" class="ul">ブラックジャック</a>をはじめ、<a href="{{P}}casino-games/baccarat/" class="ul">バカラ</a>や<a href="{{P}}casino-games/texas-holdem/" class="ul">ポーカー（テキサス・ホールデム）</a>などのカードゲーム、さらにルーレットでのご遊戯も堪能していただけます。</p>
        <p>在籍ディーラーが基本から丁寧に解説いたしますので、初心者の方でもルールを忘れてしまった方でも大丈夫！カジノ初心者の方でも気軽に遊べます。</p>
        <p>立川駅南口からわずか徒歩3分と好アクセスですので、気軽に足をお運びください。</p>
      </div>
      <div class="btns" style="justify-content:flex-start" data-reveal><a class="btn nbtn" href="{{P}}system/">料金システム</a></div>
    </div>
    <figure class="intro__photo nframe" data-reveal="right"><div class="wipe" style="--wipe:#ff2bd6"><img class="ph" src="{{P}}{IMG['lounge']}" alt="jokeRの店内でディーラーがゲームを進める様子"></div><figcaption>jokeR の店内</figcaption></figure>
  </div>
</section>

<section class="sec pickup" id="pickup">
  <div class="wrap">
    <div class="ntitle" data-reveal><b>PICK UP</b><small>おすすめプラン・ご案内</small></div>
    <div class="slider" data-reveal>
      <button class="slider__arrow prev" type="button" aria-label="前へ">‹</button>
      <div class="slider__track">{pk_html}</div>
      <button class="slider__arrow next" type="button" aria-label="次へ">›</button>
      <div class="slider__dots"></div>
    </div>
  </div>
</section>

<section class="sec" id="news" style="padding-top:20px">
  <div class="wrap">
    <div class="ntitle c" data-reveal><b>NEWS</b><small>お知らせ・大会情報</small></div>
    <div class="news__grid">
      <div class="news__box nbox" style="--nc:#3ee8ff" data-reveal="left">
        <h3>{IC_X} @JokerTachikawa<span class="live">LIVE</span></h3>
        <div class="news__x">
          <a class="twitter-timeline" data-height="480" data-theme="dark" data-chrome="noheader nofooter transparent" href="https://twitter.com/JokerTachikawa?ref_src=twsrc%5Etfw">Tweets by JokerTachikawa</a>
          <p class="note" style="margin-top:12px">最新の大会告知・営業情報は公式Xで発信しています。表示されない場合は<a href="{X_URL}" target="_blank" rel="noopener" class="ul">こちら</a>から。</p>
        </div>
      </div>
      <div class="news__box nbox news__line" style="--nc:#06e36a" data-reveal="right">
        <h3>{IC_LINE} OFFICIAL LINE</h3>
        <p class="big">ご予約・貸切のご相談は<br><span class="ng">公式LINE</span>からもOK！</p>
        <p class="note">友だち追加で、イベントや大会のお知らせが届きます。</p>
        <a class="lineb" href="{LINE_URL}" target="_blank" rel="noopener">{IC_LINE} 友だち追加する</a>
        <a class="xb" href="tel:{TEL}">{IC_TEL} {TEL}</a>
        <figure class="news__img" style="margin:6px 0 0"><img src="{{P}}{IMG['cocktail2']}" alt="" loading="lazy"></figure>
      </div>
    </div>
  </div>
</section>
</div>

<section class="sec" id="games">
  <div class="wrap">
    <div class="select__frame" data-reveal>
      <span class="neon">- Select -</span>
      <div class="select__head">
        <h2 class="pop select__h"><span class="pop-in"><span class="g">今日</span>は</span><br><span class="pop-in"><span class="p">どのゲーム</span>で</span><br><span class="pop-in">遊ぶ<span class="y">？</span></span></h2>
        <div class="select__txt"><p>ブラックジャック、バカラ、ポーカー（テキサス・ホールデム）、ルーレット。在籍ディーラーが基本から丁寧に解説するので、はじめての方も安心です。</p><span class="note">※当店はゲームカジノのため、換金や景品交換は行っておりません。</span></div>
      </div>
      <div class="games">{games_sel}</div>
    </div>
  </div>
</section>

{gsec("g-bj","c-red","BLACKJACK","ブラックジャック","bjreal","ディーラーとプレイヤー（自分）が対戦するゲーム。ルールは簡単、2枚以上のカードの合計が「21」に近いほうが勝ち。ただし「22」以上になったら即負け！","casino-games/black-jack/", tall=True, wipe="#111")}
{gsec("g-bac","c-gold","BACCARAT","バカラ","baccarat","「バンカー」と「プレイヤー」の仮想の二人の勝負で、どちらが勝つかを予想して賭けるゲーム。2〜3枚のカードの合計点数の下一桁が、9に近い方が勝ちです。","casino-games/baccarat/", tall=True, wipe="#111")}
{gsec("g-poker","c-green","POKER","テキサス・ホールデム","poker","ポーカーの一種。各プレイヤーに配られる2枚の手札と、全員共通の「コミュニティ・カード」を組み合わせて役をつくり勝負します。毎週の大会も開催中！","casino-games/texas-holdem/", wipe="#111")}
<section class="gsec c-dark" id="g-rl">
  {band("ROULETTE","ルーレット")}
  <figure class="gsec__photo wipe stripe tint-red" style="--wipe:var(--red)"><img src="{{P}}{IMG['store']}" alt="jokeR店内のルーレット台" loading="lazy"></figure>
  <div class="gsec__body">
    <h3 class="gsec__name" data-reveal="left">ROULETTE<small>ルーレット</small></h3>
    <div class="gsec__txt" data-reveal="right"><p>店内にはルーレット台もご用意。カードゲームの合間に、みんなでワイワイ盛り上がれます。</p><a class="btn" href="{{P}}casino-games/">ゲーム解説一覧</a></div>
  </div>
</section>

<section class="sec" id="system">
  <div class="wrap">
    <div class="sec-title" data-reveal><b>SYSTEM</b><small>料金システム</small></div>
    <div class="price-grid">
      <div class="ptable" data-reveal><div class="ptable__head"><h3>新規購入料金</h3></div>
        <table><tr><th>¥3,000</th><td class="pt">10,000<small>Point</small></td></tr><tr><th>¥5,500</th><td class="pt">20,000<small>Point</small></td></tr><tr><th>¥10,000</th><td class="pt">40,000<small>Point</small></td></tr></table></div>
      <div class="ptable dark" data-reveal data-delay=".1"><div class="ptable__head"><h3>引き出し料金</h3></div>
        <table><tr><th>初回引き出し<br>¥2,500</th><td class="pt">20,000<small>Point以下</small></td></tr><tr><th>2回目以降引き出し<br>¥1,500</th><td class="pt">20,000<small>Point以下</small></td></tr></table></div>
    </div>
    <div class="btns" data-reveal><a class="btn" href="{{P}}system/">学割・女性限定プランも見る</a></div>
  </div>
</section>

<section class="sec" id="food" style="padding-top:20px">
  <div class="wrap">
    <div class="sec-title" data-reveal><b>FOOD &amp; DRINK</b><small>フード・ドリンク</small></div>
    <div class="fd__grid">
      <figure class="fd__a wipe" style="--wipe:var(--gold)"><img src="{{P}}{IMG['highball']}" alt="ハイボール" loading="lazy"><figcaption>HIGHBALL</figcaption></figure>
      <figure class="fd__b wipe"><img src="{{P}}{IMG['pasta']}" alt="パスタ" loading="lazy"><figcaption>FOOD</figcaption></figure>
      <figure class="fd__c wipe"><img src="{{P}}{IMG['ham']}" alt="生ハムとサラミ" loading="lazy"></figure>
      <figure class="fd__d wipe"><img src="{{P}}{IMG['glasses']}" alt="カクテルとワイン" loading="lazy"><figcaption>DRINK</figcaption></figure>
      <figure class="fd__e wipe"><img src="{{P}}{IMG['whisky']}" alt="ウイスキーのボトル" loading="lazy"><figcaption>WHISKY</figcaption></figure>
    </div>
    <div class="fd__info">
      <div class="fd__card" data-reveal><h3>FREE FOOD<small>日替わり</small></h3><p class="big">日替わりで当店自慢の<em>無料フード</em>をご用意。</p><p class="note">メニューはご来店いただいてからのお楽しみです。</p></div>
      <div class="fd__card" data-reveal data-delay=".1"><h3>ALL YOU CAN DRINK<small>飲み放題2h</small></h3><p class="big">アルコール <em>2,500円</em>／ソフトドリンク <em>2,000円</em></p><p class="note">カジノゲームをされない方も、バーカウンターのみのご利用が可能です（1時間1,000円＋ワンドリンク制）。</p></div>
    </div>
    <div class="btns" data-reveal><a class="btn" href="{{P}}menu/">メニューを見る</a></div>
  </div>
</section>

<section class="sec" id="party" style="padding-top:30px">
  <div class="wrap party">
    <div class="party__imgs" data-reveal="left">
      <figure><img src="{{P}}{IMG['cake']}" alt="お誕生日のデザートプレート" loading="lazy"></figure>
      <figure><img src="{{P}}{IMG['wine']}" alt="ワイン" loading="lazy"></figure>
      <figure><img src="{{P}}{IMG['bottles']}" alt="ボトルとグラス" loading="lazy"></figure>
    </div>
    <div data-reveal="right">
      <span class="neon g" style="text-align:left;transform:rotate(-4deg)">Special Service</span>
      <h2 class="pop party__h">お祝い事も、<br>二次会の貸切も。</h2>
      <p>お誕生日などのお祝い事、当店がお手伝いいたします！二次会などの各種貸切パーティーも受け付けております。</p>
      <p class="note" style="margin-top:10px">費用などのご相談・ご予約は、必ず前日までにお問い合わせください。</p>
      <div class="btns" style="justify-content:flex-start"><a class="btn" href="{{P}}contact/">貸切・予約の相談</a></div>
    </div>
  </div>
</section>

<section class="rband" id="recruit">
  <div class="rband__bg stripe tint-dark"><img src="{{P}}{IMG['rband']}" alt="jokeRのディーラー" data-px=".12" loading="lazy" style="object-position:50% 30%"></div>
  <div class="wrap rband__in">
    <span class="neon" style="text-align:left">Join us!</span>
    <h2 class="pop rband__h" data-reveal><span>ディーラー、</span><br><span>はじめませんか？</span></h2>
    <p class="rband__txt" data-reveal>未経験OK！資格を持った当店講師が丁寧に教えます。<br>ディーラー・ホールスタッフ・キッチン募集中。</p>
    <div class="btns" style="justify-content:flex-start" data-reveal><a class="btn w" href="{{P}}recruit/">募集要項を見る</a></div>
  </div>
</section>

<section class="sec" id="access">
  <div class="wrap">
    <div class="sec-title" data-reveal><b>ACCESS</b><small>アクセス・店舗情報</small></div>
    {access_block()}
  </div>
</section>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
'''
    layout("", "立川のアミューズメントカジノバー jokeR（ジョーカー）｜立川駅南口 徒歩3分",
           "立川駅南口徒歩3分のアミューズメントカジノバー jokeR（ジョーカー）。ブラックジャック・バカラ・ポーカー（テキサス・ホールデム）・ルーレットを、資格を持ったディーラーが基本から丁寧に解説。初心者の方も気軽に遊べます。",
           body, top=True)

def access_block():
    return f'''<div class="access">
      <div class="map" data-reveal="left"><iframe src="{MAP_EMBED}" loading="lazy" title="jokeRの地図" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
      <div data-reveal="right">
        <table class="info">
          <tr><th>店舗名</th><td>立川 jokeR（ジョーカー）</td></tr>
          <tr><th>所在地</th><td>〒190-0022<br>東京都立川市錦町1-2-13 中島ビル2F</td></tr>
          <tr><th>アクセス</th><td>JR「立川駅」南口から徒歩3分</td></tr>
          <tr><th>電話番号</th><td><a href="tel:{TEL}">{TEL}</a></td></tr>
          <tr><th>メール</th><td><a href="mailto:{MAIL}">{MAIL}</a></td></tr>
          <tr><th>営業時間</th><td>17:00〜23:00</td></tr>
          <tr><th>定休日</th><td>なし</td></tr>
        </table>
        <div class="btns" style="justify-content:flex-start;margin-top:26px"><a class="btn-line" href="{MAP_LINK}" target="_blank" rel="noopener"><span>GOOGLE MAP<small>大きな地図で見る</small></span></a></div>
      </div>
    </div>'''

# ===================================================== SYSTEM
def system():
    body = phead("SYSTEM", "料金システム", "chips", ["SYSTEM"]) + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap">
    <div class="block">
      <h2 class="h2" data-reveal>料金システム <small>PRICE</small></h2>
      <div class="price-grid">
        <div class="ptable" data-reveal><div class="ptable__head"><h3>新規購入料金</h3></div>
          <table><tr><th>料金</th><th>チップ</th></tr><tr><td class="yen">¥3,000</td><td class="pt">10,000<small>Point</small></td></tr><tr><td class="yen">¥5,500</td><td class="pt">20,000<small>Point</small></td></tr><tr><td class="yen">¥10,000</td><td class="pt">40,000<small>Point</small></td></tr></table></div>
        <div class="ptable dark" data-reveal data-delay=".1"><div class="ptable__head"><h3>引き出し料金</h3></div>
          <table><tr><th>料金</th><th>チップ</th></tr><tr><td class="yen" style="font-size:22px">初回引き出し<br>¥2,500</td><td class="pt">20,000<small>Point以下</small></td></tr><tr><td class="yen" style="font-size:22px">2回目以降引き出し<br>¥1,500</td><td class="pt">20,000<small>Point以下</small></td></tr></table></div>
        <div class="ptable gold" id="student" data-reveal><div class="ptable__head"><h3>期間限定　学割</h3><small>平日19時まで・22歳以下</small></div>
          <table><tr><th>料金</th><th>チップ</th></tr><tr><td class="yen">¥2,000</td><td class="pt">10,000<small>Point</small><br><span class="tag">ワンドリンク付</span></td></tr><tr><td class="yen">¥3,000</td><td class="pt">20,000<small>Point</small><br><span class="tag">ワンドリンク付</span></td></tr><tr><td class="yen" style="font-size:22px">初回引き出し<br>¥2,500</td><td class="pt">20,000<small>Point以下</small><br><span class="tag">ワンドリンク付</span></td></tr></table></div>
        <div class="ptable pink" id="ladies" data-reveal data-delay=".1"><div class="ptable__head"><h3>女性限定</h3><small>LADIES</small></div>
          <table><tr><th>料金</th><th>チップ</th></tr><tr><td class="yen">¥2,000</td><td class="pt">10,000<small>Point</small><br><span class="tag">飲み放題付</span></td></tr><tr><td class="yen">¥3,000</td><td class="pt">20,000<small>Point</small><br><span class="tag">飲み放題付</span></td></tr><tr><td class="yen" style="font-size:22px">初回引き出し<br>¥2,500</td><td class="pt">20,000<small>Point以下</small><br><span class="tag">ワンドリンク付</span></td></tr></table></div>
      </div>
    </div>

    <div class="block" id="bar">
      <h2 class="h2" data-reveal>ご飲食のみご利用の場合 <small>BAR COUNTER</small></h2>
      <div class="party" style="align-items:start">
        <figure class="wipe stripe tint-red" style="margin:0;--wipe:var(--red)"><img src="{{P}}{IMG['bar']}" alt="バーカウンター" loading="lazy"></figure>
        <div data-reveal>
          <p class="pop" style="font-size:clamp(22px,2.6vw,30px)">バーカウンターのみの<br>ご利用もOK！</p>
          <p style="margin-top:14px">カジノゲームでのご遊戯をされない方も、バーカウンターのみのご利用が可能です。</p>
          <p class="mall-price" style="margin:12px 0">1時間 ¥1,000 ＋ ワンドリンク制</p>
          <p>当店でしか味わえないこだわりの食材を使った料理や、定番からとっておきのお酒まで豊富にご用意しています。</p>
          <div class="btns" style="justify-content:flex-start;margin-top:24px"><a class="btn-line" href="{{P}}menu/"><span>MENU<small>フード・ドリンクメニュー</small></span></a></div>
        </div>
      </div>
    </div>

    <div class="block">
      <h2 class="h2" data-reveal>利用規約 <small>TERMS</small></h2>
      <div class="box" data-reveal>
        <h3 class="h3" style="margin-top:0">禁止事項</h3>
        <ul class="list-x">
          <li>チップの共有</li><li>チップの持ち出し</li><li>チップを商品と交換、換金などは一切行いません</li>
          <li>他のお客様、スタッフに迷惑となる行為、暴言などは即時退店していただきます</li><li>店内で仮眠をとる</li>
          <li>ディーラーに触れるすべての行為</li><li>ディーラーに電話番号、LINE、メールアドレスなどの連絡先を聞く行為また教える行為</li>
          <li>女性スタッフの撮影</li><li>店外でのデート等の誘い</li><li>ひわいな会話</li><li>女性スタッフへのプレゼント</li><li>ストーカー行為、店前や駅前での待ち伏せ</li>
        </ul>
        <p class="note" style="margin-top:14px">上記の行為が発覚した場合、即時退店または次回以降のご来店をお断りする場合がございます。</p>
        <h3 class="h3">注意事項</h3>
        <ul class="list-dot"><li>お水、タバコの提供は致しません。</li><li>一時ご退店で外出される際は、その時点でのお会計を一度精算していただきます。</li><li>飲食物の持ち込みはご遠慮ください。</li></ul>
      </div>
      <p class="notice" style="margin-top:24px">当店はゲームカジノのため、換金や景品交換は行っておりません。あらかじめご了承ください。</p>
    </div>
  </div>
</section>'''
    layout("system/", "料金システム", "立川 jokeR の料金システム。新規購入料金・引き出し料金・学割（平日19時まで／22歳以下）・女性限定プラン、バーカウンターのみのご利用、利用規約のご案内。", body)

# ===================================================== MENU
def menu():
    def rows(items): return "".join(f'<div class="mrow"><b>{n}</b><em>{p}</em></div>' for n,p in items)
    def cat(en, jp, inner, cap=""):
        return f'<div class="mcat" data-reveal><h3>{en}<small>{jp}</small></h3>{f"<p class=cap>{cap}</p>" if cap else ""}{inner}</div>'
    def allp(price, names): return f'<p class="mall-price">ALL {price}</p><div class="mall">' + "".join(f"<span>{n}</span>" for n in names) + "</div>"
    drink = "".join([
      cat("HIGHBALL / WHISKY","ハイボール／ウイスキー", rows([("ジムビーム・ハイボール","800円"),("角ハイボール","800円"),("サントリーワールドウイスキー碧Ao","1,000円"),("JACK DANIEL’S","900円"),("富士山麓","1,000円"),("NIKKA session","1,000円"),("白州","1,500円"),("響 JAPANESE HARMONY","1,500円"),("竹鶴","1,500円"),("I.W.HARPER","1,500円"),("白州12年","4,500円")])),
      cat("BEER","ビール", rows([("ザ・プレミアム・モルツ","800円"),("コロナビール","800円")]) + '<p class="cap" style="margin-top:10px">ビアカクテル</p>' + rows([("シャンディガフ","800円"),("カシスビア","800円"),("カンパリビア","800円")]) + '<p class="cap" style="margin-top:10px">ノンアルコールビールテイスト飲料</p>' + rows([("ノンアルコールビール","700円")])),
      cat("SOUR","サワー", rows([("レモンサワー","800円"),("ゆずサワー","800円"),("アセロラサワー","800円"),("ウーロンハイ","800円"),("緑茶ハイ","800円"),("ジャスミン茶ハイ","800円"),("紅茶ハイ","800円")])),
      cat("PLUM WINE","梅酒", rows([("梅酒","800円")]), "※ロック・ソーダ割からお選びください。"),
      cat("SHOCHU","焼酎", rows([("いいちこ（麦）","800円"),("吉四六（麦）","800円"),("百年の孤独（麦）","1,200円"),("黒霧島（芋）","800円"),("富乃宝山（芋）","900円"),("鍛高譚（紫蘇）","800円")]), "※ロック・水割・お湯割からお選びください。"),
      cat("WINE","ワイン", rows([("グラスワイン（赤・白）","ALL 800円"),("ボトルワイン","ASK"),("シャンパン","ASK")])),
      cat("COCKTAIL","カクテル", allp("800円", ["ジンバック","ジンライム","ウォッカトニック","モスコミュール","スクリュードライバー","ラムトニック","ラムコーラ","カシスソーダ","カシスオレンジ","カシスグレープフルーツ","カシスウーロン","マリブコーラ","マリブオレンジ","マリブミルク","アマレットジンジャー","アマレットミルク","カルーアミルク"])),
      cat("SHOT","ショット", rows([("テキーラ","1,000円"),("イエーガーマイスター","1,000円")])),
      cat("SOFT DRINK","ソフトドリンク", allp("600円", ["ウーロン茶","緑茶","ジャスミン茶","コーラ","ジンジャーエール","オレンジジュース","グレープフルーツジュース","リンゴジュース","アセロラジュース","コーヒー","紅茶","ミルクティー"])),
    ])
    body = phead("FOOD DRINK", "フード・ドリンク", "shelf", ["MENU"], "tint-gold") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap">
    <div class="block">
      <h2 class="h2" data-reveal>FOOD MENU <small>フード</small></h2>
      <div class="fd__grid" style="margin-bottom:34px">
        <figure class="fd__a wipe"><img src="{{P}}{IMG['pasta']}" alt="パスタ" loading="lazy"></figure>
        <figure class="fd__b wipe"><img src="{{P}}{IMG['pizza']}" alt="ピザ" loading="lazy"></figure>
        <figure class="fd__c wipe"><img src="{{P}}{IMG['sausage']}" alt="ソーセージ" loading="lazy"></figure>
        <figure class="fd__d wipe"><img src="{{P}}{IMG['cheese']}" alt="チーズの盛り合わせ" loading="lazy"></figure>
        <figure class="fd__e wipe"><img src="{{P}}{IMG['veg']}" alt="野菜スティック" loading="lazy"></figure>
      </div>
      <div class="fd__info" style="margin-top:0">
        <div class="fd__card" data-reveal><h3>MAIN<small>メイン</small></h3><p class="big">日替わりで当店自慢の<em>無料フード</em>をご用意しております。</p><p class="note">メニューはご来店いただいてからのお楽しみです。一部のメニューはXでもご紹介している場合がございます。</p></div>
        <div class="fd__card" data-reveal data-delay=".1"><h3>FRIED FOOD<small>揚げ物</small></h3><div class="mrow" style="margin-top:10px"><b>からあげ</b><em>500円</em></div></div>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>DRINK MENU <small>ドリンク</small></h2>
      <div class="ptable gold" data-reveal style="max-width:560px;margin-bottom:40px"><div class="ptable__head"><h3>飲み放題プラン 2h</h3></div>
        <table><tr><th>アルコール</th><td class="yen">¥2,500</td></tr><tr><th>ソフトドリンク</th><td class="yen">¥2,000</td></tr></table></div>
      <div class="mcols">{drink}</div>
      <p class="note" style="margin-top:10px">＜表示価格は全て税込＞</p>
    </div>
  </div>
</section>'''
    layout("menu/", "フード・ドリンクメニュー", "立川 jokeR のフード・ドリンクメニュー。日替わりの無料フード、からあげ、飲み放題プラン（2h）、ハイボール・ウイスキー・ビール・サワー・焼酎・ワイン・カクテルなど。", body, og="img/photo/drink-whisky.jpg")

# ===================================================== GAMES
GSUB = [("casino-games/","ゲーム解説一覧"),("casino-games/black-jack/","ブラックジャック"),("casino-games/baccarat/","バカラ"),("casino-games/texas-holdem/","テキサス・ホールデム")]
def subnav(cur):
    return '<nav class="subnav" aria-label="ゲーム解説">' + "".join(f'<a href="{{P}}{p}"{CUR if p==cur else ""}>{t}</a>' for p,t in GSUB) + '</nav>'

def games():
    ov = [("black-jack","BLACKJACK","ブラックジャック","blackjack","ブラックジャックは、カジノディーラー（以下ディーラー）とプレイヤー（自分）が対戦する形式のゲームです。ルールは簡単。2枚以上のトランプのカードの合計が「21」に近いほうが勝ち。最初にプレイヤー、ディーラーともに2枚のカードが配られ、その2枚を「21」に近づけるためにカードを追加したり、最初に配られた2枚のカードでディーラーと勝負します。ただし、合計が「22」以上になると即負け（ゲーム終了）となるので、「22」以上にならないように気をつけながら「21」に近づけていく必要があります。"),
          ("baccarat","BACCARAT","バカラ","baccarat","バカラとは、「バンカー」と「プレイヤー」の、仮想の二人による勝負で、どちらが勝つかを客が予想して賭けるゲームです。実際にゲームをプレイしているのは仮想の人物であるため、お客さんはどちらが勝つかを予想するだけになります。2枚もしくは3枚のカードの合計点数の下一桁の数字が、9に近い方が勝ちです。"),
          ("texas-holdem","TEXAS HOLD’EM","テキサス・ホールデム","poker","テキサス・ホールデムはポーカーの一種。各プレイヤーごとに配られる2枚の手札と、コミュニティ・カードと呼ばれる全プレイヤー共通のカードを組み合わせて役をつくり勝負します。")]
    cards_html = "".join(f'''<a class="ov" href="{{P}}casino-games/{s}/" data-reveal data-delay="{i*0.1:.1f}"><div class="ov__img stripe"><img src="{{P}}{IMG[img]}" alt="{jp}" loading="lazy"></div><div class="ov__body"><p class="ov__en">{en}</p><p class="ov__jp">{jp}</p><p>{t}</p><span class="ov__more">{jp}の解説 <span>›</span></span></div></a>''' for i,(s,en,jp,img,t) in enumerate(ov))
    body = phead("CASINO GAMES", "ゲーム解説", "hands", ["CASINO GAMES"], "tint-green") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap">
    <h2 class="h2" data-reveal>ゲーム解説 <small>HOW TO PLAY</small></h2>
    <div class="overview">{cards_html}</div>
    <div class="box" style="margin-top:30px" data-reveal><p class="pop" style="font-size:20px">ルーレットもあります！</p><p style="margin-top:8px">店内ではルーレットでのご遊戯もお楽しみいただけます。遊び方はディーラーにお気軽にお尋ねください。</p></div>
    <p class="notice" style="margin-top:24px">当店はゲームカジノのため、換金や景品交換は行っておりません。</p>
    {subnav("casino-games/")}
  </div>
</section>'''
    layout("casino-games/", "ゲーム解説（ブラックジャック・バカラ・ポーカー）", "立川 jokeR で遊べるカジノゲームの解説。ブラックジャック、バカラ、ポーカー（テキサス・ホールデム）のルールをわかりやすくご紹介します。", body)

def blackjack():
    body = phead("BLACK JACK", "ブラックジャック", "blackjack", ['<a href="{P}casino-games/">CASINO GAMES</a>', "BLACK JACK"]) + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap-s">
    <div class="block">
      <h2 class="h2" data-reveal>ブラックジャックのルール <small>RULES</small></h2>
      <div class="lead" data-reveal>
        <p>ブラックジャックは、カジノディーラー（以下ディーラー）とプレイヤー（自分）が対戦する形式のゲームです。</p>
        <p class="pop" style="font-size:clamp(20px,2.4vw,26px)">ルールは簡単。2枚以上のカードの合計が<span class="y">「21」</span>に近いほうが勝ち。</p>
        <p>最初にプレイヤー、ディーラーともに2枚のカードが配られ、その2枚を「21」に近づけるためにカードを追加したり、もしくは、最初に配られた2枚のカードでディーラーと勝負します。</p>
        <p>ただし、合計が「22」以上になると即負け（ゲーム終了）となるので、カードを追加する時は、「22」以上にならないように気をつけながら「21」に近づけていく必要があります。</p>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>カードの数え方 <small>COUNT</small></h2>
      <p data-reveal>ブラックジャックでは、通常のトランプカードの数え方と少しだけ違いますが簡単です。</p>
      <div class="rule-grid" style="margin-top:20px">
        <div class="rule" data-reveal><h4>2〜10</h4>{cards("2♠ 5♥ 10♣", 46)}<p>トランプの数字と同じ数で数えます。「2」であれば「2」、「5」であれば「5」、「10」であれば「10」と数えます。</p></div>
        <div class="rule" data-reveal data-delay=".1"><h4>J・Q・K ＝ 10</h4>{cards("J♣ Q♥ K♠", 46)}<p>J(11)、Q(12)、K(13)の絵札は、トランプの数字でなくすべて「10」で数えます。この点は普通のトランプと違いますので覚えましょう。</p></div>
        <div class="rule" data-reveal data-delay=".2"><h4>A ＝ 1 or 11</h4>{cards("A♠ A♦", 46)}<p>A（エース）は特別なカード。手持ちのカードの状況を見て、「1」と数えるか「11」と数えるかをプレイヤーが決められる便利なカードです。</p></div>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>ブラックジャックの特殊なルール <small>OPTION</small></h2>
      <p data-reveal>ブラックジャックにはさまざまなオプションルールがあります。</p>
      <div class="box" style="margin-top:18px" data-reveal>
        <h3 class="h3" style="margin-top:0">インシュランス</h3>
        <p>ディーラーのアップカード（表になっているカード）が「A」の場合、ゲストに対して「インシュランス？」と聞きます。ディーラーのホールカード（伏せられているカード）が「10（J/Q/K）」の場合はブラックジャックが成立するので、ゲストは保険（インシュランス）をかけることができます。</p>
        <ul class="list-dot" style="margin:8px 0"><li>ディーラーがブラックジャックの場合は、その時点でゲストの負けになります。</li><li>ゲストもブラックジャックの場合は引き分けになります。</li></ul>
        <p>インシュランスをしたいゲストがいた場合は、ベット金額の半分までインシュランスのベットができます。ディーラーがブラックジャック成立の場合、インシュランスベットに対して3倍の配当を付けます。ディーラーがブラックジャックではなかった場合はインシュランスベットを引いて通常のゲーム進行となります。「ノージャック」のコールがあります。</p>
        <h3 class="h3">イーブンマネー</h3>
        <p>ゲストのカードがブラックジャック成立していて、ディーラーのアップカードが「A」の場合のインシュランスのことを「イーブンマネー」といいます。この場合はゲストから「イーブンマネー」というコールをしてもらいます。</p>
        <p style="margin-top:8px">ディーラーがブラックジャックの場合、引き分けとなり配当はありません。そこで1.5倍の配当ではなく、ベットの同額分の配当を先につけてゲームを終わらせる（保険を使ってゲームを終わらせる）ことができます。</p>
        <p class="note" style="margin-top:6px">※ディーラーがノージャックの場合、イーブンマネーを使わなければ1.5倍の配当</p>
        <h3 class="h3">サレンダー</h3>
        <p>ゲストはカードを2枚配られて、ディーラーのアップカードを見た時点でベットの半額を支払いゲームを降りることができます。</p>
        <p style="margin-top:8px">「サレンダー」のコールは、ゲスト自身がHIT or STAYをコールする前にコールをしてもらいます（ディーラーから「サレンダー？」はコールしません）。ディーラーがブラックジャックの場合はサレンダーできません。</p>
      </div>
    </div>
    {subnav("casino-games/black-jack/")}
  </div>
</section>'''
    layout("casino-games/black-jack/", "ブラックジャック（Black Jack）のルール", "ブラックジャックのルール解説。カードの数え方、インシュランス・イーブンマネー・サレンダーなどの特殊ルールを立川 jokeR がわかりやすく紹介します。", body)

def baccarat():
    def tr(k, v): return f"<tr><th>{k}</th><td>{v}</td></tr>"
    p_rows = tr("0〜5","3枚目のカードを引く（ヒット）") + tr("6・7","カードを引いてはならない（スタンド）") + tr("8・9","BANKERが8・9でなければ自動的に勝ち（BANKERはカードを引くことができない）。BANKERも8・9の場合はそのまま勝負。")
    b_rows = (tr("0〜2","3枚目のカードを引く")
      + tr("3","PLAYERが3枚目を引かなかったら…BANKERは3枚目を引かなければならない。<br>PLAYERが3枚目を引いてそのカードが…「8」以外の場合、BANKERも3枚目を引かなければならない。「8」の場合、3枚目を引いてはならない。")
      + tr("4","PLAYERが3枚目を引かなかったら…BANKERは3枚目を引かなければならない。<br>PLAYERが3枚目を引いてそのカードが…「0」「1」「8」「9」以外の場合、BANKERも3枚目を引かなければならない。「0」「1」「8」「9」の場合、3枚目を引いてはならない。")
      + tr("5","PLAYERが3枚目を引かなかったら…BANKERは3枚目を引かなければならない。<br>PLAYERが3枚目を引いてそのカードが…「4」「5」「6」「7」の場合、BANKERも3枚目を引かなければならない。「4」「5」「6」「7」以外の場合、3枚目を引いてはならない。")
      + tr("6","PLAYERが3枚目を引かなかったら…BANKERは3枚目を引かなければならない。<br>PLAYERが3枚目を引いてそのカードが…「6」「7」の場合、BANKERも3枚目を引かなければならない。「6」「7」以外の場合、3枚目を引いてはならない。")
      + tr("7","3枚目を引くことはできない。")
      + tr("8・9","PLAYERが8・9でなければ自動的に勝ち（PLAYERはカードを引くことができない）。PLAYERも8・9の場合はそのまま勝負。"))
    body = phead("BACCARAT", "バカラ", "baccarat", ['<a href="{P}casino-games/">CASINO GAMES</a>', "BACCARAT"], "tint-gold") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap-s">
    <div class="block">
      <h2 class="h2" data-reveal>バカラのルール <small>RULES</small></h2>
      <div class="lead" data-reveal>
        <p>バカラとは、「バンカー」と「プレイヤー」の、仮想の二人による勝負で、どちらが勝つかを客が予想して賭けるゲームです。</p>
        <p>実際にゲームをプレイしているのは仮想の人物であるため、お客さんはどちらが勝つかを予想するだけになります。</p>
        <p class="pop" style="font-size:clamp(20px,2.4vw,26px)">2枚もしくは3枚のカードの合計点数の下一桁の数字が、<span class="y">9</span>に近い方が勝ち。</p>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>カードの数え方 <small>COUNT</small></h2>
      <div class="rule-grid" style="grid-template-columns:1fr 1fr">
        <div class="rule" data-reveal><h4>A（1）〜9 ＝ 数字通り</h4>{cards("A♥ 2♠ 5♦ 9♣", 46)}<p>A〜9はトランプの数字と同じ数で数えます。2であれば「2点」、5であれば「5点」、9であれば「9点」と数えます。</p></div>
        <div class="rule" data-reveal data-delay=".1"><h4>10・J・Q・K ＝ 0点</h4>{cards("10♣ J♣ Q♣ K♣", 46)}<p>10と、J／Q／Kの絵札はすべて「0点」で数えます。</p></div>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>3枚目を引く条件 <small>THIRD CARD</small></h2>
      <p data-reveal>2枚カードを引いた時点での手札の合計点数の下一桁の数字によって、3枚目を引く条件が変わります。ただし、プレイヤーとバンカーのいずれかの点数がナチュラル（8点か9点）の場合は、両者とも3枚目のカードは引きません。</p>
      <h3 class="h3" data-reveal>プレイヤーの最初の2枚のカードの合計の下一桁</h3>
      <div style="overflow-x:auto" data-reveal><table class="btable"><thead><tr><th>合計</th><th>PLAYER</th></tr></thead><tbody>{p_rows}</tbody></table></div>
      <h3 class="h3" data-reveal>バンカーの最初の2枚のカードの合計の下一桁</h3>
      <div style="overflow-x:auto" data-reveal><table class="btable"><thead><tr><th>合計</th><th>BANKER</th></tr></thead><tbody>{b_rows}</tbody></table></div>
    </div>
    {subnav("casino-games/baccarat/")}
  </div>
</section>'''
    layout("casino-games/baccarat/", "バカラ（Baccarat）のルール", "バカラのルール解説。カードの数え方、プレイヤー・バンカーが3枚目を引く条件を立川 jokeR がわかりやすく紹介します。", body)

def holdem():
    hands = [("ワンペア","同じ数字のカードが1組だけある。","K♠ K♥ 4♣ 8♦ 2♠"),
             ("ツーペア","同じ数字のカードが2組ある。","J♠ J♦ 5♣ 5♥ 9♠"),
             ("スリーカード","同じ数字のカードが3枚ある。","7♠ 7♥ 7♦ Q♣ 3♠"),
             ("ストレート","マークに関係なく、5枚の数字が連続する。（10-J-Q-K-Aはストレートとなるが、Q-K-A-2はストレートにならない。すなわち、KとAは連続するが、K-A-2を含むものはストレートにならない。）","5♣ 6♦ 7♠ 8♥ 9♣"),
             ("フラッシュ","数字に関係なく、同じマークのカードが5枚ある。","2♥ 6♥ 9♥ J♥ K♥"),
             ("フルハウス","スリーカードとワンペアが1組ずつできる。","5♣ 5♦ K♠ K♦ K♥"),
             ("フォーカード","同じ数字のカードが4枚ある。","9♠ 9♥ 9♦ 9♣ A♠"),
             ("ストレートフラッシュ","同じマークで、5枚の数字が連続する。","5♠ 6♠ 7♠ 8♠ 9♠"),
             ("ロイヤルストレートフラッシュ","同じマークの10、J、Q、K、Aをそろえる。","10♥ J♥ Q♥ K♥ A♥")]
    hh = "".join(f'<div class="hand" data-reveal><b>{n}</b><div><p>{d}</p>{cards(c)}</div></div>' for n,d,c in hands)
    body = phead("TEXAS HOLD’EM", "テキサス・ホールデム", "poker", ['<a href="{P}casino-games/">CASINO GAMES</a>', "TEXAS HOLD’EM"], "tint-green") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap-s">
    <div class="block">
      <h2 class="h2" data-reveal>テキサス・ホールデムのルール <small>RULES</small></h2>
      <div class="lead" data-reveal>
        <p>テキサス・ホールデム（Texas hold’em）はポーカーの一種。</p>
        <p>各プレイヤーごとに配られる2枚の手札と、コミュニティ・カードと呼ばれる全プレイヤー共通のカードを組み合わせて役をつくり勝負します。</p>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>ポーカーの役 <small>HANDS</small></h2>
      <div data-reveal><p>ポーカーの役を、弱い順に紹介します。</p>
      <p style="margin-top:8px">2人のプレイヤーが同じ役を作った場合は、役を構成しているカードの数字が強い方（A、K、…2の順）が勝ちとなります。役を構成しているカードも同じ場合は、役に使われていないカードが強い方が勝ちとなります。</p>
      <p class="pop" style="font-size:18px;margin-top:12px">テキサス・ホールデムでは、7枚の中から役がもっとも強くなる<span class="y">5枚</span>を選択して、その5枚の役で勝負します。</p></div>
      <div class="hands" style="margin-top:24px">{hh}</div>
    </div>
    {subnav("casino-games/texas-holdem/")}
  </div>
</section>'''
    layout("casino-games/texas-holdem/", "テキサス・ホールデム（Texas hold’em）のルール", "ポーカー（テキサス・ホールデム）のルールと役の一覧。ワンペアからロイヤルストレートフラッシュまで、立川 jokeR がわかりやすく紹介します。", body)

# ===================================================== DEALER (ナビには出さない：現行サイトでも非表示)
def dealer():
    ds = [("♠","サワ"),("♠","Ten"),("♠","カイト"),("♥","つばさ"),("♥","しほみ"),("♥","しぃな"),("♥","なな"),("♥","ゆかり"),("♥","きらり"),("♥","跳華"),("♥","れいな"),("♥","みりな")]
    cs = "".join(f'''<div class="dealer" data-reveal data-delay="{(i%6)*0.06:.2f}"><div class="dealer__card"><div class="dealer__face{" r" if s=="♥" else ""}"><span class="s tl">{s}</span><span class="ph">PHOTO</span><b>{n}</b><span class="s br">{s}</span></div><div class="dealer__back"><span>{n}</span></div></div></div>''' for i,(s,n) in enumerate(ds))
    body = phead("DEALER", "ディーラー紹介", "dealer", ["DEALER"], "tint-red") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap">
    <h2 class="h2" data-reveal>在籍ディーラー <small>DEALERS</small></h2>
    <div class="dealers">{cs}</div>
  </div>
</section>'''
    layout("profile/", "ディーラー紹介", "立川 jokeR の在籍ディーラー紹介。", body)

# ===================================================== ACCESS
def access():
    body = phead("ACCESS", "アクセス", "table", ["ACCESS"]) + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap">
    <h2 class="h2" data-reveal>店舗情報 <small>SHOP INFO</small></h2>
    {access_block()}
    <div class="btns" data-reveal><a class="btn" href="tel:{TEL}">電話する {TEL}</a><a class="btn" href="{{P}}contact/">お問い合わせ</a></div>
  </div>
</section>'''
    layout("access/", "アクセス・店舗情報", "立川 jokeR（ジョーカー）へのアクセス。JR立川駅南口から徒歩3分、東京都立川市錦町1-2-13 中島ビル2F。営業時間・定休日・電話番号のご案内。", body)

# ===================================================== RECRUIT
def recruit():
    body = phead("RECRUIT", "キャスト・スタッフ募集", "dealer", ["RECRUIT"], "tint-red") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap">
    <div class="block">
      <p class="pop" data-reveal style="font-size:clamp(24px,3.6vw,42px);text-align:center">おしゃれな空間で、<br class="sp">やり甲斐のある仕事を<br>してみませんか？</p>
      <p data-reveal style="text-align:center;margin-top:16px">アミューズメントカジノ jokeR では、スタッフを募集しております。</p>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>時給 <small>JOBS</small></h2>
      <div class="jobs">
        <div class="job" data-reveal><h3>ディーラー</h3><p class="pay">1,300<small>円〜</small></p><p>能力により昇給可能。未経験可／経験者優遇</p><p class="note" style="margin-top:10px">★ディーラー経験者優遇！未経験者でも資格を持った当店講師が丁寧に教えます。</p></div>
        <div class="job" data-reveal data-delay=".1"><h3>ホールスタッフ</h3><p class="pay">1,300<small>円</small></p><p>研修中 1,200円</p><p class="note" style="margin-top:10px">★食事やドリンクを運んだりするウェイトレス業務になります。</p></div>
        <div class="job" data-reveal data-delay=".2"><h3>キッチン</h3><p class="pay">1,300<small>円</small></p><p>研修中 1,200円</p><p class="note" style="margin-top:10px">★キッチン経験者優遇！未経験者でも当店スタッフがしっかり指導します。</p></div>
      </div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>勤務条件 <small>CONDITIONS</small></h2>
      <ul class="tags" data-reveal><li>定休：月曜日</li><li>週1回からOK</li><li>土日祝出勤できる方優遇</li><li>14:00〜24:00（内4時間から）</li><li>交通費応相談</li></ul>
      <h2 class="h2" style="margin-top:50px" data-reveal>待遇 <small>BENEFITS</small></h2>
      <ul class="tags" data-reveal><li>ノルマ一切無し</li><li>終電考慮します</li><li>女性スタッフ制服貸与</li><li>女性フロアスタッフのみ体験入店有</li><li>ピアス・ネイルOK</li><li>髪色自由</li><li>〜40歳まで応募可能</li><li>フリーター歓迎</li></ul>
      <p class="note" style="margin-top:12px">※詳しくはお問い合わせください。</p>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>応募方法 <small>ENTRY</small></h2>
      <p data-reveal>当店ではスタッフを募集しております。ご興味のある方はご連絡ください。メールでのお問い合わせもお待ちしております。</p>
      <div class="cways" style="margin-top:20px">
        <div class="cway" data-reveal><h3>お電話（店舗）</h3><a class="v" href="tel:{TEL}">{TEL}</a></div>
        <div class="cway" data-reveal data-delay=".1"><h3>メール</h3><a class="v s" href="mailto:{MAIL}?subject=%E6%B1%82%E4%BA%BA%E3%81%B8%E3%81%AE%E5%BF%9C%E5%8B%9F">{MAIL}</a></div>
      </div>
    </div>
  </div>
</section>'''
    layout("recruit/", "キャスト・スタッフ募集", "立川 jokeR のスタッフ募集。ディーラー・ホールスタッフ・キッチン。未経験OK、資格を持った講師が丁寧に指導します。", body)

# ===================================================== CONTACT
def contact():
    body = phead("CONTACT", "お問い合わせ", "chips", ["CONTACT"], "tint-dark") + f'''
<section class="sec" style="padding-top:50px">
  <div class="wrap-s">
    <div class="block">
      <p data-reveal>お問い合わせは、お電話・メール・お問い合わせフォームにてお受けしております。なお、ご予約や貸切のご相談もお受けしております。まずは、お問い合わせください。</p>
      <div class="cways" style="margin-top:26px">
        <div class="cway" data-reveal><h3>お電話でのお問い合わせ</h3><a class="v" href="tel:{TEL}">{TEL}</a><p class="note">受付：営業時間内</p></div>
        <div class="cway" data-reveal data-delay=".1"><h3>メールでのお問い合わせ</h3><a class="v s" href="mailto:{MAIL}">{MAIL}</a><p class="note">受付：24時間365日</p></div>
      </div>
      <div class="btns" data-reveal><a class="lineb" href="{LINE_URL}" target="_blank" rel="noopener">{IC_LINE} 公式LINEで問い合わせる</a></div>
    </div>
    <div class="block">
      <h2 class="h2" data-reveal>フォームでのお問い合わせ <small>FORM</small></h2>
      <form class="form box" id="contact-form" data-reveal>
        <div><label for="f-name">お名前<i>必須</i></label><input id="f-name" name="name" required autocomplete="name"></div>
        <div><label for="f-tel">電話番号<i>必須</i></label><input id="f-tel" name="tel" type="tel" required autocomplete="tel"></div>
        <div><label for="f-email">メールアドレス<i>必須</i></label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
        <div><label for="f-msg">ご要望やご質問など<i class="o">任意</i></label><textarea id="f-msg" name="message"></textarea></div>
        <div class="sr"><label for="f-web">このフィールドは空のままにしてください。</label><input id="f-web" name="website" tabindex="-1" autocomplete="off"></div>
        <p class="note">上記の内容をご確認のうえ［この内容で送信する］ボタンを押してください。お使いのメールアプリが開きますので、そのまま送信してください。</p>
        <div style="text-align:center"><button class="btn" type="submit">この内容で送信する</button></div>
      </form>
    </div>
  </div>
</section>'''
    layout("contact/", "お問い合わせ・ご予約", "立川 jokeR へのお問い合わせ・ご予約・貸切のご相談。お電話・メール・公式LINE・フォームで受け付けています。", body)

def notfound():
    body = f'''<section class="sec" style="min-height:80vh;display:grid;place-items:center;text-align:center"><div class="wrap">
<p class="phead__en">4<span style="color:var(--red)">0</span>4</p><p class="pop" style="font-size:24px;margin:16px 0 30px">ページが見つかりませんでした</p><a class="btn" href="/">トップへ戻る</a></div></section>'''
    layout("", "ページが見つかりません", "お探しのページは見つかりませんでした。", body)
    os.replace(os.path.join(OUT, "index.html"), os.path.join(OUT, "404.html"))

notfound(); top(); system(); menu(); games(); blackjack(); baccarat(); holdem(); dealer(); access(); recruit(); contact()
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
paths = ["", "system/", "menu/", "casino-games/", "casino-games/black-jack/", "casino-games/baccarat/", "casino-games/texas-holdem/", "profile/", "access/", "recruit/", "contact/"]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in paths) + "</urlset>\n")
print("built")
import re
p404 = os.path.join(OUT, "404.html")
s = open(p404, encoding="utf-8").read()
s = re.sub(r'(href|src)="(?!https?:|/|#|tel:|mailto:)(\./)?', r'\1="/', s)
open(p404, "w", encoding="utf-8").write(s)
