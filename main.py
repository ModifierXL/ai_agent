import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("No API Key found!")

    client = genai.Client(api_key=api_key)
    ai_model = "gemini-2.5-flash"

    response = client.models.generate_content(
        model = ai_model, 
        contents = messages)
    
    if not response:
        raise RuntimeError("Something went wrong with your request to the GEMINI API")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print("Response:")
    print(result.text)


if __name__ == "__main__":
    main()
