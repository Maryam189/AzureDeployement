import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from datasets import load_dataset
import re
from google.colab import drive
from rouge_score import rouge_scorer

# Load dataset
df = load_dataset('cnn_dailymail', '3.0.0')
train_df = pd.DataFrame(df['train'])
test_df = pd.DataFrame(df['test'])
val_df = pd.DataFrame(df['validation'])

# Display the first few rows of the dataset
print("Train Dataset - Sample Rows:")
print(train_df.head())

# Distribution of article length
train_df['article_len'] = train_df['article'].apply(lambda x: len(x.split()))
plt.figure(figsize=(10, 6))
sns.histplot(data=train_df, x='article_len', bins=30)
plt.title("Distribution of Article Length")
plt.xlabel("Article Length")
plt.show()

# Data Cleaning
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(' +', ' ', text)
    return text

train_df['article'] = train_df['article'].apply(clean_text)
train_df['highlights'] = train_df['highlights'].apply(clean_text)

# Check for missing data
missing_data = train_df.isnull().sum()
print("Missing Data:")
print(missing_data)

# Balancing Check
category_counts = train_df['article_len'].value_counts()
print("Train Dataset - Category Counts:")
print(category_counts)

# Model preparation
model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def generate_summary(article_text, max_length=100):
    inputs = tokenizer(article_text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=max_length, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Summarize and evaluate a single article from the test dataset
article = test_df.iloc[0]['article']
original_summary = test_df.iloc[0]['highlights']
generated_summary = generate_summary(article)
print("Generated Summary:")
print(generated_summary)

# Calculate ROUGE scores
rouge_scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'])
rouge_scores = rouge_scorer.score(generated_summary, original_summary)

# Print ROUGE scores line by line
for metric, scores in rouge_scores.items():
    print(f"{metric}:")
    print(f"Precision: {scores.precision}")
    print(f"Recall: {scores.recall}")
    print(f"F1 Score: {scores.fmeasure}")
    print()

# Function to calculate word overlap accuracy
def calculate_accuracy(original_summary, generated_summary):
    original_words = set(original_summary.split())
    generated_words = set(generated_summary.split())
    common_words = original_words.intersection(generated_words)
    accuracy = len(common_words) / len(original_words) if len(original_words) > 0 else 0.0
    return accuracy

# Calculate and print accuracy
accuracy = calculate_accuracy(original_summary, generated_summary)
print(f"Word Overlap Accuracy: {accuracy:.2%}")

# Calculate and print the average ROUGE F1 score
average_f1_score = sum(scores.fmeasure for scores in rouge_scores.values()) / len(rouge_scores)
print(f"Average ROUGE F1 Score: {average_f1_score:.4f}")