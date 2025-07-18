# 📚 Automated Book Publication Workflow

An AI-powered pipeline that automates the scraping, rewriting, reviewing, and feedback-driven improvement of book chapters using local LLMs (Gemma 2B) via Ollama — all without requiring paid APIs.

---

## 🚀 Features

- ✅ Chapter scraping from online sources (e.g., Wikisource)
- ✍️ AI Writer: Rewrites content into a more engaging narrative using **Gemma 2B**
- 🧐 AI Reviewer: Reviews for grammar, tone, and style improvements
- 👨‍💻 Human-in-the-loop Streamlit UI for approval and feedback
- 📊 Reward model using Reinforcement Learning signal
- 🔍 Semantic search with ChromaDB for version retrieval
- 🧠 All models run **locally via Ollama**, no paid APIs needed

---

## 🧱 Project Structure

```
automated-book-workflow/
│
├── ai_writer/
│   ├── writer_agent.py        # Calls Gemma to rewrite text
│   └── reviewer_agent.py      # Calls Gemma to review text
│
├── scraping/
│   └── playwright_scraper.py  # Scrapes content from web
│
├── human_interface/
│   └── streamlit_ui.py        # Human approval and feedback UI
│
├── chromadb/
│   └── vector_store.py        # Stores and searches versions
│
├── rl_model/
│   └── reward_signal.py       # Computes feedback-based rewards
│
├── utils/
│   └── text_cleaner.py        # Basic text preprocessing
│
├── outputs/                   # Stores raw, spun, and reviewed text
├── main.py                    # End-to-end execution pipeline
└── requirements.txt           # Dependencies
```

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/automated-book-workflow.git
cd automated-book-workflow
```

2. **Set up environment**
```bash
pip install -r requirements.txt
```

3. **Install and run Ollama**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull and run Gemma 2B model
ollama pull gemma:2b
ollama run gemma:2b
```

---

## 📌 Usage

### ➤ Step 1: Run the Workflow
```bash
python main.py
```

This will:
- Scrape a chapter
- Rewrite it with Gemma
- Review it with Gemma
- Compute reward score

### ➤ Step 2: Launch the Human Feedback UI
```bash
streamlit run human_interface/streamlit_ui.py
```

- Paste the original, spun, and reviewed content.
- Manually finalize and submit feedback.
- Reward model updates accordingly.

---

## 🧠 Semantic Search (ChromaDB)

All versions are stored with embeddings using ChromaDB and can be retrieved via metadata and similarity search (via `vector_store.py`).

---

## 🧪 Example Output

```bash
Reward score: 0.87
Chapter rewritten and reviewed saved in outputs/
```

---

## 🤖 Models Used

| Component       | Model        | Source      |
|----------------|--------------|-------------|
| AI Writer       | Gemma 2B     | Local via Ollama |
| AI Reviewer     | Gemma 2B     | Local via Ollama |
| Embeddings      | OpenAIEmbeddings or custom | ChromaDB |
| RL Reward Logic | Custom       | Python Logic |

---

## 📎 Future Enhancements

- Switch to local embedding model (e.g., MiniLM) for full offline capability
- Add multi-chapter ingestion
- Implement vector-based search UI
- Track human feedback logs per version

---

## 🧑‍💻 Contributors

- **Prathamesh Bandal** – Project Author & Developer

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
