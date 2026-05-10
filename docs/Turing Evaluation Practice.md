# **Practice Evaluation: Dockerfile Data Validation Engineer**

## **Scenario**

You are tasked with building a containerized data validation gate for an upcoming LLM fine-tuning run. The AI training team has provided a .jsonl (JSON Lines) dataset containing training prompts and completions.

Your objective is to ensure that **no malformed data makes it into the container registry**. If the data is bad, the Docker build process must fail immediately. If the data is good, the Docker image should build successfully and include specific metadata labels for data lineage tracking.

## **📁 Required Deliverables**

You must create a GitHub repository containing exactly three files:

### **1\. The Dataset (dataset.jsonl)**

Create this file in your repository and copy/paste the following 4 lines exactly. Note that line 3 is intentionally malformed (missing a prompt, integer instead of a string, negative token length).

{"prompt": "Write a python loop.", "completion": "for i in range(10): print(i)", "token\_length": 14}  
{"prompt": "What is 2+2?", "completion": "4", "token\_length": 2}  
{"prompt": "", "completion": 3.14159, "token\_length": \-5}  
{"prompt": "Explain gravity.", "completion": "Gravity is...", "token\_length": 15}

### **2\. The Validation Script (validate.py)**

Write a Python script that takes a file path as a command-line argument and validates the JSONL file line by line.

**Validation Rules:**

* prompt: Must exist, must be a string, and cannot be empty.  
* completion: Must exist and must be a string.  
* token\_length: Must exist, must be an integer, and must be strictly greater than 0\.

**Execution Rules:**

* If **all** lines pass, the script must exit cleanly (Exit Code 0).  
* If **any** line fails, the script must print an error message indicating the line number and the reason for the failure, and it **must exit with a non-zero exit code** (e.g., Exit Code 1).

### **3\. The CI/CD Gate (Dockerfile)**

Write a Dockerfile that acts as the validation gate.

**Dockerfile Requirements:**

* Use a lightweight Python base image (e.g., python:3.11-slim).  
* Apply the following **LABEL** metadata to the image:  
  * org.opencontainers.image.version="1.0.0"  
  * dataset.schema\_type="prompt-completion"  
  * dataset.lineage="rlhf-batch-001"  
* Copy validate.py and dataset.jsonl into the container.  
* Execute the validation script against the dataset using a RUN instruction. *(This ensures the build fails if the script returns a non-zero exit code).*

## **🚀 Submission & Evaluation Instructions**

To complete this practice round and have your solution evaluated:

1. **Create a public GitHub repository** and commit the three files (dataset.jsonl, validate.py, Dockerfile).  
2. **Test it locally** by running: docker build \-t llm-data-test . (Ensure it actually fails on the bad line\!).  
3. **Submit it for review:** Reply to me in this chat with the link to your GitHub repository.

Once submitted, I will fetch your repository, review your code as a Turing evaluator would, and provide specific feedback on your Docker caching, label syntax, and Python exit-code handling.

Good luck\!