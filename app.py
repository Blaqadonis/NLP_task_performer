import gradio as gr
from llmware_module import (
    classify_sentiment,
    detect_emotions,
    generate_tags,
    identify_topics,
    perform_intent,
    get_ratings,
    get_category,
    perform_ner,
    perform_nli,
)

def analyze_text(text, tasks):
    results = {}
    if not tasks:  # If no task is selected, default to sentiment analysis
        tasks = ["Sentiment Analysis"]
    if "Sentiment Analysis" in tasks:
        results["Sentiment Analysis"] = classify_sentiment(text)
    if "Emotion Detection" in tasks:
        results["Emotion Detection"] = detect_emotions(text)
    if "Generate Tags" in tasks:
        results["Generate Tags"] = generate_tags(text)
    if "Identify Topics" in tasks:
        results["Identify Topics"] = identify_topics(text)
    if "Perform Intent" in tasks:
        results["Perform Intent"] = perform_intent(text)
    if "Get Ratings" in tasks:
        results["Get Ratings"] = get_ratings(text)
    if "Get Category" in tasks:
        results["Get Category"] = get_category(text)
    if "Perform NER" in tasks:
        results["Perform NER"] = perform_ner(text)
    if "Perform NLI" in tasks:
        results["Perform NLI"] = perform_nli(text)
    return results

iface = gr.Interface(
    fn=analyze_text,
    inputs=[
        gr.Textbox(label="Enter Text Here:", lines=5),
        gr.CheckboxGroup(
            label="Select Analysis Tools to Use:",
            choices=[
                "Sentiment Analysis", "Emotion Detection", "Generate Tags", 
                "Identify Topics", "Perform Intent", "Get Ratings", 
                "Get Category", "Perform NER", "Perform NLI"
            ],
            type="value"
        )
    ],
    outputs=gr.JSON(label="Results"),
    title="🅱🅻🅰🆀's NLP Task Performer",
    description="Select one or more NLP tasks to perform on the input text."
)

iface.launch()