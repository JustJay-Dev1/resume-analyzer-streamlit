import streamlit as st
import requests
import PyPDF2
import time

# ---------------- CONFIG ---------------- #

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-small"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
}

# ---------------- FUNCTIONS ---------------- #

def query(payload):
    for _ in range(3):  # retry 3 times
        response = requests.post(API_URL, headers=headers, json=payload)

        # Try parsing JSON safely
        try:
            result = response.json()
        except:
            return {"error": response.text}

        # Handle model loading case
        if isinstance(result, dict) and "error" in result:
            if "loading" in result["error"].lower():
                time.sleep(5)
                continue
            return {"error": result["error"]}

        return result

    return {"error": "Model is still loading. Please try again."}


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def analyze_resume(text):
    text = text[:1500]

    summary = query({
        "inputs": f"Summarize this resume:\n{text}"
    })

    skills = query({
        "inputs": f"Extract key skills from this resume:\n{text}"
    })

    suggestions = query({
        "inputs": f"Give improvement suggestions for this resume:\n{text}"
    })

    return summary, skills, suggestions


def extract_output(res):
    if isinstance(res, dict) and "error" in res:
        return f"⚠️ {res['error']}"

    if isinstance(res, list):
        return res[0].get("generated_text", str(res))

    return str(res)


# ---------------- UI ---------------- #

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.markdown("### Upload your resume and get smart insights")

uploaded_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])

analyze_btn = st.button("🚀 Analyze Resume")

# Output placeholders
summary_box = st.empty()
skills_box = st.empty()
suggestions_box = st.empty()

if analyze_btn:

    if uploaded_file is None:
        st.warning("⚠️ Please upload a resume first!")
    else:
        with st.spinner("Analyzing..."):

            # Read file
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            else:
                text = uploaded_file.read().decode("utf-8")

            # Analyze
            summary, skills, suggestions = analyze_resume(text)

            # Display results
            summary_box.subheader("📄 Summary")
            summary_box.write(extract_output(summary))

            skills_box.subheader("💡 Skills")
            skills_box.write(extract_output(skills))

            suggestions_box.subheader("📊 Suggestions")
            suggestions_box.write(extract_output(suggestions))

            st.success("✅ Analysis complete!")