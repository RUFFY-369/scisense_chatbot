<!-- # SciSenseBot - A Galactica based Chatbot to answer Science related Questions

## Task
Forge an 💬NLP chatbot that doesn’t just answer, but masters science-related questions.

## Ground Rules
Step up with any arsenal (read: libraries or packages) you believe in, but remember:
* 👎 External services like chatGPT are off-limits. Stand on your own.
* 👎 Plagiarism is for the weak. Forge your own path.
* 👎 A broken app equals failure. Non-negotiable.

## Deployment Options
The application can be executed in two different ways:
* locally by running the `start.sh` 
* on in a docker container using `Dockerfile` 

## Proving Your Mettle
* Submit your masterpiece on GitHub. We want the link within **1 week, not a second more**.
* Go the extra mile and include a video where you walk us through your solution, showcasing 
it in live action. 
* We want to see not just what you've created but also how you envisioned and executed it


## This Is It
We're not just evaluating a project; we're judging your potential to revolutionize our 
landscape. A half-baked app won’t cut it.

We're zeroing in on:
* 👍 Exceptional documentation.
* 👍 Code that speaks volumes.
* 👍 Inventiveness that dazzles.
* 👍 A problem-solving beast.
* 👍 Unwavering adherence to the brief -->

# SciSenseBot - A Science Q&A Chatbot Powered by Galactica
Welcome to SciSenseBot – an intelligent chatbot designed to tackle your toughest science-related questions. Powered by the Galactica language model, SciSenseBot leverages cutting-edge natural language processing (NLP) to generate precise, insightful responses to questions spanning physics, chemistry, biology, and beyond!

## 🌟 Solution Overview
This project is the solution to the challenge of creating an AI chatbot capable of answering complex science-related queries. Our bot harnesses Galactica, a powerful model optimized for scientific content, ensuring high-quality, contextually accurate responses.

In this implementation, we focus on efficiency, creativity, and robustness by using OPTForCausalLM from the Galactica family to provide accurate and meaningful responses to a wide variety of scientific questions.

## 🚀 Features
Scientific Q&A: Answers a wide range of science-related questions in physics, chemistry, biology, and other disciplines.
Contextual Understanding: Galactica is fine-tuned to handle technical and scientific language efficiently.
Error Handling: Built-in error handling ensures a smooth experience even when dealing with problematic inputs.

## 🧠 How It Works
### 1. Model Initialization
SciSenseBot initializes the Galactica model for causal language modeling using OPTForCausalLM to generate science-related responses.

```
from transformers import OPTForCausalLM, AutoTokenizer
import tempfile

def init_model(model_name: str = "facebook/galactica-1.3b"):
    temp_dir = tempfile.TemporaryDirectory()
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = OPTForCausalLM.from_pretrained(
        model_name, device_map="auto", offload_folder=temp_dir.name
    )
    return model, tokenizer, temp_dir
```

### 2. Response Generation
Galactica generates responses based on input prompts provided by the user.

```
def generate_response(model, tokenizer, prompt, max_length=250, top_p=0.7):
    prompt = f"Question: {prompt}\n\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    response = model.generate(inputs, max_length=max_length, do_sample=True, top_p=top_p)[0]
    output = tokenizer.decode(response, skip_special_tokens=True)
    return output
```

### 3. Error Handling
SciSenseBot gracefully handles invalid or empty inputs, ensuring a reliable and responsive chatbot experience.

```
if not text.strip():
    output.append("Please provide a valid input.")
else:
    try:
        response = generate_response(model, tokenizer, text)
        output.append(response)
    except Exception as e:
        warnings.warn(f"Error generating response for '{text}': {str(e)}")
        output.append("Sorry, I encountered an issue processing your request.")
```

## 🛠️ Usage
Running Locally
You can run the bot on your local machine by following these steps:

Install the required dependencies:

```
pip install -r requirements.txt
```

Start the app:

```
bash start.sh
```

Example:

```
curl --location 'localhost:5500/execution' \
     --header 'Content-Type: application/json' \
     --data '{
         "text":["What is the theory of evolution?"]
     }'
```

## 🧪 Sample Questions

```
declare -a questions=(
    "What is the structure of a black hole?"
    "Explain the process of photosynthesis."
    "What is DNA replication?"
    "Describe quantum entanglement."
    "How do chemical reactions occur?"
    "What is gravitational force?"
)
```

You can also run these questions in bulk using the provided script in the /scripts folder.

## 📊 Model Information
Model	Size	Purpose
Galactica (1.3B)	1.3B	Generating science-related responses

## ✨ Key Highlights
Science-Tuned: Galactica excels at answering complex science-related questions with precision.
Performance: The model handles a wide array of scientific topics efficiently while maintaining good response times.
Error Handling: Built-in exception handling ensures robustness against malformed inputs.

## 🔍 Further Improvements
Expand the model’s capabilities by fine-tuning for more specific scientific domains.
Introduce caching for repeated questions to enhance performance in large-scale use cases.

## 💡 Conclusion
The SciSenseBot is an intelligent chatbot tailored for science Q&A tasks. By utilizing the Galactica model, we ensure that it delivers high-quality, contextually accurate responses across a wide range of scientific domains. This is a powerful tool for students, educators, and science enthusiasts alike.