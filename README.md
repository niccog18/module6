# Module 6: Web Essentials & Streamlit — Starter Kit

## Quick Setup

### Option A: Clone with Git
```bash
git clone <repo-url>
cd module-06-web-essentials-streamlit
```

### Option B: Download ZIP (no Git required)
1. Go to this repo on GitHub
2. Click the green **Code** button
3. Click **Download ZIP**
4. Unzip the downloaded file and open the folder

---

### Shared steps (both options)

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start working:** Open any exercise folder and edit the starter file.

---

### Running the apps

| App type | Command |
|----------|---------|
| Streamlit app | `streamlit run solution.py` |
| FastAPI backend | `uvicorn mini_api:app --reload --port 8000` |
| Plain Python script | `python solution.py` |
| HTML file | Open in any browser (double-click or `open file.html`) |

> **Note for mini-dashboard and streamlit-fastapi exercises:** start the FastAPI
> backend first, then open the HTML frontend or run the Streamlit app.

---

## Exercises

| # | Exercise | Folder | Packages / Tech |
|---|----------|--------|-----------------|
| L1 | API Explorer | `exercises/api-explorer/` | **requests** |
| L2 | Portfolio Page | `exercises/portfolio-page/` | HTML5 only |
| L3 | Styled Portfolio | `exercises/styled-portfolio/` | HTML5 + CSS3 |
| L4 | Interactive Flashcard App | `exercises/flashcard-app/` | Vanilla JS |
| L5 | API-Powered Live Search | `exercises/live-search/` | Vanilla JS + Fetch API |
| L6 | Mini Dashboard | `exercises/mini-dashboard/` | **fastapi**, **uvicorn** + HTML/JS |
| L7 | Streamlit Exploration App | `exercises/exploration-app/` | **streamlit** |
| L8 | Personal Stats Dashboard | `exercises/personal-dashboard/` | **streamlit** |
| L9 | Stateful Quiz App | `exercises/quiz-app/` | **streamlit** |
| L10 | Data Explorer | `exercises/data-explorer/` | **streamlit**, **requests** |
| L11 | Streamlit + FastAPI | `exercises/streamlit-fastapi/` | **streamlit**, **fastapi**, **uvicorn** |
| L12 | AI Chat Interface | `exercises/ai-chat/` | **streamlit** |

> **Lessons 1–6** use the HTML/CSS/JS skills introduced early in the module.
> **Lessons 7–12** use Streamlit. Make sure your virtual environment is active
> and `requirements.txt` is installed before running those exercises.

---

### Stretch Challenges (solutions only)

| # | Challenge | Folder | Builds On |
|---|-----------|--------|-----------|
| L3b | Responsive Media Query | `solutions/responsive-portfolio/` | L3 Styled Portfolio |
| L4b | Keyboard Navigation | `solutions/flashcard-keyboard/` | L4 Flashcard App |
| L9b | Countdown Timer | `solutions/quiz-timer/` | L9 Quiz App |
| L12b | Conversation Export | `solutions/chat-export/` | L12 AI Chat |

---

## Module Project

The project is an **AI Dashboard** — a full Streamlit app with authentication,
task management, data visualisation, and an AI chat interface.

### Starter
```bash
cd project/starter
pip install -r requirements.txt
streamlit run app.py
```

The starter includes:
- `app.py` — Streamlit skeleton with TODO stubs
- `api_client.py` — stub API functions to implement
- `mock_data.py` — sample data for offline development

### Running with the backend
```bash
pip install fastapi uvicorn
uvicorn backend:app --reload --port 8000   # in one terminal
streamlit run app.py                        # in another terminal
```

See the project README in `project/starter/` for full requirements, grading rubric, and presentation guidelines.

---

## Solutions

Solutions are in the `solutions/` folder. **Try each exercise yourself first!**
Compare your approach to the reference solution after you've made your attempt.
Differences are fine — there are many valid ways to solve these problems.

---

## Need Help?

- Re-read the lesson's Concept and Guided Example sections
- Post in the course discussion board
- Bring questions to office hours
