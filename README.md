# Pneumonia Detection Gradio App

Selected model: VGG16_Enhanced_FineTuned

## Run locally
1. `pip install -r requirements.txt`
2. `python app.py`
3. Open `http://localhost:7860`

## Run with Docker
1. `docker build -t pneumonia-app .`
2. `docker run -p 7860:7860 pneumonia-app`
3. Open `http://localhost:7860`

## GitHub Codespaces
1. Create a GitHub repository and run `git lfs install`.
2. Run `git lfs track "*.keras"`, then add and push all deployment files.
3. Open the repository in GitHub Codespaces.
4. Run the Docker build and run commands above.
5. In the Codespaces Ports panel, set port 7860 visibility as required.
6. Open the forwarded URL and make a test inference.

Educational prototype only. Not for medical diagnosis.
