import re
import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SECTIONS = ["summary", "education", "experience", "projects", "skills", "certifications"]


def read_pdf(file):
    return " ".join(page.extract_text() or "" for page in PdfReader(file).pages)


def match_score(resume, jd):
    matrix = TfidfVectorizer(stop_words="english").fit_transform([resume, jd])
    return round(cosine_similarity(matrix[0], matrix[1])[0][0] * 100)


def top_keywords(text, n=25):
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=n)
    vec.fit([text])
    return set(vec.get_feature_names_out())


def checks(text):
    low = text.lower()
    return {
        "Email": bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text)),
        "Phone": bool(re.search(r"\+?\d[\d\s-]{8,}\d", text)),
        "LinkedIn": "linkedin.com" in low,
        "GitHub": "github.com" in low,
        "Length (300-900 words)": 300 <= len(text.split()) <= 900,
    }


st.set_page_config(page_title="Smart Resume Analyzer", page_icon="📄", layout="wide")
st.title("📄 Smart Resume Analyzer")
st.caption("Upload your resume, paste a job description, and see how well they match.")

left, right = st.columns(2)
file = left.file_uploader("Resume (PDF)", type="pdf")
jd = right.text_area("Job description", height=220)

if file and jd.strip():
    resume = read_pdf(file)
    score = match_score(resume, jd)
    wanted = top_keywords(jd)
    low = resume.lower()
    found = sorted(k for k in wanted if k in low)
    missing = sorted(wanted - set(found))

    st.divider()
    a, b = st.columns([1, 2])
    a.metric("Match score", f"{score}%")
    b.progress(score / 100)
    if score >= 70:
        b.success("Strong match")
    elif score >= 40:
        b.warning("Decent match, add the missing keywords")
    else:
        b.error("Weak match, tailor your resume to this role")

    c, d = st.columns(2)
    c.subheader("✅ Keywords found")
    c.write(", ".join(found) or "None")
    d.subheader("❌ Keywords missing")
    d.write(", ".join(missing) or "None")

    e, f = st.columns(2)
    e.subheader("Sections")
    for s in SECTIONS:
        e.write(("✅ " if s in low else "❌ ") + s.title())
    f.subheader("Quick checks")
    for name, ok in checks(resume).items():
        f.write(("✅ " if ok else "❌ ") + name)
else:
    st.info("Add both a resume and a job description to get started.")
