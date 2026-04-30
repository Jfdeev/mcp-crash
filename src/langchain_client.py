import asyncio

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-pro", temperature=0)

async def main():
    print("Starting LangGraph React Agent with MultiServerMCPClient...")

if __name__ == "__main__":
    asyncio.run(main())