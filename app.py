from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
import gradio as gr

IMAGE_SIZE = 128
THRESHOLD = 0.50
MODEL_PATH = Path(__file__).with_name("best_final_model.keras")
model = tf.keras.models.load_model(MODEL_PATH)

def predict_xray(image):
    if image is None:
        return {"No lung opacity": 0.0, "Lung opacity": 0.0}, "Please upload an image."
    gray = image.convert("L").resize((IMAGE_SIZE, IMAGE_SIZE))
    array = np.asarray(gray, dtype=np.float32) / 255.0
    batch = array[None, ..., None]
    positive_score = float(model.predict(batch, verbose=0)[0, 0])
    negative_score = 1.0 - positive_score
    predicted = "Lung opacity" if positive_score >= THRESHOLD else "No lung opacity"
    note = (
        f"Prediction: {predicted}. Score={positive_score:.3f}. "
        "Educational prototype only - not for medical diagnosis."
    )
    return {"No lung opacity": negative_score, "Lung opacity": positive_score}, note

demo = gr.Interface(
    fn=predict_xray,
    inputs=gr.Image(type="pil", label="Upload chest X-ray"),
    outputs=[gr.Label(num_top_classes=2, label="Model scores"), gr.Textbox(label="Result")],
    title="Pneumonia / Lung Opacity Screening Demo",
    description="Upload a chest X-ray. This educational model does not replace clinical assessment."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
