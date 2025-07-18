import subprocess
import json

def ai_writer(text):
    prompt = f"Rewrite this chapter with more engaging narrative:\n{text}"
    print("Running Gemma via Ollama...")
    result = subprocess.run(
        ["ollama", "run", "gemma:2b"],
        input=prompt,
        text=True,
        capture_output=True,
        timeout=120  # prevent infinite wait
    )
    print("Gemma output captured.")
    return result.stdout

