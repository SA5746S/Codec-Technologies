# 🎭 Twitter Sentiment Analysis using NLTK (VADER)
# Author: Shibnath Sahoo

import streamlit as st
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Streamlit Page Setup ----
st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon="🎭", layout="wide")

# ---- App Heading ----
st.markdown("""
    <h1 style='text-align:center; color:#3B82F6;'>🎭 Twitter Sentiment Analysis</h1>
    <h3 style='text-align:center; color:#10B981;'>By <b>Shibnath Sahoo</b></h3>
    <p style='text-align:center; font-size:16px;'>Analyze tweets and classify them as Positive, Negative, or Neutral using NLP (VADER Sentiment Analyzer)</p>
    <hr>
""", unsafe_allow_html=True)

# ---- NLTK Setup ----
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# ---- Function: Clean Tweet ----
def clean_tweet(text):
    text = re.sub(r'http\S+', '', text)          # remove URLs
    text = re.sub(r'@\w+', '', text)             # remove mentions
    text = re.sub(r'#', '', text)                # remove hashtags
    text = re.sub(r'[^A-Za-z\s]', '', text)      # remove non-alphabetic
    text = text.lower().strip()
    return text

# ---- Function: Get Sentiment ----
def get_sentiment(text):
    score = sia.polarity_scores(text)
    if score['compound'] > 0.05:
        return 'Positive'
    elif score['compound'] < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# ---- Sidebar ----
st.sidebar.header("📥 Input Options")
option = st.sidebar.radio("Choose Input Type:", ["Enter Tweets Manually", "Upload CSV File"])

# ---- Option 1: Manual Input ----
if option == "Enter Tweets Manually":
    tweet_input = st.text_area("✍️ Enter one or more tweets (separated by new lines):")
    if st.button("Analyze Tweets"):
        if tweet_input.strip():
            tweets = tweet_input.strip().split("\n")
            df = pd.DataFrame(tweets, columns=["tweet"])
            df["clean_tweet"] = df["tweet"].apply(clean_tweet)
            df["sentiment"] = df["clean_tweet"].apply(get_sentiment)

            st.subheader("🧾 Sentiment Results")
            st.dataframe(df, use_container_width=True)

            # Visualization
            st.subheader("📊 Sentiment Distribution")
            fig, ax = plt.subplots()
            sns.countplot(x="sentiment", data=df, palette="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Please enter at least one tweet.")

# ---- Option 2: CSV Upload ----
else:
    uploaded_file = st.file_uploader("📂 Upload a CSV file containing a column named 'tweet'")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "tweet" not in df.columns:
            st.error("❌ CSV must contain a column named 'tweet'.")
        else:
            df["clean_tweet"] = df["tweet"].apply(clean_tweet)
            df["sentiment"] = df["clean_tweet"].apply(get_sentiment)

            st.subheader("🧾 Sentiment Results")
            st.dataframe(df.head(20), use_container_width=True)

            # Visualization
            st.subheader("📊 Sentiment Distribution")
            fig, ax = plt.subplots()
            sns.countplot(x="sentiment", data=df, palette="viridis", ax=ax)
            st.pyplot(fig)

            # Download option
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="sentiment_analysis_results.csv",
                mime="text/csv",
            )

# ---- Footer ----
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:14px;'>Made with ❤️ by <b>Shibnath Sahoo</b> | NLP + Streamlit</p>",
    unsafe_allow_html=True
)


# 🎭 Twitter Sentiment Analysis using NLTK (VADER)
# Author: Shibnath Sahoo

# import streamlit as st
# import pandas as pd
# import re
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import matplotlib.pyplot as plt
# import seaborn as sns

# # ---- Streamlit Page Setup ----
# st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon="🎭", layout="wide")

