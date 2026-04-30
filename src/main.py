import asyncio

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import GoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-pro", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/Users/dti-/Desktop/mcp-crash/src/servers/math_server.py"],
)

async def main():   
    print("Hello from mcp-crash!")


if __name__ == "__main__":
    asyncio.run(main())
