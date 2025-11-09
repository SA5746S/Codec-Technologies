# # import streamlit as st
# # from deep_translator import GoogleTranslator
# # from gtts import gTTS
# # import speech_recognition as sr
# # import tempfile
# # import os

# # # --- Streamlit Page Config ---
# # st.set_page_config(page_title="🎧 AI Voice Translator", page_icon="🌍", layout="centered")

# # # --- App Header ---
# # st.title("🎙️ AI Voice Translator with Audio & History")
# # st.write("Developed by **Shibnath Sahoo** | Speak or type text → translate → listen 🔊")

# # st.markdown("---")

# # # --- Initialize Session State ---
# # if 'history' not in st.session_state:
# #     st.session_state['history'] = []
# # if 'input_text' not in st.session_state:
# #     st.session_state['input_text'] = ""

# # # --- Function: Speech Recognition ---
# # def recognize_speech():
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         st.info("🎤 Listening... (Speak for up to 5 seconds)")
# #         audio = recognizer.listen(source, phrase_time_limit=5)
# #         try:
# #             text = recognizer.recognize_google(audio)
# #             st.success(f"✅ You said: {text}")
# #             return text
# #         except sr.UnknownValueError:
# #             st.error("❌ Could not understand your voice.")
# #         except sr.RequestError:
# #             st.error("⚠️ Speech recognition service error.")
# #     return None

# # # --- Language Map for TTS ---
# # lang_codes = {
# #     "Auto": "en",
# #     "English": "en",
# #     "Hindi": "hi",
# #     "Bengali": "bn",
# #     "French": "fr",
# #     "Spanish": "es",
# #     "German": "de",
# #     "Japanese": "ja",
# #     "Korean": "ko",
# #     "Russian": "ru",
# #     "Chinese": "zh-CN"
# # }

# # # --- Language Selection ---
# # langs = list(lang_codes.keys())
# # col1, col2 = st.columns(2)
# # with col1:
# #     src = st.selectbox("🌐 Source Language", langs, index=0)
# # with col2:
# #     dest = st.selectbox("🎯 Target Language", langs, index=2)

# # # --- Input Area ---
# # st.write("### 📝 Enter or Speak Text:")
# # text = st.text_area("Type or speak here:", st.session_state['input_text'], height=120)

# # # --- Microphone Input ---
# # if st.button("🎤 Speak"):
# #     spoken_text = recognize_speech()
# #     if spoken_text:
# #         st.session_state['input_text'] = spoken_text
# #         st.rerun()

# # # --- Translate Button ---
# # if st.button("🔄 Translate"):
# #     if not text.strip():
# #         st.warning("⚠️ Please enter or speak some text first.")
# #     else:
# #         try:
# #             # --- Translation ---
# #             translated = GoogleTranslator(source=src, target=dest).translate(text)

# #             # --- Display Both Texts ---
# #             st.subheader("🗣️ Original Text:")
# #             st.info(text)
# #             st.subheader("🌍 Translated Text:")
# #             st.success(translated)

# #             # --- Save to History ---
# #             st.session_state['history'].append({
# #                 "original": text,
# #                 "translated": translated,
# #                 "source": src,
# #                 "target": dest
# #             })

# #             # --- Generate & Play Original Audio ---
# #             src_code = lang_codes.get(src, "en")
# #             dest_code = lang_codes.get(dest, "en")

# #             tts_input = gTTS(text, lang=src_code)
# #             input_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
# #             tts_input.save(input_audio.name)
# #             st.audio(input_audio.name, format="audio/mp3")
# #             st.caption("🔊 Original text audio")

# #             # --- Generate & Play Translated Audio ---
# #             tts_output = gTTS(translated, lang=dest_code)
# #             output_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
# #             tts_output.save(output_audio.name)
# #             st.audio(output_audio.name, format="audio/mp3")
# #             st.caption("🎧 Translated text audio")

# #         except Exception as e:
# #             st.error(f"❌ Error: {str(e)}")

# # st.markdown("---")

