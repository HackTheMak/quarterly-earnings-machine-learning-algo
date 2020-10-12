import os
import glob
import pandas as pd
import dask.dataframe as dd

from google.api_core.client_options import ClientOptions
from google.cloud import automl
from google.cloud import storage

# To overcome the Python "self" oddity for passing values in Predict()
project_id = "InsertYourProjectID"
model_id = "InsertYourModelID"
# For Credentials to access Google
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/InsertPathHere/InsertFilenameHere.json"


class AutoMLPredictor:

  def __init__(self, model_name):
    self.client = storage.Client()
    self.model_name = model_name

  def __inline_text_payload(self, content):
    return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

  def get_prediction(self, text, model_name=None):
    if model_name is None:
      model_name = self.model_name

    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(client_options=options)
    model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

    payload = self.__inline_text_payload(text)

    params = {}
    request = automl.PredictRequest(
      name = model_full_id,
      payload = payload,
      params = params
    )
    response = prediction_client.predict(request=request)
    prtt = "Response"
    print(prtt)
    print(request.payload[0].text_sentiment.sentiment)
    return request.payload[0].text_sentiment.sentiment  # waits until request is returned


def main():
  pass

if __name__ == "__main__":
    main()
