import subprocess

def ai_reviewer(text):
    prompt = f"Check grammar, tone, and suggest improvements:\n{text}" # Adjust the prompt as needed
    
    result = subprocess.run(
        ["ollama", "run", "gemma:2b", prompt], # prompt to initiate gemma:2b locally
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