# # # --- Translation History ---
# # if st.session_state['history']:
# #     st.subheader("🕘 Translation History")
# #     for idx, item in enumerate(reversed(st.session_state['history']), start=1):
# #         with st.expander(f"🔹 {idx}. {item['source']} → {item['target']}"):
# #             st.write(f"**Original:** {item['original']}")
# #             st.write(f"**Translated:** {item['translated']}")

# # st.caption("💡 Powered by Deep Translator, Google Speech Recognition & gTTS | Created by Shibnath Sahoo 🎓")


# import streamlit as st
# from deep_translator import GoogleTranslator
# from gtts import gTTS
# import speech_recognition as sr
# import tempfile
# import os

# # --- Streamlit Page Config ---
# st.set_page_config(page_title="🎧 AI Voice Translator", page_icon="🌍", layout="centered")

# # --- App Header ---
# st.markdown("<h1 style='text-align:center;'>🎙️ AI Voice Translator with Audio & History</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; color:gray;'>Developed by <b>Shibnath Sahoo</b> | Speak or type text → Translate → Listen 🔊</p>", unsafe_allow_html=True)
# st.markdown("---")

# # --- Initialize Session State ---
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'input_text' not in st.session_state:
#     st.session_state['input_text'] = ""

# # --- Function: Speech Recognition ---
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎤 Listening... (Speak for up to 5 seconds)")
#         audio = recognizer.listen(source, phrase_time_limit=5)
#         try:
#             text = recognizer.recognize_google(audio)
#             st.success(f"✅ You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             st.error("❌ Could not understand your voice.")
#         except sr.RequestError:
#             st.error("⚠️ Speech recognition service error.")
#     return None

# # --- Language Map for TTS ---
# lang_codes = {
#     "English": "en",
#     "Hindi": "hi",
#     "Bengali": "bn",
#     "French": "fr",
#     "Spanish": "es",
#     "German": "de",
#     "Japanese": "ja",
#     "Korean": "ko",
#     "Russian": "ru",
#     "Chinese": "zh-cn"
# }

# langs = ["Auto"] + list(lang_codes.keys())

# # --- Language Selection ---
# col1, col2 = st.columns(2)
# with col1:
#     src = st.selectbox("🌐 Source Language", langs, index=0)
# with col2:
#     dest = st.selectbox("🎯 Target Language", langs, index=2)

# # --- Input Area ---
# st.write("### 📝 Enter or Speak Text:")
# text = st.text_area("Type or speak here:", st.session_state['input_text'], height=120)

# # --- Microphone Input ---
# if st.button("🎤 Speak"):
#     spoken_text = recognize_speech()
#     if spoken_text:
#         st.session_state['input_text'] = spoken_text
#         st.rerun()

# # --- Translate Button ---
# if st.button("🔄 Translate"):
#     if not text.strip():
#         st.warning("⚠️ Please enter or speak some text first.")
#     else:
#         try:
#             # --- Translation ---
#             translated = GoogleTranslator(source=src if src != "Auto" else "auto",
#                                           target=dest.lower()).translate(text)

#             st.subheader("🌍 Translation Result")

#             # --- Original Text + Audio ---
#             st.markdown("**Original Text:**")
#             st.info(text)

#             src_code = lang_codes.get(src, "en")
#             tts_input = gTTS(text=text, lang=src_code)
#             input_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#             tts_input.save(input_audio.name)
#             st.caption("🔊 Original text audio:")
#             st.audio(input_audio.name, format="audio/mp3")

#             # --- Translated Text + Audio ---
#             st.markdown("**Translated Text:**")
#             st.success(translated)

#             dest_code = lang_codes.get(dest, "en")
#             tts_output = gTTS(text=translated, lang=dest_code)
#             output_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#             tts_output.save(output_audio.name)
#             st.caption("🎧 Translated text audio:")
#             st.audio(output_audio.name, format="audio/mp3")

#             # --- Save to History ---
#             st.session_state['history'].append({
#                 "original": text,
#                 "translated": translated,
#                 "source": src.upper(),
#                 "target": dest.upper(),
#                 "original_audio": input_audio.name,
#                 "translated_audio": output_audio.name
#             })

#         except Exception as e:
#             st.error(f"❌ Error: {str(e)}")

