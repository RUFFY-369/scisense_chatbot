import os
import warnings
from typing import Dict
from model.galactica import init_model, generate_response
from openfabric_pysdk.utility import SchemaUtil
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass


############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    print(configuration)
    print(state)


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []
    # Initialize the model and tokenizer
    model, tokenizer, temp_dir = init_model()

    for text in request.text:
        # Check for empty or invalid input
        if not text.strip():
            output.append("Please provide a valid input.")
            continue

        try:
            # Generate the response
            response = generate_response(model, tokenizer, text)
            output.append(response)
        except Exception as e:
            # Handle the error, log it, and add a fallback response
            error_message = f"Error generating response for '{text}': {str(e)}"
            warnings.warn(error_message)
            output.append("Sorry, I encountered an issue processing your request.")

    # Clean up the temporary directory when done
    temp_dir.cleanup()

    return SchemaUtil.create(SimpleText(), dict(text=output))
