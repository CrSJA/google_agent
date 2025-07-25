import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types
load_dotenv()





def main():

    print(len(sys.argv))
    if len(sys.argv) == 1:
        sys.exit("error arguments not provided")

    user_prompt=sys.argv[1]

    messages=[
        types.Content(role='user',parts=[types.Part(text=user_prompt)])
    ]

    if '--verbose' in sys.argv:
        api_key = os.environ.get("GEMINI_API_KEY")
        #print("GEMINI_API_KEY" in os.environ)  

        client = genai.Client(api_key=api_key)


        response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        )
        print(response.text)
        print(f'responce tokens: {response.usage_metadata.candidates_token_count}')
        print(f'user prompt: {user_prompt}')
        print(f'promt tokens: {response.usage_metadata.prompt_token_count}')


    else:

        api_key = os.environ.get("GEMINI_API_KEY")
        #print("GEMINI_API_KEY" in os.environ)  

        client = genai.Client(api_key=api_key)


        response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        )

        print(response.text)





if __name__ == "__main__":
    main()
