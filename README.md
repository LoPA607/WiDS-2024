# WiDS-2024
# Fine-Tuning a Large Language Model (LLM) for a Financial Chatbot  

## 📄 Project Overview  
This project involves building and fine-tuning a Large Language Model (LLM) to create a chatbot that answers queries related to the finance domain. The chatbot focuses on providing accurate and up-to-date information about top companies in India, such as stock updates, quarterly results, and company announcements.  

## ✨ Key Features  
- Answers queries related to financial news and company updates.  
- Uses fine-tuned LLM for question-answering tasks in the finance domain.  
- Integrated with a user-friendly web-based interface for seamless interaction.  
- Provides real-time, reliable financial insights from curated sources.  

---

## 📌 Learnings  
- Python (Intermediate Level)  
- Web Scraping Knowledge  
- Understanding of Natural Language Processing (NLP) and Large Language Models  

---

## 🚀 Project Workflow  

### A) Dataset Preparation  
1. **Data Collection**  
   - Scraped financial news and company announcements from reliable sources like:  
     - [Moneycontrol](https://www.moneycontrol.com)  
     - [Economic Times](https://economictimes.indiatimes.com)  
   - Collected data on stock prices, quarterly earnings, and major announcements from top Indian companies.  

2. **Post-Processing**  
   - Cleaned and filtered the data to remove noise, irrelevant details, and duplicates.  
   - Transformed the dataset into a question-answering format suitable for training the model.  
   - **Example Dataset Format (JSON)**:  
     ```json
     [
       {
         "id": "1",
         "question": "What are the latest quarterly results of Reliance Industries?",
         "answers": ["Reliance Industries reported a net profit of ₹15,792 crore for Q3 FY24."]
       },
       {
         "id": "2",
         "question": "What is the stock price of TCS?",
         "answers": ["The current stock price of TCS is ₹3,500 (as of the latest update)."]
       }
     ]
     ```  

---

### B) Model Training  
1. **Model Selection**  
   - Pre-trained models were chosen from Hugging Face, including:  
     - BERT (Bidirectional Encoder Representations from Transformers)  


2. **Fine-Tuning Process**  
   - Fine-tuned the selected model for question-answering tasks using the prepared financial dataset.  
   - Applied techniques to avoid overfitting and ensure robust performance on unseen queries.  

3. **Performance Metrics**  
   - Evaluated the model using:  
     - **Accuracy**  
     - **F1-Score**  
     - **BLEU Score**  

---

### C) Evaluation and Interface Integration  
1. **Model Evaluation**  
   - Tested the model on unseen financial queries to assess its accuracy and relevance.  
  

2. **User Interface**  
   - Developed a web-based interface using **Gradio** for easy user interaction with the chatbot.  


---


