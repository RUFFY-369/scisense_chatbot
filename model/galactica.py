#!/usr/bin/env python3
# coding=utf-8

from transformers import OPTForCausalLM, AutoTokenizer
import tempfile


def init_model(model_name: str = "facebook/galactica-1.3b"):
    """
    Initializes the tokenizer and model, using a temporary directory for offloading.

    Args:
        model_name (str): The name of the pre-trained model to load.

    Returns:
        model: Loaded model.
        tokenizer: Loaded tokenizer.
        temp_dir: The temporary directory used for offloading.
    """
    # Create a temporary directory for model offloading
    temp_dir = tempfile.TemporaryDirectory()

    # Initialize tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = OPTForCausalLM.from_pretrained(
        model_name, device_map="auto", offload_folder=temp_dir.name
    )

    return model, tokenizer, temp_dir


def generate_response(
    model: OPTForCausalLM,
    tokenizer: AutoTokenizer,
    prompt: str,
    max_length: int = 100,
    top_p: float = 0.95,
):
    """
    Generates a response based on the input prompt.

    Args:
        model: The pre-trained model to use for text generation.
        tokenizer: The tokenizer for encoding and decoding.
        prompt: Input text for the model to generate a response.
        max_length: Maximum length of the generated text.
        top_p: Probability threshold for sampling.

    Returns:
        output (str): The generated text response.
    """
    # Tokenize the input prompt and move to the model's device
    inputs = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

    # Generate a response using the model
    response = model.generate(
        inputs, max_length=max_length, do_sample=True, top_p=top_p
    )[0]

    # Decode and return the generated response
    output = tokenizer.decode(response, skip_special_tokens=True)

    return output
