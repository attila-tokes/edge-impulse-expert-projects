import os
from edge_impulse_linux.audio import AudioImpulseRunner

# Edge ML with the Edge Impulse Python SDK
class EdgeML:
    DEFAULT_MODEL = "/home/pi/.ei-linux-runner/models/128115/v1/model.eim"
    DEFAULT_LABEL = "listen"
    DEFAULT_THRESHOLD = 0.85

    def __init__(self, model = DEFAULT_MODEL):
      self.model = model

      dir_path = os.path.dirname(os.path.realpath(__file__))
      modelfile = os.path.join(dir_path, model)

      self.runner = AudioImpulseRunner(modelfile)
      model_info = self.runner.init()
      print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '" . Labels: ' + str(model_info['model_parameters']['labels']))

    # Run the keyword spotting model until the desired label is detected
    def wait_for_keyword(self, label=DEFAULT_LABEL, threshold=DEFAULT_THRESHOLD, device_id=5):
        with self.runner as runner:
            try:
                model_info = runner.init()
                for res, audio in runner.classifier(device_id = device_id):
                    if res['result']['classification'][label] > threshold:
                        return True

            finally:
                if (runner):
                    runner.stop()

        return False