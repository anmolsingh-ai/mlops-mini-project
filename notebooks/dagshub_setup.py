import mlflow
import dagshub

mlflow.set_tracking_uro("https://dagshub.com/anmolsingh-ai/mlops-mini-project.mlflow")
dagshub.init(repo_owner='anmolsingh-ai', repo_name='mlops-mini-project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)