# st.markdown("---")

# # --- Translation History ---
# if st.session_state['history']:
#     st.markdown("<h2>🕘 Translation History</h2>", unsafe_allow_html=True)
#     for idx, item in enumerate(reversed(st.session_state['history']), start=1):
#         with st.expander(f"{idx}. {item['source']} → {item['target']} : “{item['original'][:40]}...”"):
#             st.markdown(f"**Original ({item['source']}):** {item['original']}")
#             st.audio(item['original_audio'], format="audio/mp3")
#             st.markdown(f"**Translated ({item['target']}):** {item['translated']}")
#             st.audio(item['translated_audio'], format="audio/mp3")

# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align:center; color:#00A884;'>🌟 Created by <b>Shibnath Sahoo</b> | AI Voice Translator 🌐</h3>", unsafe_allow_html=True)


# import streamlit as st
# from deep_translator import GoogleTranslator
# from gtts import gTTS
# import speech_recognition as sr
# import tempfile

# # --- Streamlit Page Config ---
# st.set_page_config(page_title="🎧 AI Voice Translator", page_icon="🌍", layout="centered")

# # --- App Header ---
# st.markdown("<h1 style='text-align:center;'>🎙️ AI Voice Translator with Audio & History</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; color:gray;'>Developed by <b>Shibnath Sahoo</b> | Speak or type → Translate → Listen 🔊</p>", unsafe_allow_html=True)
# st.markdown("---")

# # --- Initialize Session State ---
# if 'history' not in st.session_state:
#     st.session_state['history'] = []
# if 'input_text' not in st.session_state:
#     st.session_state['input_text'] = ""

# # --- Supported Languages ---
# languages = {
#     "English": {"translator": "english", "tts": "en", "speech": "en-IN"},
#     "Hindi": {"translator": "hindi", "tts": "hi", "speech": "hi-IN"},
#     "Bengali": {"translator": "bengali", "tts": "bn", "speech": "bn-IN"},
#     "French": {"translator": "french", "tts": "fr", "speech": "fr-FR"},
#     "Spanish": {"translator": "spanish", "tts": "es", "speech": "es-ES"},
#     "German": {"translator": "german", "tts": "de", "speech": "de-DE"},
#     "Japanese": {"translator": "japanese", "tts": "ja", "speech": "ja-JP"},
#     "Korean": {"translator": "korean", "tts": "ko", "speech": "ko-KR"},
#     "Russian": {"translator": "russian", "tts": "ru", "speech": "ru-RU"},
#     "Chinese": {"translator": "chinese (simplified)", "tts": "zh-CN", "speech": "zh-CN"},
#     "Tamil": {"translator": "tamil", "tts": "ta", "speech": "ta-IN"},
#     "Telugu": {"translator": "telugu", "tts": "te", "speech": "te-IN"},
#     "Urdu": {"translator": "urdu", "tts": "ur", "speech": "ur-IN"},
#     "Arabic": {"translator": "arabic", "tts": "ar", "speech": "ar-SA"},
#     "Italian": {"translator": "italian", "tts": "it", "speech": "it-IT"}
# }

# langs = ["Auto"] + list(languages.keys())

# # --- Language Selection ---
# col1, col2 = st.columns(2)
# with col1:
#     src = st.selectbox("🌐 Source Language", langs, index=0)
# with col2:
#     dest = st.selectbox("🎯 Target Language", langs, index=2)

# # --- Function: Speech Recognition ---
# def recognize_speech(language_code="en-IN"):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info(f"🎤 Listening... (Speak in {language_code.split('-')[0].upper()}, up to 5 seconds)")
#         audio = recognizer.listen(source, phrase_time_limit=5)
#         try:
#             text = recognizer.recognize_google(audio, language=language_code)
#             st.success(f"✅ You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             st.error("❌ Could not understand your voice.")
#         except sr.RequestError:
#             st.error("⚠️ Speech recognition service error.")
#     return None

# # --- Input Area ---
# st.write("### 📝 Enter or Speak Text:")
# text = st.text_area("Type or speak here:", st.session_state['input_text'], height=120)

