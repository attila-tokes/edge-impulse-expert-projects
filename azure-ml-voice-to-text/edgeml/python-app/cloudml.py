import requests

# CloudML interaction via REST endpoints
class CloudML:
    DEFAULT_SCORE_ENDPOINT = "http://localhost:5001/score"
    DEFAULT_API_KEY = "none"

    def __init__(self, score_endpoint = DEFAULT_SCORE_ENDPOINT, api_key = DEFAULT_API_KEY):
        self.score_endpoint = score_endpoint
        self.api_key = api_key
        pass

    # Call the voice to text scoring endpoint
    def voice_to_text(self, input_audio):
        r = requests.post(self.score_endpoint,
        json={ "data": input_audio.tolist() },
        headers={ "Authorization" : "Bearer " + self.api_key })

        if r.status_code != 200:
            raise "Cloud request failed!"

        payload = r.json()
        return payload['result']