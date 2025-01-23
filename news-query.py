from gnews import GNews
import os
import google.generativeai as genai

# Set your Google API key (replace this with your actual API key)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAglKsF7I1N45AqqXwC7EXrEiYEMceTYa4"

# Configure Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to fetch news articles based on query
def fetch_news(query, max_results=2):
    google_news = GNews()
    articles = google_news.get_news(query)
    return articles[:max_results]

# Function to summarize article based on user query
def summarize_article(content, user_query):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Based on the following article:\n\n{content}\n\nAnswer the question: {user_query}"
    response = model.generate_content(prompt)
    return response.text

# Chatbot function
def chatbot():
    user_query = input("Ask me anything: ")
    articles = fetch_news(user_query)
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Source: {article['publisher']['title']}")
        print(f"Link: {article['url']}")
        print("Summary:")
        content = article['description']  # Assuming 'description' contains the article content
        summary = summarize_article(content, user_query)
        print(summary)
        print("\n")

# Run the chatbot
chatbot()
