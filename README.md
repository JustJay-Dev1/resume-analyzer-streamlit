# 📄 AI Resume Analyzer (Cloud-Based)

## 🚀 Project Overview

The **AI Resume Analyzer** is a cloud-based application that allows users to upload their resumes (in `.txt` or `.pdf` format) and receive intelligent insights such as:

* 📄 Summary of the resume
* 💡 Extracted key skills
* 📊 Improvement suggestions

The system uses **Natural Language Processing (NLP)** models to analyze resume content and provide meaningful feedback.

---

## ☁️ Why This is a Cloud Computing Project

This project is implemented using **cloud computing principles**, where all processing and hosting are performed remotely instead of on a local machine.

### 🔹 Cloud Features Used

* **Cloud Hosting**
  The application is deployed on a cloud platform (Streamlit Cloud), making it accessible from anywhere via a web browser.

* **Remote Processing**
  Resume analysis and NLP model execution happen on cloud servers instead of the user's device.

* **On-Demand Resource Usage**
  The application uses cloud resources (CPU, memory) only when a user interacts with it.

* **Scalability**
  Multiple users can access the system simultaneously without installing any software locally.

* **Platform Independence**
  Users can access the app from any device (laptop, mobile, tablet) without compatibility issues.

---

## 🧠 Technologies Used

### 🔹 Frontend

* Streamlit (Python-based UI framework)

### 🔹 Backend

* Python

### 🔹 Machine Learning / NLP

* Transformers (Hugging Face)
* Pre-trained models:

  * `google/flan-t5-small` (text generation)
  * `sshleifer/distilbart-cnn-12-6` (summarization)

### 🔹 File Processing

* PyPDF2 (for PDF text extraction)

### 🔹 Cloud Platform

* Streamlit Cloud (deployment & hosting)

---

## 🏗️ System Architecture

```
User Uploads Resume
        ↓
Streamlit Web Interface (Cloud)
        ↓
Text Extraction (PDF/TXT)
        ↓
NLP Model Processing
        ↓
Results Display (Summary, Skills, Suggestions)
```

---

## ⚙️ Features

* 📄 Upload resume in `.txt` or `.pdf`
* 📝 Automatic summarization
* 💡 Skill extraction
* 📊 Resume improvement suggestions
* ☁️ Fully cloud-based access

---

## 📦 Installation (Local Setup)

1. Clone the repository:

```
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed on **Streamlit Cloud**, which provides:

* Automatic deployment from GitHub
* Free cloud hosting
* Public access via URL

---

## 📊 Advantages of Cloud-Based Approach

* No installation required for users
* Centralized processing
* Easy updates and maintenance
* High availability
* Cost-efficient resource usage

---

## ⚠️ Limitations

* PDF parsing may fail for scanned/image-based resumes
* Model responses depend on input quality
* Large files are trimmed for performance

---

## 🔮 Future Enhancements

* 📊 ATS Score calculation
* 📄 Support for DOCX files
* 🎯 Job-role based analysis
* 📈 Resume ranking system
* 🧠 Improved AI models

---

## 👨‍💻 Author

**Jayesh Jachak**

---

## 🎯 Conclusion

The AI Resume Analyzer demonstrates how **cloud computing and AI can be combined** to build intelligent, scalable, and accessible applications.
It highlights the use of **cloud deployment, remote processing, and machine learning models** in a practical real-world scenario.

---
