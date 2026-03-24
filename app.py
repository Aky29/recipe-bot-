requirementsfrom langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient
import base64
import streamlit as st
from langchain.messages import HumanMessage
from openai import OpenAI
load_dotenv()

openai_key = os.environ["OPENAI_API_KEY"] 
tavily_key = os.environ["TAVILY_API_KEY"]

tavily_client = TavilyClient(api_key=tavily_key)
client = OpenAI(api_key=openai_key)

@tool
def search_for_recipe(ingredients: str) -> str:
    """
    Search for information.
    """
    response = tavily_client.search(ingredients=ingredients)
    return response


agent = create_agent(
    model=init_chat_model(model="gpt-4o", temperature=0.9, openai_api_key=openai_key),
    system_prompt="you are helpful assistant that helps users find resipes based on the ingredients they have."
)

picture = st.file_uploader("Upload an image of your ingredients", type=["png"])

audio_value = st.audio_input("Record voice input")

if audio_value:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_value
    )
    user_input = transcription.text
    st.success(f"Transcribed: {user_input}")
else:
    user_input = st.text_input("Enter ingredients (comma separated):")

if picture is not None:
    bytes_data = picture.getvalue()
    base64_encoded = base64.b64encode(bytes_data).decode("utf-8")

    data_url = f"data:{picture.type};base64,{base64_encoded}"

    if user_input:
        multimodal_question = HumanMessage(
            content=[
                {"type": "text", "text": user_input},
                {
                    "type": "image_url",
                    "image_url": {"url": data_url},
                },
            ]
        )

        response = agent.invoke({"messages": [multimodal_question]})
        st.markdown(response["messages"][-1].content)
