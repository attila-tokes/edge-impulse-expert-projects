from scipy.io import wavfile
import requests
import librosa

# Read audio file
file_name = 'sample.wav'
input_audio, _ = librosa.load(file_name, sr=16000)

# Make request to the Azure ML endpoint
r = requests.post('https://ml-endpoint-voice-to-text.westeurope.inference.ml.azure.com/score',
             json={"data": input_audio.tolist()}, headers={"Authorization":"Bearer 4h6iclxxxxxxxxxxxxx"})

print("Status code: %d" % r.status_code)
print("Result: %s" % r.json())