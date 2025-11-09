import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# ---------------- Streamlit Page Setup ----------------
st.set_page_config(page_title="🖋️ Handwritten Digit + Text Recognizer", page_icon="🧠", layout="wide")

st.markdown("""
<h1 style='text-align:center; color:#3B82F6;'>🖋️ Handwritten Digit + Text Recognizer</h1>
<h3 style='text-align:center; color:#10B981;'>By <b>Shibnath Sahoo</b></h3>
<p style='text-align:center; font-size:16px;'>Draw or upload a handwritten digit (0-9) and see how the CNN model recognizes it — both as an image and text!</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- Load & Preprocess Data ----------------
@st.cache_resource
def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    return (x_train, y_train), (x_test, y_test)

(x_train, y_train), (x_test, y_test) = load_data()

# ---------------- Build CNN Model ----------------
@st.cache_resource
def create_model():
    model = Sequential([
        Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, kernel_size=3, activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

model = create_model()

# ---------------- Training Section ----------------
st.sidebar.header("⚙️ Model Training")
if st.sidebar.button("Train Model (Quick Demo)"):
    with st.spinner("Training CNN model... please wait ⏳"):
        model.fit(x_train, y_train, epochs=2, batch_size=128, validation_split=0.1, verbose=1)
    loss, acc = model.evaluate(x_test, y_test)
    st.success(f"✅ Model trained successfully! Test Accuracy: {acc:.4f}")

# ---------------- Drawing & Upload Section ----------------
tab1, tab2 = st.tabs(["✏️ Draw Digit", "📤 Upload Image"])

with tab1:
    st.subheader("🖊️ Draw a Digit Below")
    canvas_result = st_canvas(
        fill_color="#000000",
        stroke_width=10,
        stroke_color="#FFFFFF",
        background_color="#000000",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("🔍 Predict from Drawing"):
        if canvas_result.image_data is not None:
            img = canvas_result.image_data[:, :, 0]
            img = tf.image.resize(img, [28, 28])
            img = tf.cast(img, tf.float32) / 255.0
            img = tf.reshape(img, (1, 28, 28, 1))

            prediction = model.predict(img)
            digit = np.argmax(prediction)

            st.image(canvas_result.image_data, caption=f"🖼️ Your Drawn Digit: {digit}", width=200)
            st.success(f"🎯 Predicted Digit: **{digit}**")

            fig, ax = plt.subplots()
            ax.bar(range(10), prediction[0])
            ax.set_xticks(range(10))
            ax.set_xlabel("Digits")
            ax.set_ylabel("Confidence")
            st.pyplot(fig)
        else:
            st.warning("Please draw a digit first!")

with tab2:
    st.subheader("📂 Upload a Digit Image")
    uploaded_file = st.file_uploader("Choose a digit image file (PNG or JPG)", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("L").resize((28, 28))
        img_array = np.array(image)
        img_array = 255 - img_array  # invert for white digits on black background
        img_array = img_array / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        prediction = model.predict(img_array)
        digit = np.argmax(prediction)

        st.image(uploaded_file, caption=f"🖼️ Uploaded Digit: {digit}", width=200)
        st.success(f"🧠 Predicted Digit (Text): **{digit}**")

        fig, ax = plt.subplots()
        ax.bar(range(10), prediction[0])
        ax.set_xticks(range(10))
        ax.set_xlabel("Digits")
        ax.set_ylabel("Confidence")
        st.pyplot(fig)

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("<p style='text-align:center; font-size:14px;'>Made with ❤️ using TensorFlow + Streamlit | By <b>Shibnath Sahoo</b></p>", unsafe_allow_html=True)
