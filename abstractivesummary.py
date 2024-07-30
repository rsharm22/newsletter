# This script contains the functions to generate the AI summary from the article details taking into account missing
# indices, and varying search options.

from transformers import BartForConditionalGeneration, BartTokenizer
from credentials import categories

# Load the BART model and tokenizer
model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)


# Creating a function to generate an AI summary from text
def generate_summary(text, max_length=200, min_length=30):
    inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4,
                                 early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# Creating a function to generate the AI summary based on category and indices of articles available
def generate_ai_summary(articles, category=categories, max_length=1000):
    abstractive_summaries = {}
    indices = articles.keys()
    for i in indices:
        abstractive_summaries[i] = generate_summary(articles[i][1], max_length=max_length)
        if not abstractive_summaries[i].endswith('.'):
            abstractive_summaries[i] += '.'
    return abstractive_summaries
