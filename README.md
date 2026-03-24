# 🍳 AI Recipe Bot: Vision-to-Table
A sophisticated AI agent that transforms refrigerator photos into personalized recipes. Built with **LangChain**, **OpenAI**, and **Streamlit**, this bot analyzes images, searches the web for the best cooking methods, and formats a culinary plan in real-time.

## 🚀 How it Works
1.  **Image Analysis:** Uses OpenAI's Vision capabilities to identify ingredients from an uploaded photo.
2.  **Agentic Search:** A LangChain agent uses the **Tavily Search Tool** to find trending or highly-rated recipes based on those specific ingredients.
3.  **Dynamic Execution:** The agent reasons through the search results to pick the most feasible recipe based on common pantry staples.
4.  **Streamlit Interface:** Provides a clean, interactive UI for image uploads and recipe display.

## 🛠️ Tech Stack
* **Framework:** `LangChain` (Agentic workflow & Tool calling)
* **LLM:** `OpenAI GPT-4o` (Vision and Reasoning)
* **Search Engine:** `Tavily API` (Optimized for AI agent web search)
* **Frontend:** `Streamlit`
* **Utilities:** `Base64` for image encoding, `Python-dotenv` for secret management.

## 📦 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/ai-recipe-bot.git](https://github.com/your-username/ai-recipe-bot.git)
    cd ai-recipe-bot
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_key
    TAVILY_API_KEY=your_tavily_key
    ```

4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 🧠 Key Logic Highlights
* **Vision Processing:** The bot converts images to `base64` to pass them through a `HumanMessage`, allowing the LLM to "see" your ingredients.
* **Agentic Logic:** Using `create_agent` and `init_chat_model`, the bot is equipped with a `tool` (Tavily) that allows it to browse the live internet if it needs more information.

---
**Developed by [Your Name]**
