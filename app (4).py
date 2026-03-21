
import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

st.title("📄 Resume Screening App")

job_description = st.text_area("Enter Job Description")
resume_text = st.text_area("Enter Resume Text")

if st.button("Calculate Similarity"):
    if job_description and resume_text:
        job_vec = vectorizer.transform([job_description])
        resume_vec = vectorizer.transform([resume_text])
        score = cosine_similarity(job_vec, resume_vec)[0][0]
        st.success(f"Similarity Score: {score:.2f}")
    else:
        st.warning("Please enter both job description and resume text.")
