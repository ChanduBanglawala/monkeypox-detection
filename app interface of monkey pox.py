import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load model
model = tf.keras.models.load_model("C:\\Users\\Downloads\\monkeypox_vgg16.keras")

# Title
st.set_page_config(page_title="Monkeypox Detection")

st.title("🦠 Monkeypox Detection System")
st.write("Upload a skin lesion image for prediction")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    img = image.resize((224,224))
    img = np.array(img)

    if len(img.shape) == 2:
        img = np.stack((img,)*3, axis=-1)

    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    

    if prediction < 0.5:
        st.error("⚠️ Monkeypox Detected")
        confidence = (1 - prediction) * 100
        st.write(f"Confidence: {confidence:.2f}%")
    else:
        st.success("✅ Normal Skin")
        confidence = prediction * 100
        st.write(f"Confidence: {confidence:.2f}%")
