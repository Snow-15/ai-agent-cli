import sys
import argparse

from google.genai import types

from ai_client import generate_response
from call_function import get_function_responses
from config import MAX_ITERS


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(MAX_ITERS):
        response = generate_response(messages)

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.usage_metadata is None:
            raise RuntimeError("API request failed")
        
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            function_results = get_function_responses(response.function_calls, verbose=args.verbose)
        else:
            print(f"Response:\n{response.text}")
            return

        messages.append(types.Content(role="user", parts=function_results))

    print(f"Error: Maximum iterations has been reached and the model still hasn't produced a final response")
    sys.exit(1)


if __name__ == "__main__":
    main()
