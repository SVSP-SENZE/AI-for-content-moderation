def analyze_text(text):
    """
    Mock implementation for text analysis.
    In a real scenario, this would use a NLP model to detect safety issues.
    """
    print("  [Pipelines] Analyzing text...")
    # Mock detection: if "hack" is in text, flag it
    if "hack" in text.lower():
        return {"score": 0.85, "reason": "Potential hacking/malicious content detected in text"}
    return {"score": 0.1, "reason": "No issues found"}

def analyze_audio(audio_path):
    """
    Mock implementation for audio analysis.
    In a real scenario, this would use speech-to-text or audio classification.
    """
    print("  [Pipelines] Analyzing audio...")
    return {"score": 0.2, "reason": "No suspicious audio patterns found"}

def analyze_video(frame_paths):
    """
    Mock implementation for video analysis.
    In a real scenario, this would use computer vision models on the frames.
    """
    print("  [Pipelines] Analyzing video frames...")
    return {"score": 0.15, "reason": "Visual content appears safe"}
