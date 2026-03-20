# 📄 Resume Screening & Candidate Ranking System
🚀 This project was developed as part of the **Machine Learning Internship at Future Interns**.
This system automatically **screens, scores, and ranks resumes** based on a given job description using Natural Language Processing (NLP) techniques.
---

# 🎯 Project Objective
Recruiters receive hundreds of resumes for a single role, making manual screening inefficient.
This system helps to:
✅ Automatically analyze resumes  
✅ Match candidate skills with job requirements  
✅ Rank candidates based on relevance  
✅ Identify missing or weak skills  
---

# 🧠 How It Works
The system follows a complete NLP pipeline:
1️⃣ Resume text preprocessing  
2️⃣ Job description cleaning  
3️⃣ Feature extraction using **TF-IDF**  
4️⃣ Similarity scoring using **Cosine Similarity**  
5️⃣ Ranking candidates based on scores  
6️⃣ Identifying missing skills  
---

# 🛠️ Technologies Used
💻 Python  
📊 Pandas & NumPy  
🤖 Scikit-learn  
🧹 NLP (Text Cleaning & Processing)  
📓 Jupyter Notebook / Google Colab  
---

# 📂 Dataset
For this project, sample resume data was used, including:
- Resume text (skills, experience)
- Job description
This setup simulates real-world hiring scenarios.
---

# 🔍 Text Preprocessing
The following NLP steps were applied:
✔ Lowercasing text  
✔ Removing punctuation  
✔ Cleaning unstructured data  
---

# ⚙️ Feature Engineering
📌 **TF-IDF Vectorization** was used to convert text into numerical features.
This allows the system to understand the importance of words in resumes and job descriptions.
---

# 📊 Similarity Scoring
📌 **Cosine Similarity** is used to measure how closely a resume matches the job description.
Higher score = better match.
---

# 🏆 Candidate Ranking
Resumes are ranked based on similarity scores:
📈 Higher score → More relevant candidate  
📉 Lower score → Less relevant candidate  
---

**Results**
| Resume | Score (%) | Missing Skills |
|--------|----------|----------------|
| Python ML Data Analyst | 48.95 | science, deep |
| Python Deep Learning NLP | 41.89 | data, machine |
| SQL Data Analyst | 7.90 | python, deep, machine |
| Java Developer | 0.00 | python, data, machine |
---

# 🔍 Skill Gap Analysis
The system identifies missing skills by comparing:
📌 Resume keywords vs Job description keywords  
This helps recruiters understand **why a candidate is not a perfect match**.
---

# 🚀 Business Impact
This system helps organizations:
⚡ Automate resume screening  
⚡ Reduce recruiter workload  
⚡ Improve hiring efficiency  
⚡ Identify skill gaps quickly  
Such systems are widely used in **HR-tech platforms and recruitment systems**.
---

# 📁 Project Structure
FUTURE_ML_03
│
├── resume_screening.ipynb
├── README.md
├── output.png
---

# 🌐 Internship Program
This project was completed as part of the **Machine Learning Internship at Future Interns**.
---

# 📬 Connect With Me
💼 LinkedIn  
💻 GitHub  
---

⭐ If you found this project useful, consider giving it a star!
