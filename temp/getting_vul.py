import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
llm = genai.GenerativeModel('gemini-pro')

vul_format = """{
    Problem 1: Potential Solution of Problem 1,
    Problem 2: Potential Solution of Problem 2,
    .... and so on.
}"""

def get_vul(code):

    prompt = f"""
    You are given a code snippet, your task is to return a list of vulnerabilities in the code and their potential solution in this format.

    Format:
    ```
    vulnerabilities = {vul_format}
    ```

    Code:
    ```
    {code}
    ```
    """

    response = llm.generate_content(prompt)
    return response

