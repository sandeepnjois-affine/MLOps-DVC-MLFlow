import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/sandeepnjois-affine/MLOps-DVC-MLFlow.mlflow")

dagshub.init(repo_owner='sandeepnjois-affine', repo_name='MLOps-DVC-MLFlow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)