# # --- Microphone Input ---
# if st.button("🎤 Speak"):
#     # choose the speech recognition language based on selected src
#     if src == "Auto":
#         speech_code = "en-IN"  # default English
#     else:
#         speech_code = languages[src]["speech"]

#     spoken_text = recognize_speech(language_code=speech_code)
#     if spoken_text:
#         st.session_state['input_text'] = spoken_text
#         st.rerun()

# # --- Translate Button ---
# if st.button("🔄 Translate"):
#     if not text.strip():
#         st.warning("⚠️ Please enter or speak some text first.")
#     else:
#         try:
#             # --- Setup Language Codes ---
#             src_translator = "auto" if src == "Auto" else languages[src]["translator"]
#             dest_translator = languages[dest]["translator"]
#             src_tts = "en" if src == "Auto" else languages[src]["tts"]
#             dest_tts = languages[dest]["tts"]

#             # --- Translate ---
#             translated = GoogleTranslator(source=src_translator, target=dest_translator).translate(text)

#             st.subheader("🌍 Translation Result")

#             # --- Original Text & Audio ---
#             st.markdown("**Original Text:**")
#             st.info(text)

#             tts_input = gTTS(text=text, lang=src_tts)
#             input_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#             tts_input.save(input_audio.name)
#             st.caption("🔊 Original text audio:")
#             st.audio(input_audio.name, format="audio/mp3")

#             # --- Translated Text & Audio ---
#             st.markdown("**Translated Text:**")
#             st.success(translated)

#             tts_output = gTTS(text=translated, lang=dest_tts)
#             output_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#             tts_output.save(output_audio.name)
#             st.caption("🎧 Translated text audio:")
#             st.audio(output_audio.name, format="audio/mp3")

#             # --- Save to History ---
#             st.session_state['history'].append({
#                 "original": text,
#                 "translated": translated,
#                 "source": src.upper(),
#                 "target": dest.upper(),
#                 "original_audio": input_audio.name,
#                 "translated_audio": output_audio.name
#             })

#         except Exception as e:
#             st.error(f"❌ Error: {str(e)}")

# st.markdown("---")

# # --- Translation History ---
# if st.session_state['history']:
#     st.markdown("<h2>🕘 Translation History</h2>", unsafe_allow_html=True)
#     for idx, item in enumerate(reversed(st.session_state['history']), start=1):
#         with st.expander(f"{idx}. {item['source']} → {item['target']} : “{item['original'][:40]}...”"):
#             st.markdown(f"**Original ({item['source']}):** {item['original']}")
#             st.audio(item['original_audio'], format="audio/mp3")
#             st.markdown(f"**Translated ({item['target']}):** {item['translated']}")
#             st.audio(item['translated_audio'], format="audio/mp3")

# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align:center; color:#00A884;'>🌟 Created by <b>Shibnath Sahoo</b> | AI Voice Translator 🌐</h3>", unsafe_allow_html=True)



import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import speech_recognition as sr
import tempfile

# --- Streamlit Page Config ---
st.set_page_config(page_title="🎧 AI Voice Translator", page_icon="🌍", layout="centered")

