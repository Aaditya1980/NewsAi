import streamlit as st
import feedparser

st.set_page_config(page_title="🗞️ News AI", layout="wide")
st.title("🗞️ News AI - India Edition")
st.write("Stay informed with top news from Indian sources.")

# RSS feed sources
rss_feeds = {
    "🗞️ Times of India": "https://timesofindia.indiatimes.com/rssfeeds/1221656.cms",
    "🟣 NDTV": "https://feeds.feedburner.com/ndtvnews-top-stories",
    "🟢 Hindustan Times": "https://www.hindustantimes.com/rss/topnews/rssfeed.xml"
}

# Sidebar for source selection
choice = st.sidebar.selectbox("📡 Choose News Source", list(rss_feeds.keys()))
feed_url = rss_feeds[choice]

# Parse feed
feed = feedparser.parse(feed_url)

# Function to strip basic HTML tags manually
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

# Show top 10 articles
for entry in feed.entries[:10]:
    st.markdown("----")
    st.subheader(entry.title)
    st.caption(entry.published)

    # Prefer description, fallback to summary
    desc = entry.get("description", "").strip()
    if len(desc) < 30:
        desc = entry.get("summary", "").strip()

    # Extract image if present
    image_url = ""
    if 'src="' in desc:
        try:
            part1 = desc.split('src="')[1]
            image_url = part1.split('"')[0]
            st.image(image_url, width=500)
        except:
            pass

    # Clean HTML from description
    cleaned_desc = clean_html(desc)

    # Show preview
    st.write(cleaned_desc)

    # Link to original article
    st.markdown(f"[🔗 Read full article]({entry.link})")
