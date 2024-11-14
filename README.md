# Dog Breed Classifier

![Image](./Image.png)

## Overview
Dog Breed Classifier is a machine learning-powered application that identifies the breed of a dog based on its image. The project leverages the ResNet model for accurate classification and provides an intuitive interface for users to upload images and view results.

---

## Features
- Upload a dog image to classify its breed.
- Simple and user-friendly interface.
- Uses state-of-the-art ResNet architecture for predictions.

---

## Preview
Here’s a preview of the application interface:

![Website Screenshot](./Image1.png)

---

## Project Structure
- **`app.py`**: Main application file to run the Flask web app.
- **`static/uploads/`**: Directory to store uploaded images temporarily.
- **`templates/`**: Contains HTML templates for the app.
- **`data/`**: Includes additional scripts and resources such as `classifier.py`, test data, and supporting files.

---

## Getting Started
### Prerequisites
- Python 3
- Flask
- torchvision

How It Works
1. Users upload an image of a dog.
2. The application processes the image using a pre-trained ResNet model.
3. The breed of the dog is displayed alongside the uploaded image.

Technologies Used
- Python: For backend development.
- Flask: Lightweight framework to build the web application.
- ResNet: Pre-trained neural network for image classification.

Future Enhancements
- Add support for multiple models.
- Improve classification accuracy for mixed-breed dogs.
- Create a mobile version of the application.

## Website
[Dog Breed Classifier Website](https://astrotech-666.github.io/dog-breed-classifier)

---

## Author
Developed by **Farzana**  
GitHub: [AstroTech-666](https://github.com/AstroTech-666)
