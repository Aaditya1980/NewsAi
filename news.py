import streamlit as st
import requests

st.set_page_config(page_title="🗞️ News AI", layout="wide")

st.title("🗞️ News AI - India Edition")
st.write("Stay informed with top news from Indian sources.")


st.sidebar.header("⚙️ News Settings")
language = st.sidebar.selectbox("🈯 Choose Language", ["English", "Hindi"])
category = st.sidebar.selectbox(
    "🗂️ Select Category",
    ["top", "world", "nation", "business", "technology", "entertainment", "sports", "science", "health"]
)


api_key = "1c7ab4fa13fc0a1caee22f7762b15fe2"
api_url = f"https://gnews.io/api/v4/top-headlines?lang={language}&topic={category}&country=in&max=10&apikey={api_key}"


response = requests.get(api_url)
data = response.json()

if "articles" in data:
    for article in data["articles"]:
        st.markdown("----")
        st.subheader(article["title"])
        st.caption(article["publishedAt"])

        if article.get("image"):
            st.image(article["image"], width=500)

        st.write(article["description"] or "No description available.")
        st.markdown(f"[🔗 Read full article]({article['url']})")
else:
    st.error("Failed to fetch news articles.")



linkedin_username = "aadityagoyal80"
email_id = "aadityagoyal80@gmail.com"

st.markdown("---")
st.markdown(
    f"""
    <div style="text-align:center; font-size:16px; padding: 10px;">
        <b>Made by Aaditya Goyal</b><br>
        📧 <a href="mailto:{email_id}">{email_id}</a> <br>
        🔗 <a href="https://www.linkedin.com/in/{linkedin_username}" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
