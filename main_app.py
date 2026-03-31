# main_app.py — Smart City Assistant (Streamlit-based)
import streamlit as st
from utils.feedback_handler import handle_feedback
from utils.doc_summarizer import summarize_document
from utils.eco_advisor import eco_advice
from utils.sensor_dashboard import get_city_metrics

st.set_page_config(page_title="Smart City 360°", layout="wide")

st.title("🏙️ Smart City 360° Assistant")
st.markdown("Use the tabs below to interact with various smart city modules.")

# ---------- Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 City Health Dashboard",
    "🗣️ Citizen Feedback System",
    "📄 Document Summarization",
    "🌿 Eco Advice Assistant"
])

# ----- TAB 1: Sensor Dashboard -----
with tab1:
    st.subheader("📊 Real-Time Metrics")
    if st.button("Refresh Metrics"):
        metrics = get_city_metrics()
        st.text_area("City Metrics", metrics, height=300)

# ----- TAB 2: Feedback -----
with tab2:
    st.subheader("🗣️ Report a City Issue")
    issue = st.text_area("Describe the issue here (e.g. water leak, traffic jam)...")
    if st.button("Submit Feedback"):
        result = handle_feedback(issue)
        st.success("Feedback Processed:")
        st.write(result)

# ----- TAB 3: Document Summarization -----
with tab3:
    st.subheader("📄 Summarize a City Document")
    uploaded_file = st.file_uploader("Upload a PDF or text file", type=["pdf", "txt"])
    if uploaded_file and st.button("Summarize"):
        summary = summarize_document(uploaded_file)
        st.success("Summary:")
        st.write(summary)

# ----- TAB 4: Eco Advice -----
with tab4:
    st.subheader("🌿 Get Eco-friendly Suggestions")
    query = st.text_input("Ask something like 'How can I save electricity at home?'")
    if st.button("Get Eco Advice"):
        tips = eco_advice(query)
        st.success("Eco Advice:")
        st.write(tips)
