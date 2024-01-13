# model-deployment-workshop

1. Create a new repository if not created already

2. Setup environment
    1. Install asdf using this [guide](https://asdf-vm.com/guide/getting-started.html)
    2. Create python environment
        ```
        > python -m venv ml
        > chmod +x deployment/bin/activate
        > source deployment/bin/activate
        ```
    3. Install packages
        ```
        pip install -r requirements.txt
        ```

3. Train model (if `mode)l.pkl` file is not saved in `model/`)
    ```
    cd tabular
    python model.py
    ```


4. Run the app locally
    1. Run flask app
        ```
        cd tabular
        python api.py
        ```
    2. Run the streamlit app
        ```
        streamlit run ui.py
        ```

5. Run the app locally using Docker
    1. Install docker(skip if already installed)
        - [Steps to install Docker on your system](https://docs.docker.com/engine/install/ubuntu/)
        
    1. Create docker image
        ```
        docker build -t ml_deployment .
        ```
    2. Run docker container
        ```
        docker run -d -p 8501:8501 -p 5000:5000 ml_deployment
        ```