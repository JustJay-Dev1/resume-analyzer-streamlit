# 📄 AI Resume Analyzer (Cloud-Based)

## 🚀 Project Overview

The **AI Resume Analyzer** is a cloud-based web application that allows users to upload resumes (in `.txt` or `.pdf` format) and receive intelligent insights such as:

* 📄 Resume Summary
* 💡 Extracted Key Skills
* 📊 Improvement Suggestions

The application uses **Large Language Models (LLMs)** via cloud APIs to analyze resume content and generate meaningful feedback.

---

## ☁️ Why This is a Cloud Computing Project

This project is built using **cloud computing principles**, where all processing is performed remotely using cloud services instead of local computation.

### 🔹 Cloud Concepts Used

* **Cloud Deployment**
  The application is hosted on **Streamlit Cloud**, making it accessible globally via a browser.

* **API-Based Inference (Cloud AI)**
  Resume analysis is performed using the **OpenRouter API**, which provides access to LLMs hosted in the cloud.

* **On-Demand Resource Usage**
  Compute resources are used only when a user interacts with the system.

* **Scalability**
  Multiple users can access the system simultaneously without installing any software.

* **Platform Independence**
  Works on any device (laptop, mobile, tablet) with internet access.

---

## 🧠 Technologies Used

### 🔹 Frontend

* Streamlit (Python-based UI framework)

### 🔹 Backend

* Python

### 🔹 AI / NLP

* OpenRouter API (LLM inference)
* Model used: `meta-llama/llama-3-8b-instruct` 

### 🔹 File Processing

* PyPDF2 (for PDF text extraction)

### 🔹 Cloud Platform

* Streamlit Cloud (deployment & hosting)

---

## 🏗️ System Architecture

```text
User Uploads Resume
        ↓
Streamlit Web App (Cloud)
        ↓
Text Extraction (PDF/TXT)
        ↓
OpenRouter API (LLM Processing)
        ↓
Generated Output
(Summary, Skills, Suggestions)
```

---

## ⚙️ Features

* 📄 Upload resume in `.txt` or `.pdf`
* 📝 Automatic resume summarization
* 💡 Key skills extraction
* 📊 Resume improvement suggestions
* ☁️ Fully cloud-based access

---

## 📦 Installation (Local Setup)

1. Clone the repository:

```bash
git clone https://github.com/JustJay-Dev1/resume-analyzer-streamlit.git
cd resume-analyzer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add API key:
   Create `.streamlit/secrets.toml`

```toml
OPENROUTER_API_KEY = "your_api_key"
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed on **Streamlit Cloud**, which provides:

* Free cloud hosting
* Automatic deployment from GitHub
* Public access via URL

---

## 📊 Advantages of Cloud-Based Approach

* No local installation required
* Lightweight application (no heavy models)
* Faster deployment and updates
* Scalable and accessible
* Efficient resource usage

---

## ⚠️ Limitations

* Requires internet connection
* API response depends on model availability
* Free API usage may have rate limits
* PDF parsing may not work for scanned documents

---

## 🔮 Future Enhancements

* 📊 ATS Score calculation
* 🎯 Job-role based analysis
* 📄 Support for DOCX files
* 📈 Resume ranking system
* 🎨 Enhanced UI/UX

---

## 👨‍💻 Author

**Jayesh Jachak**

---

## 🎯 Conclusion

This project demonstrates how **cloud computing and AI can be integrated** to build intelligent, scalable applications.
By using **API-based model inference**, the system avoids heavy local computation while delivering powerful AI-driven insights.

---
