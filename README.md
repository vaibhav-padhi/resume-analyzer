# 📄 Smart Resume Analyzer

Upload a resume, paste a job description, and instantly see how well they match.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF-F7931E?logo=scikitlearn&logoColor=white)

**[🚀 Live Demo](YOUR_STREAMLIT_LINK_HERE)**

![demo](demo.gif)

## Features
- Match score (0-100%) using TF-IDF and cosine similarity
- Keywords from the job description that your resume has and lacks
- Section check: summary, education, experience, projects, skills, certifications
- Quick checks: email, phone, LinkedIn, GitHub, resume length

## Run locally
```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
streamlit run app.py
```

## How it works
1. Extracts text from the PDF with `pypdf`
2. Vectorizes the resume and job description with TF-IDF
3. Scores them with cosine similarity
4. Pulls the top keywords from the job description and checks them against the resume

## What I learned
- Text processing and vectorization with scikit-learn
- Building and deploying a data app with Streamlit

## Roadmap
- [ ] DOCX support
- [ ] Skill suggestions per role
- [ ] Downloadable PDF report
