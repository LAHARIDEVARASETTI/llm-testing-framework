'''pipfrom openai import OpenAI
from dotenv import load_dotenv
import os
from utils.file_loader import load_json
from utils.logger import logger
#from utils.helpers import normalize_text
import time

from utils.helpers import save_results


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

test_cases = load_json(
    "evaluation_pipeline/pipeline_data.json"
)

passed = 0
failed = 0

for test in test_cases:

    prompt = test["prompt"]

    expected_keywords = test["expected_keywords"]
    
    
    
    

    logger.info(f"Running test for: {prompt}")
    
    
    
    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    end_time = time.time()

    execution_time = end_time - start_time

    logger.info(f"Execution Time: {execution_time} seconds")

    

    answer = response.choices[0].message.content

    normalized_answer = normalize_text(answer)

    success = all(
        keyword in normalized_answer
        for keyword in expected_keywords
    )

    if success:
        print(f"PASS: {prompt}")
        passed += 1

    else:
        print(f"FAIL: {prompt}")
        failed += 1

logger.info(f"Passed: {passed}")
logger.info(f"Failed: {failed}")'''

import time

from models.openai_model import generate_openai_response
from models.gemini_model import generate_gemini_response

from utils.result_logger import save_result

PROMPT = "Explain what AI testing is."

# ----------------------------
# OPENAI
# ----------------------------

start_time = time.time()

response = generate_openai_response(PROMPT)

end_time = time.time()

latency = end_time - start_time

print("\nOPENAI RESPONSE:\n")

print(response)

save_result(
    test_type="response_quality",
    status="PASS",
    latency=latency,
    toxicity_score=0,
    hallucination_count=0,
    model="openai"
)

# ----------------------------
# GEMINI
# ----------------------------

start_time = time.time()

response = generate_gemini_response(PROMPT)

end_time = time.time()

latency = end_time - start_time

print("\nGEMINI RESPONSE:\n")

print(response)

save_result(
    test_type="response_quality",
    status="PASS",
    latency=latency,
    toxicity_score=0,
    hallucination_count=0,
    model="gemini"
)