# # ---- App Heading ----
# st.markdown("""
#     <h1 style='text-align:center; color:#3B82F6;'>🎭 Twitter Sentiment Analysis</h1>
#     <h3 style='text-align:center; color:#10B981;'>By <b>Shibnath Sahoo</b></h3>
#     <p style='text-align:center; font-size:16px;'>Analyze tweets and classify them as Positive, Negative, or Neutral using NLP (VADER Sentiment Analyzer)</p>
#     <hr>
# """, unsafe_allow_html=True)

# # ---- NLTK Setup ----
# nltk.download('vader_lexicon', quiet=True)
# sia = SentimentIntensityAnalyzer()

# # ---- Function: Clean Tweet ----
# def clean_tweet(text):
#     text = re.sub(r'http\S+', '', text)          # remove URLs
#     text = re.sub(r'@\w+', '', text)             # remove mentions
#     text = re.sub(r'#', '', text)                # remove hashtags
#     text = re.sub(r'[^A-Za-z\s]', '', text)      # remove non-alphabetic
#     text = text.lower().strip()
#     return text

# # ---- Function: Get Sentiment ----
# def get_sentiment(text):
#     score = sia.polarity_scores(text)
#     if score['compound'] > 0.05:
#         return 'Positive'
#     elif score['compound'] < -0.05:
#         return 'Negative'
#     else:
#         return 'Neutral'

# # ---- Sidebar ----
# st.sidebar.header("📥 Input Options")
# option = st.sidebar.radio("Choose Input Type:", ["Enter Tweets Manually", "Upload CSV File"])

# # ---- Option 1: Manual Input ----
# if option == "Enter Tweets Manually":
#     tweet_input = st.text_area("✍️ Enter one or more tweets (separated by new lines):")
#     if st.button("Analyze Tweets"):
#         if tweet_input.strip():
#             tweets = tweet_input.strip().split("\n")
#             df = pd.DataFrame(tweets, columns=["tweet"])
#             df["clean_tweet"] = df["tweet"].apply(clean_tweet)
#             df["sentiment"] = df["clean_tweet"].apply(get_sentiment)

#             st.subheader("🧾 Sentiment Results")
#             st.dataframe(df, use_container_width=True)

#             # Visualization
#             st.subheader("📊 Sentiment Distribution")
#             fig, ax = plt.subplots()
#             sns.countplot(x="sentiment", data=df, palette="coolwarm", ax=ax)
#             st.pyplot(fig)
#         else:
#             st.warning("Please enter at least one tweet.")

# # ---- Option 2: CSV Upload ----
# else:
#     uploaded_file = st.file_uploader("📂 Upload a CSV file containing a column named 'tweet'")
#     if uploaded_file:
#         try:
#             # ✅ FIXED: handles commas, quotes, and bad lines automatically
#             df = pd.read_csv(uploaded_file, engine='python', quoting=3, on_bad_lines='skip')
#         except Exception as e:
#             st.error(f"Error reading CSV: {e}")
#             st.stop()

#         if "tweet" not in df.columns:
#             st.error("❌ CSV must contain a column named 'tweet'.")
#         else:
#             df["clean_tweet"] = df["tweet"].apply(clean_tweet)
#             df["sentiment"] = df["clean_tweet"].apply(get_sentiment)

#             st.subheader("🧾 Sentiment Results")
#             st.dataframe(df.head(20), use_container_width=True)

#             # Visualization
#             st.subheader("📊 Sentiment Distribution")
#             fig, ax = plt.subplots()
#             sns.countplot(x="sentiment", data=df, palette="viridis", ax=ax)
#             st.pyplot(fig)

#             # Download option
#             csv = df.to_csv(index=False).encode('utf-8')
#             st.download_button(
#                 label="📥 Download Results as CSV",
#                 data=csv,
#                 file_name="sentiment_analysis_results.csv",
#                 mime="text/csv",
#             )

# # ---- Footer ----
# st.markdown("---")
# st.markdown(
#     "<p style='text-align:center; font-size:14px;'>Made with ❤️ by <b>Shibnath Sahoo</b> | NLP + Streamlit</p>",
#     unsafe_allow_html=True
# )
