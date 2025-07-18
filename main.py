from dotenv import load_dotenv
load_dotenv()

from scraping.playwright_scraper import scrape_chapter
from ai_writer.writer_agent import ai_writer
from ai_writer.reviewer_agent import ai_reviewer
from utils.text_cleaner import clean_text
from rl_model.reward_signal import compute_reward

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"  # As per given task assignment i'm adding this url
    scrape_chapter(url)

    with open("outputs/raw_chapter.txt", encoding="utf-8") as f:
        raw = f.read()

    cleaned = clean_text(raw)
    spun = ai_writer(cleaned)
    reviewed = ai_reviewer(spun)
    
    with open("outputs/spun_chapter.txt", "w", encoding="utf-8") as f:
        f.write(spun)

    with open("outputs/reviewed_chapter.txt", "w", encoding="utf-8") as f:
        f.write(reviewed)


    # reward score from user
    reward = compute_reward(cleaned, spun, reviewed, feedback_score=0.9)
    print("Reward score:", reward)
    
    print("Scraping from webpage...")
    scrape_chapter(url)
    print("scraping done.")

    print("Reading raw file...")
    with open("outputs/raw_chapter.txt", encoding="utf-8") as f:
        raw = f.read()
    print("Raw file read.")

    cleaned = clean_text(raw)
    print("Text cleaned.")

    print("Initiating AI writer...")
    spun = ai_writer(cleaned)
    print("Spun version:", spun[:300])  # Showing preview
