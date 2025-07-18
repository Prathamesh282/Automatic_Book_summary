import streamlit as st
from rl_model.reward_signal import compute_reward
from utils.text_cleaner import clean_text

# Load content
def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""
    
# text files saved to outputs folder after executing scraper
raw = load_file("outputs/raw_chapter.txt")
spun = load_file("outputs/spun_chapter.txt") 
reviewed = load_file("outputs/reviewed_chapter.txt")

# adding title for streamlit page
st.title("Automated Book Workflow, Review & Feedback")

st.subheader("Original Chapter")
st.text_area("Original Text", raw, height=200)

st.subheader("AI Spun text")
st.text_area("AI Rewritten Text", spun, height=200)

st.subheader("AI Reviewed text")
st.text_area("Reviewed Text", reviewed, height=200)

# Human Final Approval/Feedback
st.subheader("User Final Approval")
final = st.text_area("Your Final Approved Version", reviewed, height=200)

feedback_score = st.slider("How do you rate the AI output?", 0.0, 1.0, 0.8)

if st.button("Submit your feedback"):
    cleaned_raw = clean_text(raw)
    reward = compute_reward(cleaned_raw, spun, reviewed, feedback_score)

    with open("outputs/human_feedback.txt", "w", encoding="utf-8") as f:
        f.write(f"Final Version:\n{final}\n\nFeedback Score: {feedback_score}\nReward: {reward}\n")

    st.success(f"Thank you for feedback. Reward Score: {reward:.3f}")
