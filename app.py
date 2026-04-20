import streamlit as st
from transformers import pipeline
import PyPDF2

# ---------------- LOAD MODELS ---------------- #

@st.cache_resource
def load_models():
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return qa_pipeline, summarizer

qa_pipeline, summarizer = load_models()

# ---------------- FUNCTIONS ---------------- #

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def analyze_resume(text):
    text = text[:1500]

    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

    skills_prompt = f"List key skills from this resume:\n{text}"
    skills = qa_pipeline(skills_prompt, max_length=100)[0]['generated_text']

    suggestion_prompt = f"Give improvement suggestions for this resume:\n{text}"
    suggestions = qa_pipeline(suggestion_prompt, max_length=120)[0]['generated_text']

    return summary, skills, suggestions

# ---------------- UI ---------------- #

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume (.txt or .pdf)")

uploaded_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])

if uploaded_file is not None:
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing..."):

            # Detect file type
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            else:
                text = uploaded_file.read().decode("utf-8")

            summary, skills, suggestions = analyze_resume(text)

            st.subheader("📄 Summary")
            st.write(summary)

            st.subheader("💡 Skills")
            st.write(skills)

            st.subheader("📊 Suggestions")
            st.write(suggestions)