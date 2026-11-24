# HANDOFF — jokeR 立川 公式サイト（新）

公開先：https://joker.lecrin.biz （GitHub Pages）／ 旧サイト：https://casino-joker.jp/
リポジトリ：https://github.com/lecrin-group/joker-site （Public・main の一番上を公開）／ Pages 設定：https://github.com/lecrin-group/joker-site/settings/pages
DNS：lecrin.biz は Xserver。joker の CNAME → lecrin-group.github.io
新しい順に上から書く。

## いまの状態（2026-11-25）

- 旧サイトの全ページの中身を移した（TOP・SYSTEM・MENU・CASINO GAMES と3つのルール・DEALER・ACCESS・RECRUIT・CONTACT）。URL も旧サイトと同じ形（/system/ など）にしてある
- デザイン：GLOBAL GROVE（global-grove.com）を8割、BAGUS・REGALO を2割。高級にしすぎない、ポップ寄り
  - GROVE から：ローディング、左上の黒ラベルのナビ、白い四角のハンバーガー、写真の斜めストライプ、袋文字の英字、ネオンの筆記体見出し、カッコ型の枠とネオンアイコン、色ベタの区画を斜めに流れる文字
  - BAGUS・REGALO から：明朝体の英字見出し＋小さい日本語、PICK UP のスライダー、細い線のボタン、メニュー表
- 写真は 2026-11-25 にナギサからもらった7枚に差し替え済み（`img/photo/` の bar-lamps・cocktails・casino-dealer・bar-bottles・chips-dice・royal-flush・bet-chips）。**仮の画像が残っているのはバカラだけ**（`img/ph/baccarat.svg`）
- ロゴは文字で作った仮のもの（o の字をチップにした）。元データが届いたら差し替え
- お問い合わせフォームは、送信するとメールアプリが開く方式（GitHub Pages ではフォームの受信ができないため）

## 作り方

- `_tools/build.py` が全ページの HTML を作る。中身を直すときは build.py を直してから、リポジトリの一番上で `python3 _tools/build.py .`
- `_` で始まるフォルダは GitHub Pages で公開されない
- CSS：`assets/css/style.css`、JS：`assets/js/main.js`（ライブラリなし）。直したら build.py の `VER` を変える（キャッシュ対策）

## 写真の差し替え方

1. 写真を `img/photo/` に入れる（例 `img/photo/roulette.jpg`、横1600px くらいに縮める）
2. `_tools/build.py` の `IMG = {...}` の該当行を、`img/ph/○○.svg` から新しいファイルに書き換える
3. `python3 _tools/build.py .` を実行

| IMG の名前 | 今の写真 | 使っている場所 |
|---|---|---|
| hero | casino-dealer.jpg（赤い台でカードを配る手） | トップの大きい写真1枚目 |
| hands | casino-dealer.jpg | スタッフ募集の帯・ゲーム解説の見出し |
| chips | chips-dice.jpg（チップとサイコロ） | トップ3枚目・料金/お問い合わせの見出し |
| lounge | bar-lamps.jpg（ランプのバーカウンター） | トップの「立川でのカジノ遊びは」の横 |
| blackjack・dealer | bet-chips.jpg（チップを置く手） | ブラックジャック区画・PICK UP の求人・求人/ディーラーの見出し |
| poker | royal-flush.jpg（640px と小さめ） | ポーカー区画・ルールページ |
| highball | cocktails.jpg | FOOD & DRINK の大きい写真 |
| shelf | bar-bottles.jpg | NEWS 欄・メニューの見出し |
| baccarat | **仮の画像のまま** | バカラ区画・ルールページ。候補：写真AC https://www.photo-ac.com/main/detail/875317 |

旧サイトの写真（`img/orig/`）から切り出して使っているもの：店内のルーレットとバーカウンター、料理6枚、お祝いプレート・ワイン（`img/photo/`）。どれも小さく画質が低いので、撮影できたら差し替えたい。

## 課題

- お店に確認してから直すこと（料金・営業時間・求人の条件など）は、課題シート「jokeR_課題」No.37〜39 に書いてある（リポジトリは公開されるので、ここには細かく書かない）
- DEALER ページ（/profile/）は旧サイト同様ナビには出していない。写真が届いたらカードに入れる
- 旧サイトにあった、閲覧数カウンター・ポイントランキング（非表示だった）・公式アプリのバナー（非表示だった）は移していない
- 旧サイトの地図（Googleマイマップ）は消えていたので、住所の Google マップに替えた

## これまで

- 2026-11-25 GitHub に公開（lecrin-group/joker-site）。最初の push は写真差し替え前の版だった。DNS は Xserver で A レコードを消して CNAME に替える必要あり（課題 No.37）
- 2026-11-25 ナギサの写真7枚に差し替え（バカラ以外）
- 2026-11-25 新サイトを作成（Claude Code）。ドメイン joker.lecrin.biz をナギサが作成
