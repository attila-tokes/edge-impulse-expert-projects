FROM mcr.microsoft.com/azureml/pytorch-1.10-ubuntu18.04-py37-cpu-inference:latest

RUN conda list -p $AZUREML_CONDA_ENVIRONMENT_PATH

# Install pip dependencies
RUN pip install 'transformers' \
                'matplotlib>=3.3,<3.4' \
                'psutil>=5.8,<5.9' \
                'tqdm>=4.59,<4.63' \
                'pandas>=1.3,<1.4' \
                'scipy>=1.5,<1.8' \
                'numpy>=1.10,<1.22' \
                'ipykernel~=6.0' \
                # upper bound azure-core to address typing-extensions conflict
                'azure-core<1.23.0' \
                'azureml-core==1.43.0' \
                'azureml-defaults==1.43.0' \
                'azureml-mlflow==1.43.0.post1' \
                'azureml-telemetry==1.43.0'

# This is needed for mpi to locate libpython
ENV LD_LIBRARY_PATH $AZUREML_CONDA_ENVIRONMENT_PATH/lib:$LD_LIBRARY_PATH