# 画像の縮小と画質調整 Streamlit アプリ

このStreamlitアプリは、アップロードされた画像（JPG, JPEG, PNG形式）の縮小比率と画質を調整します。

## 使用方法

1. StreamlitとPIL（Pillow）をインストールします。
    ```bash
    pip install streamlit pillow
    ```

2. 以下のPythonコードを`app.py`として保存します。

    ```python
    import streamlit as st
    from PIL import Image

    # タイトル
    st.title('画像の縮小と画質調整')

    # 画像のアップロード
    uploaded_file = st.file_uploader("画像をアップロードしてください。", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # 画像を読み込む
        image = Image.open(uploaded_file)
        
        # オリジナル画像を表示
        st.image(image, caption="オリジナル画像", use_column_width=True)
        
        # 縮小比率と画質のスライダー
        ratio = st.slider("縮小比率（1/n）", 1, 10, 1)
        quality = st.slider("画質（1-100）", 1, 100, 85)
        
        # 画像の縮小
        width, height = image.size
        new_width = int(width / ratio)
        new_height = int(height / ratio)
        resized_image = image.resize((new_width, new_height))
        
        # 画質調整と保存
        output_img_path = "resized_image.jpg"
        resized_image.save(output_img_path, quality=quality)
        
        # 処理後の画像を表示
        st.image(output_img_path, caption="処理後の画像")
    ```

3. ターミナルで以下のコマンドを実行してアプリを起動します。
    ```bash
    streamlit run app.py
    ```

アプリが起動すると、画像をアップロードし、縮小比率と画質を調整できます。
