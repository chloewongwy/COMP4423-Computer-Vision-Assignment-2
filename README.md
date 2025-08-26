# COMP4423 Computer Vision Assignment 2

This repository contains the implementation and report for **COMP4423 Computer Vision Assignment 2**.  
The project explores **CNN architectures (ResNet vs VGG, Deformable CNNs)** and **3D scene reconstruction with Tiny NeRF**, including ray sampling and volume rendering.

## 📅 Project Info  
- Developed: March 2025  

---

## 📂 Project Structure

```
src/
│── dCNN.py/               # Implementation of Deformable CNNs
│── Raysampling.py/        # Ray sampling (uniform + stratified) for NeRF
│── ResNetvsVGG.py/        # Comparison of ResNet18 and VGG16 (gradient flow + loss landscape)
│── Tiny_nerf.ipynb/          # Tiny NeRF implementation and experiments
│── Volumne_rendering.py/  # Volume rendering functions and visualization
report.pdf              # Detailed assignment report with results and explanations
COMP4423 Assignment 2 - requirements.pdf        # Assignment specification
```

---

## 🚀 Features

- **ResNet vs VGG**:  
  - Gradient flow visualization  
  - Loss landscape visualization  
  - Comparison and analysis of optimization behavior  

- **Deformable CNN (dCNN)**:  
  - Custom offset convolution implementation  
  - Explanation of channel requirements  

- **NeRF (Neural Radiance Fields) Components**:  
  - Ray sampling (uniform & stratified)  
  - Volume rendering (opacity, transmittance, weights)  
  - Tiny NeRF training & improvement (hidden layer size modification)  

- **Visualizations**:  
  - Loss landscapes  
  - Gradient flow plots  
  - Sampling strategies  
  - Volume rendering curves  
  - NeRF rendered scenes

---

## 📖 Report

A full explanation of methods, results, and visualizations can be found in [`report.pdf`](./report.pdf).


## ▶️ Usage

Each part of the assignment is implemented in separate folders under `src/`.  
You can run individual modules as follows:

```bash
# Run Deformable CNN
python src/dCNN.py

# Run Ray Sampling
python src/Raysampling.py

# Run ResNet vs VGG comparison
python src/ResNetvsVGG.py

# Run Volume Rendering
python src/Volumne_rendering.py

# Open Tiny_nerf.ipynb in Jupyter Notebook or VS Code and execute the cells step by step:
jupyter notebook src/Tiny_nerf.ipynb

```

---

## 📌 Requirements

- Python 3.8+  
- PyTorch  
- torchvision  
- numpy  
- matplotlib  
- loss-landscapes  
