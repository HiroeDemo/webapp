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
