import streamlit as st
from transformers import pipeline

# ---------------- LOAD MODELS ---------------- #

@st.cache_resource
def load_models():
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return qa_pipeline, summarizer

qa_pipeline, summarizer = load_models()

# ---------------- UI ---------------- #

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume → Get summary, skills & suggestions")

uploaded_file = st.file_uploader("Upload Resume (.txt only)", type=["txt"])

# ---------------- FUNCTION ---------------- #

def analyze_resume(text):
    text = text[:1500]

    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

    skills_prompt = f"List key skills from this resume:\n{text}"
    skills = qa_pipeline(skills_prompt, max_length=100)[0]['generated_text']

    suggestion_prompt = f"Give improvement suggestions for this resume:\n{text}"
    suggestions = qa_pipeline(suggestion_prompt, max_length=120)[0]['generated_text']

    return summary, skills, suggestions

# ---------------- BUTTON ---------------- #

if uploaded_file is not None:
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing..."):
            text = uploaded_file.read().decode("utf-8")

            summary, skills, suggestions = analyze_resume(text)

            st.subheader("📄 Summary")
            st.write(summary)

            st.subheader("💡 Skills")
            st.write(skills)

            st.subheader("📊 Suggestions")
            st.write(suggestions)
