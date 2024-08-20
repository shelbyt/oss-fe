## Modify Params for Deploy
Go to .streamlit/examples.toml and change base url to be the endpoint. It must end with /v1.
Change the model_name to be the model name from the docker-compose file.

```
[inference_params]
base_url = "http://localhost:9001/v1"
model_name = "meta-llama-3.1-8b-instruct"
```


## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Home.py
```