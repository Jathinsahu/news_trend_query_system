from gnews import GNews
import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "AIzaSyAglKsF7I1N45AqqXwC7EXrEiYEMceTYa4"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def fetch_news(query, max_results=2):
    google_news = GNews()
    articles = google_news.get_news(query)
    return articles[:max_results]

def summarize_article(content, user_query):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Based on the following article:\n\n{content}\n\n Answer the question and give only the most relevant information : {user_query}"
    response = model.generate_content(prompt)
    return response.text

def chatbot():
    user_query = input("Ask me your query : ")
    articles = fetch_news(user_query)
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Source: {article['publisher']['title']}")
        print(f"Link: {article['url']}")
        print("Summary:")
        content = article['description'] 
        summary = summarize_article(content, user_query)
        print(summary)
        print("\n")

chatbot()
