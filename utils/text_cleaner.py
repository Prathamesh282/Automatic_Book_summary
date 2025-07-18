def clean_text(raw_text):
    cleaned = raw_text.replace("\n", " ").strip()
    return cleaned