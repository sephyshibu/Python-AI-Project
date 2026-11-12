import os 
import sys
import logging
from typing import Optional
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

# Configure professional logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("Python AI project")

def initialize_client() -> genai.Client:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        logger.error("GEMINI_API_KEY is missing from environment variables or .env file.")
        raise ValueError("Missing API Key. Check your .env setup.")

    logger.info("Google GenAI client initialized successfully.")
    return genai.Client(api_key=api_key)

def query_llm(prompt: str, system_prompt: Optional[str] = None) -> Optional[str]:
    """
    Sends a structured prompt to the Google Gemini API with robust error handling.
    """
    client = initialize_client()

    try:
        logger.info("Sending request to Gemini...")
        
        # Combine system instructions and prompt if needed
        config = None
        if system_prompt:
            from google.genai import types
            config = types.GenerateContentConfig(system_instruction=system_prompt)

        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=prompt,
            config=config
        )

        logger.info("Successfully received response from Gemini.")
        return response.text

    except APIError as e:
        logger.error(f"Google API error occurred: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        
    return None

if __name__ == "__main__":
    print("=== Week 1 AI Script Execution (Gemini Free Tier) ===")
    user_prompt = "Explain how vector embeddings are used in AI in 3 concise bullet points."
    system_role = "You are an expert AI engineer and technical educator."
    
    result = query_llm(prompt=user_prompt, system_prompt=system_role)
    
    if result:
        print("\n--- Final Formatted Response ---")
        print(result)
    else:
        print("\nExecution failed. Review log outputs above.")