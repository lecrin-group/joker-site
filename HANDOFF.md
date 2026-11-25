# HANDOFF — jokeR 立川 公式サイト（新）

公開先：https://joker.lecrin.biz （Xserver。GitHub から自動アップ）／ 旧サイト：https://casino-joker.jp/
リポジトリ：https://github.com/lecrin-group/joker-site
公開のしかた：main に push すると `.github/workflows/deploy.yml` が FTP で Xserver の joker.lecrin.biz のフォルダへ自動アップ（他のサイトと同じ形。見本は hearts-recruit）。DNS はさわらない（Xserver でサブドメインを作ったときの A レコードのまま）
- Secrets：FTP_SERVER = sv8695.xserver.jp ／ FTP_USERNAME = github-joker@lecrin.biz（jokeR 専用。joker.lecrin.biz のフォルダにしか入れない）／ FTP_PASSWORD（ナギサが管理）／ FTP_SERVER_DIR = ./
- Variables：DEPLOY_ENABLED = true（入れてある。push のたびに本番へ自動アップ）
- `_tools/`・`img/orig/`・`*.md`・`.htaccess`・`.htpasswd` はサーバーに上げない
- `.htaccess` はサーバーにあるものが本物（Xserver の「アクセス制限」の鍵がここに書かれるため）。404 の設定などを直すときは Xserver のファイルマネージャで直す
新しい順に上から書く。

## いまの状態（2026-11-25）

- 旧サイトの全ページの中身を移した（TOP・SYSTEM・MENU・CASINO GAMES と3つのルール・DEALER・ACCESS・RECRUIT・CONTACT）。URL も旧サイトと同じ形（/system/ など）にしてある
- デザイン：GLOBAL GROVE（global-grove.com）を8割、BAGUS・REGALO を2割。高級にしすぎない、ポップ寄り
  - GROVE から：ローディング、左上の黒ラベルのナビ、白い四角のハンバーガー、写真の斜めストライプ、袋文字の英字、ネオンの筆記体見出し、カッコ型の枠とネオンアイコン、色ベタの区画を斜めに流れる文字
  - BAGUS・REGALO から：明朝体の英字見出し＋小さい日本語、PICK UP のスライダー、細い線のボタン、メニュー表
- 写真は店内の撮影（動画のコマ）と、ナギサからもらった7枚を使っている。（`img/photo/` の bar-lamps・cocktails・casino-dealer・bar-bottles・chips-dice・royal-flush・bet-chips）。**仮の画像が残っているのはバカラだけ**（`img/ph/baccarat.svg`）
- ロゴは文字で作った仮のもの（o の字をチップにした）。元データが届いたら差し替え
- お問い合わせフォームは、送信するとメールアプリが開く方式（GitHub Pages ではフォームの受信ができないため）

## 作り方

- `_tools/build.py` が全ページの HTML を作る。中身を直すときは build.py を直してから、リポジトリの一番上で `python3 _tools/build.py .`
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

- 2026-11-25 トップの中間（ROULETTE と SYSTEM の間）に、フッターと同じ「ふちだけ・グラデーションが流れる文字」を追加（逆向きに流れる。文言は `_tools/build.py` の `MID_MARQ`）
- 2026-11-25 スマホのメニューを PC に近づけた：上部に PC と同じ店内写真（ゆっくりズーム）、ボタンの位置から円が広がって開く、開く前にハンバーガーの線が伸びる、項目をタップすると各色（ピンク・シアン・黄・緑・紫）で光ってから移動
- 2026-11-25 スマホでメニュー画面が左右にブレるのを修正（メニューを縦スクロールだけにして、背景の光やスライドイン演出で横に動かないようにした）
- 2026-11-25 トップの切り替えの2・3枚目を、ナギサからもらった「エースとチップ」「ネオンのボトル棚」に差し替え（スマホは縦に切り出したもの）。チップの「10K」の文字は、賭博と誤解されないよう画像を加工して消した
- 2026-11-25 PAGE TOP ボタンを赤白のカジノチップに（スクロールに合わせて回る）
- 2026-11-25 フッターの流れる文字を「ふちだけ・色が流れるグラデーション」に（SVG）。公式SNSのボタンを追加（メニュー画面とフッター）：Instagram は入れた。TikTok・YouTube・Threads は URL 待ち（`_tools/build.py` の `TIKTOK_URL`・`YOUTUBE_URL`・`THREADS_URL` に入れて build すると出る）
- 2026-11-25 ロゴの「o」のチップを、ナギサからもらった赤白のチップのイラストに差し替え（`img/chip-red.png`。背景を透明に切り抜いたもの）
- 2026-11-25 トップを3パターンで切り替え（7秒ごと）：①店内の動画 ②IMG_5924（カードを配る）③赤いカーテンの店内。スマホは縦の写真に入れ替わる（`img/photo/hero-*`）。光の演出（ライト・レーザー・光の粒・ストロボ）を控えめにした
- 2026-11-25 フッターの流れる文字を明るいネオンに、「Join us!」を見出しから離した、PAGE TOP とページ内リンクを高速スクロールに（約0.5〜1.1秒で移動が見える）
- 2026-11-25 店長確認のため Xserver の「アクセス制限」（ID・パスワード）をかける準備。自動アップで鍵が外れないよう、.htaccess・.htpasswd を上げない設定にした
- 2026-11-25 Xserver へ初回アップ（jokeR 専用 FTP アカウント github-joker@lecrin.biz を作成）
- 2026-11-25 ナギサが店内で撮った動画・写真（ダウンロードの IMG_59xx・LongVideo）から差し替え：トップの背景を店内の動画に（`img/video/hero-wide.mp4` は PC、`hero-tall.mp4` はスマホ。各8秒・約5MB）。紹介の写真・ブラックジャック・バカラ・スタッフ募集・メニュー画面・ディーラー/求人/アクセスの見出しを店内の写真に（`img/photo/store-*.jpg`、動画のコマを切り出して色を整えたもの）。写っている方の掲載許可は取得済み。仮の画像はなくなった
- 2026-11-25 トップ（Select より上）をナイトクラブ風に作り直し：ネオンのロゴ・ハンバーガー・ヒーロー（ライトの光線・レーザー・ストロボ・光の粒）・PICK UP と NEWS をネオンのカードに。フォントに Monoton・Zen Kaku 900 を追加
- 2026-11-25 公開のしかたを GitHub Pages から、他のサイトと同じ「Xserver へ FTP 自動アップ」に変えた（GitHub Pages は止めた。CNAME・_config.yml は削除、.htaccess で 404 ページを設定）
- 2026-11-25 GitHub に上げた（lecrin-group/joker-site）
- 2026-11-25 ナギサの写真7枚に差し替え（バカラ以外）
- 2026-11-25 新サイトを作成（Claude Code）。ドメイン joker.lecrin.biz をナギサが作成