# --- App Header ---
st.markdown("<h1 style='text-align:center;'>🎙️ AI Voice and LanguageTranslator with Audio & History</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Developed by <b>Shibnath Sahoo</b> | Speak or type → Translate → Listen 🔊</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Initialize Session State ---
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'input_text' not in st.session_state:
    st.session_state['input_text'] = ""

# --- Supported Languages ---
languages = {
    "English": {"translator": "english", "tts": "en", "speech": "en-IN"},
    "Hindi": {"translator": "hindi", "tts": "hi", "speech": "hi-IN"},
    "Bengali": {"translator": "bengali", "tts": "bn", "speech": "bn-IN"},
    "French": {"translator": "french", "tts": "fr", "speech": "fr-FR"},
    "Spanish": {"translator": "spanish", "tts": "es", "speech": "es-ES"},
    "German": {"translator": "german", "tts": "de", "speech": "de-DE"},
    "Japanese": {"translator": "japanese", "tts": "ja", "speech": "ja-JP"},
    "Korean": {"translator": "korean", "tts": "ko", "speech": "ko-KR"},
    "Russian": {"translator": "russian", "tts": "ru", "speech": "ru-RU"},
    "Chinese": {"translator": "chinese (simplified)", "tts": "zh-CN", "speech": "zh-CN"},
    "Tamil": {"translator": "tamil", "tts": "ta", "speech": "ta-IN"},
    "Telugu": {"translator": "telugu", "tts": "te", "speech": "te-IN"},
    "Urdu": {"translator": "urdu", "tts": "ur", "speech": "ur-IN"},
    "Arabic": {"translator": "arabic", "tts": "ar", "speech": "ar-SA"},
    "Italian": {"translator": "italian", "tts": "it", "speech": "it-IT"}
}

langs = ["Auto"] + list(languages.keys())

# --- Language Selection ---
col1, col2 = st.columns(2)
with col1:
    src = st.selectbox("🌐 Source Language", langs, index=0)
with col2:
    dest = st.selectbox("🎯 Target Language", langs, index=2)

# --- Function: Speech Recognition ---
def recognize_speech(language_code="en-IN"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info(f"🎤 Listening... (Speak in {language_code.split('-')[0].upper()}, up to 5 seconds)")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio, language=language_code)
            st.success(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("❌ Could not understand your voice.")
        except sr.RequestError:
            st.error("⚠️ Speech recognition service error.")
    return None

# --- Input Area ---
st.write("### 📝 Enter or Speak Text:")
text = st.text_area("Type or speak here:", st.session_state['input_text'], height=120)

# --- Microphone Input ---
if st.button("🎤 Speak"):
    # choose the speech recognition language based on selected src
    if src == "Auto":
        speech_code = "en-IN"  # default English
    else:
        speech_code = languages[src]["speech"]

    spoken_text = recognize_speech(language_code=speech_code)
    if spoken_text:
        st.session_state['input_text'] = spoken_text
        st.rerun()

# --- Translate Button ---
if st.button("🔄 Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter or speak some text first.")
    else:
        try:
            # --- Setup Language Codes ---
            src_translator = "auto" if src == "Auto" else languages[src]["translator"]
            dest_translator = languages[dest]["translator"]
            src_tts = "en" if src == "Auto" else languages[src]["tts"]
            dest_tts = languages[dest]["tts"]

            # --- Translate ---
            translated = GoogleTranslator(source=src_translator, target=dest_translator).translate(text)

            st.subheader("🌍 Translation Result")

            # --- Original Text & Audio ---
            st.markdown("**Original Text:**")
            st.info(text)

            tts_input = gTTS(text=text, lang=src_tts)
            input_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts_input.save(input_audio.name)
            st.caption("🔊 Original text audio:")
            st.audio(input_audio.name, format="audio/mp3")

            # --- Translated Text & Audio ---
            st.markdown("**Translated Text:**")
            st.success(translated)

            tts_output = gTTS(text=translated, lang=dest_tts)
            output_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts_output.save(output_audio.name)
            st.caption("🎧 Translated text audio:")
            st.audio(output_audio.name, format="audio/mp3")

            # --- Save to History ---
            st.session_state['history'].append({
                "original": text,
                "translated": translated,
                "source": src.upper(),
                "target": dest.upper(),
                "original_audio": input_audio.name,
                "translated_audio": output_audio.name
            })

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

st.markdown("---")

# --- Translation History ---
if st.session_state['history']:
    st.markdown("<h2>🕘 Translation History</h2>", unsafe_allow_html=True)
    for idx, item in enumerate(reversed(st.session_state['history']), start=1):
        with st.expander(f"{idx}. {item['source']} → {item['target']} : “{item['original'][:40]}...”"):
            st.markdown(f"**Original ({item['source']}):** {item['original']}")
            st.audio(item['original_audio'], format="audio/mp3")
            st.markdown(f"**Translated ({item['target']}):** {item['translated']}")
            st.audio(item['translated_audio'], format="audio/mp3")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#00A884;'>🌟 Created by <b>Shibnath Sahoo</b> | AI Voice Translator 🌐</h3>", unsafe_allow_html=True)
