import streamlit as st
import requests
import PyPDF2

# ---------------- CONFIG ---------------- #

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
    "Content-Type": "application/json"
}

# ---------------- FUNCTIONS ---------------- #

def query(prompt):
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        # If still HTML error → catch it
        if "text/html" in response.headers.get("content-type", ""):
            return {"error": "API endpoint blocked or incorrect."}

        result = response.json()

        if isinstance(result, dict) and "error" in result:
            return {"error": result["error"]}

        return result

    except Exception as e:
        return {"error": str(e)}


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def analyze_resume(text):
    text = text[:1500]

    summary = query(f"Summarize this resume:\n{text}")
    skills = query(f"Extract key skills from this resume:\n{text}")
    suggestions = query(f"Give improvement suggestions for this resume:\n{text}")

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
st.markdown("Upload your resume and get smart insights")

uploaded_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])

if st.button("🚀 Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume first!")
    else:
        with st.spinner("Analyzing..."):

            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            else:
                text = uploaded_file.read().decode("utf-8")

            summary, skills, suggestions = analyze_resume(text)

            st.subheader("📄 Summary")
            st.write(extract_output(summary))

            st.subheader("💡 Skills")
            st.write(extract_output(skills))

            st.subheader("📊 Suggestions")
            st.write(extract_output(suggestions))

            st.success("Analysis complete!")