# 🤖 AI Coding Tutor Gen-AI

An **interactive AI-powered coding tutor** built with Streamlit.  
It helps learners understand coding concepts through **step-by-step explanations**, **auto-generated diagrams**, and **interactive quizzes**.  

Perfect for students, teachers, and self-learners who want a hands-on way to master programming.



## 🚀 Features
- 📘 **Step-by-step explanations** – Clear breakdown of coding concepts.
- 🖼️ **Auto-generated diagrams** – Visualize algorithms & data structures using Graphviz.
- 📝 **Interactive quizzes** – Practice with instant grading & feedback.
- 💬 **AI-powered tutor** – Ask coding questions and get tailored answers.



## 📂 Project Structure
```
ai-coding-tutor-gen-ai/
│── .env.example          # Example environment variables file
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── streamlit_app.py      # Main Streamlit app
└── src/
    ├── __init__.py
    ├── config.py         # Configuration & environment handling
    ├── tutor.py          # AI tutor logic (Q&A + explanations)
    ├── diagrams.py       # Diagram generation with Graphviz
    ├── quiz.py           # Quiz generation & grading
    └── utils.py          # Helper functions
```



## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-coding-tutor-gen-ai.git
   cd ai-coding-tutor-gen-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` → `.env`
   - Add your API key inside `.env`

4. **Run the Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```



## 💡 Example Usage

Ask the tutor:  
> *Explain binary search with a diagram and give me a quiz.*

✅ The app will:
1. Explain **binary search step-by-step**  
2. Show a **diagram** of how binary search works  
3. Generate a **quiz** with instant grading  



## 📸 Demo (Optional GIF/Images)
_Add screenshots or a short demo GIF here._



