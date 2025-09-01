# 🤖 AI Coding Tutor Gen-AI

An **interactive AI-powered coding tutor** that explains coding concepts step by step with diagrams 🖼️ and quizzes ❓.

## 🚀 Features
- 📘 Step-by-step explanations of coding concepts
- 🖼️ Auto-generated diagrams using Graphviz
- 📝 Interactive quizzes with grading
- 💬 AI-powered Q&A tutor

## 📂 Project Structure
```
ai-coding-tutor-gen-ai/
│── .env.example
│── requirements.txt
│── README.md
│── streamlit_app.py
└── src/
    ├── __init__.py
    ├── config.py
    ├── tutor.py
    ├── diagrams.py
    ├── quiz.py
    └── utils.py
```

## ⚙️ Setup
1. Clone the repo & install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your API key in `.env` file.

3. Run Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## 💡 Example
Ask: *Explain binary search with diagram + quiz*.  
👉 Output: Step explanation, Graphviz diagram, quiz question.

---
Made with ❤️ using Gen-AI 🚀
