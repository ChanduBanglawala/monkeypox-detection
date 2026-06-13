Monkeypox Detection System 🦠

This project is a Deep Learning-based medical image classification system that detects Monkeypox from skin lesion images using a VGG16 Transfer Learning model.

Features
Upload skin lesion images
Real-time Monkeypox detection
Confidence score prediction
User-friendly Streamlit interface
Transfer Learning using VGG16
Image preprocessing and augmentation
Model Performance
Model	Accuracy
Custom CNN	53.09%
VGG16 Transfer Learning	91.15%
Technologies Used
Python
TensorFlow / Keras
VGG16
NumPy
PIL
Streamlit
Google Colab
Dataset

The model was trained on the Monkeypox Skin Image Dataset from Kaggle https://www.kaggle.com/datasets/dipuiucse/monkeypoxskinimagedataset

Project Workflow
Data Collection
Image Preprocessing
Data Augmentation
Model Training
Transfer Learning with VGG16
Model Evaluation
Streamlit Deployment
Results

The VGG16 Transfer Learning model significantly outperformed the Custom CNN model, achieving 91.15% validation accuracy, demonstrating the effectiveness of transfer learning on limited medical image datasets.
<img width="582" height="455" alt="image" src="https://github.com/user-attachments/assets/64598ef1-c471-46e4-9678-f528019872a1" />
<img width="573" height="455" alt="image" src="https://github.com/user-attachments/assets/e909dd82-88a7-4ac6-9fbe-b0f8ec4eb0d6" />



Disclaimer

This project is intended for educational and research purposes only and should not be used as a substitute for professional medical diagnosis.
## Model File

The trained model file is not included in this repository because it exceeds GitHub's file size limits (100 MB).


### Download Model

Download the trained VGG16 model from Google Drive:

[https://drive.google.com/file/d/1rEJSN7wjqt2baztmEmbblgYFxMTzJ3ep/view?usp=sharing](https://drive.google.com/file/d/1qwum--of28CM2Bqn6msVJLwXVMXCGic1/view?usp=sharing)

### About the Model File

**File Name:** `monkeypox_vgg16.keras`

**Contents:**

* Trained VGG16 Transfer Learning model
* Learned weights and biases
* Model architecture
* Binary classification configuration (Monkeypox vs Normal)

### Model Performance

* Validation Accuracy: **91.15%**
* Architecture: **VGG16 Transfer Learning**
* Input Image Size: **224 × 224 × 3**

### Usage

After downloading the model file, place it in the project root directory:

```
Monkeypox-Detection/
│
├── app interface of monkey pox.py
├── monkeypox_vgg16.keras
├── requirements.txt
└── README.md
```

Then run:

```bash
streamlit run app.py
```

Output Results:
Result for normal person
<img width="1366" height="943" alt="image" src="https://github.com/user-attachments/assets/fcf27b1d-5ce8-4212-b4ca-5af905593af3" />

Result for monkeypox person
<img width="1366" height="943" alt="monkey pox result" src="https://github.com/user-attachments/assets/4ec40a89-2073-4576-8a91-9cc7f312f431" />
