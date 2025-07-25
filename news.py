import streamlit as st
import feedparser

st.set_page_config(page_title="🗞️ News AI", layout="wide")
st.title("🗞️ News AI - India Edition")
st.write("Stay informed with top news from Indian sources.")


rss_feeds = {
    "🗞️ Times of India": "https://timesofindia.indiatimes.com/rssfeeds/1221656.cms",
    "🟣 NDTV": "https://feeds.feedburner.com/ndtvnews-top-stories",
    "🟢 Hindustan Times": "https://www.hindustantimes.com/rss/topnews/rssfeed.xml"
}


choice = st.sidebar.selectbox("📡 Choose News Source", list(rss_feeds.keys()))
feed_url = rss_feeds[choice]


feed = feedparser.parse(feed_url)


def clean_html(raw_html):
    cleaned = ''
    skip = False
    for ch in raw_html:
        if ch == '<':
            skip = True
        elif ch == '>':
            skip = False
            continue
        if not skip:
            cleaned += ch
    return cleaned.strip()


for entry in feed.entries[:10]:
    st.markdown("----")
    st.subheader(entry.title)
    st.caption(entry.published)

   
    desc = entry.get("description", "").strip()
    if len(desc) < 30:
        desc = entry.get("summary", "").strip()


    image_url = ""
    if 'src="' in desc:
        try:
            part1 = desc.split('src="')[1]
            image_url = part1.split('"')[0]
            st.image(image_url, width=500)
        except:
            pass


    cleaned_desc = clean_html(desc)
    
    st.write(cleaned_desc)

   
    st.markdown(f"[🔗 Read full article]({entry.link})")

    st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray;'>
        Made with ❤️ by <b>Aaditya Goyal</b><br>
       📧 Email: <a href='mailto:aadityagoyal80@gmail.com'>aadityagoyal80@gmail.com</a><br>
        🔗 LinkedIn: <a href='https://www.linkedin.com/in/Aaditya Goyal/' target='_blank'>linkedin.com/in/Aaditya Goyal</a>
    </div>
    """,
    unsafe_allow_html=True
)


   
