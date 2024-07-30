# 画像リサイズ＆軽量化アプリ

このプロジェクトは、画像をリサイズして軽量化するためのStreamlitアプリケーションです。ユーザーは画像をアップロードし、サイズと画質を調整することができます。

## 概要

このアプリケーションでは、以下の機能を提供しています：

- 画像のアップロード（PNG/JPEG形式）
- 画像の縮小比率の調整
- 画像の画質の調整（JPEGのみ）
- リサイズされた画像の表示
- リサイズされた画像のダウンロード

## インストール

このプロジェクトをローカル環境で動かすためには、以下の手順に従ってください。

1. リポジトリをクローンします：

   ```sh
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. 必要なパッケージをインストールします：

   ```sh
   pip install -r requirements.txt
   ```

## 使い方

アプリケーションを起動するには、以下のコマンドを実行します：

```sh
streamlit run app.py
```

ブラウザで`http://localhost:8501`を開き、画像をアップロードして、サイズと画質を調整します。

## ファイル構成

- `app.py`：メインのアプリケーションコード
- `requirements.txt`：必要なPythonパッケージのリスト

## 貢献

貢献方法：

1. リポジトリをフォーク(Fork)します。
2. フィーチャーブランチを作成します(`git checkout -b feature/AmazingFeature`)。
3. 変更をコミットします(`git commit -m 'Add some AmazingFeature'`)。
4. ブランチをプッシュします(`git push origin feature/AmazingFeature`)。
5. プルリクエストを作成します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルを参照してください。

## 著者

- 名前: Hiroe Matsuno
