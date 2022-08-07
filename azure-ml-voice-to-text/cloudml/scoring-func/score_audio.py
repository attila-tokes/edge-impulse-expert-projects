# Imports
import os
import numpy as np
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

## Azure ML Schema Inference
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType

# Initialize Model:
def init():
    global tokenizer, model

    print("Loading pre-trained model (facebook/wav2vec2-base-960h).")
    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    print("Loading model DONE")
   
# The run() method is called each time a request is made to the scoring API.
@input_schema('data', NumpyParameterType(np.array([0.1, 1.2, 2.3])))
@output_schema(StandardPythonParameterType({ "result": "TEXT" }))
def run(data):    
    input_audio = data

    print("Input audio: %s" % input_audio);
    print(" - shape: %s" % input_audio.shape);

    input_values = tokenizer(input_audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
  
    # You can return any JSON-serializable object.
    return { "result" : transcription }