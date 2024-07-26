import streamlit as st
from PIL import Image
import io

def resize_image(image, scale_factor, quality):
    # 元の画像サイズを取得
    width, height = image.size
    # 新しいサイズを計算
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    # 画像をリサイズ
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    # 画像をバイトデータに変換
    img_byte_arr = io.BytesIO()
    resized_image.save(img_byte_arr, format=image.format, quality=quality)
    img_byte_arr = img_byte_arr.getvalue()
    return resized_image, img_byte_arr

def main():
    st.title("画像リサイズ＆軽量化アプリ")

    uploaded_file = st.file_uploader("画像ファイルをアップロードしてください (PNG/JPEG)", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="元の画像", use_column_width=True)

        st.sidebar.header("調整オプション")
        scale_factor = st.sidebar.slider("縮小比率", 0.1, 1.0, 0.5)
        quality = st.sidebar.slider("画質 (JPEGのみ)", 10, 100, 85)

        if st.sidebar.button("画像を処理"):
            resized_image, img_byte_arr = resize_image(image, scale_factor, quality)
            st.image(resized_image, caption="リサイズされた画像", width=resized_image.width)

            st.download_button(
                label="リサイズ画像をダウンロード",
                data=img_byte_arr,
                file_name="resized_image." + image.format.lower(),
                mime="image/" + image.format.lower()
            )

if __name__ == "__main__":
    main()
