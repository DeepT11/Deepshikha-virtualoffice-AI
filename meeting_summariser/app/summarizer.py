# app/summarizer.py

from transformers import pipeline

# Load the summarization pipeline using T5 or BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_chunk_size: int = 1024) -> str:
    """
    Summarizes long text using HuggingFace summarization pipeline.

    Args:
        text (str): Full transcript text
        max_chunk_size (int): Max input tokens per chunk (model limit ~1024)

    Returns:
        str: Summarized version of the text
    """
    if not text.strip():
        return "No content to summarize."

    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summary += result[0]['summary_text'].strip() + " "

    return summary.strip()
