# Cancer Gene Prediction using PPI Network Topology Data

This project focuses on predicting cancer genes based on protein-protein interaction (PPI) network topology data using machine learning techniques. The goal of this project is to identify genes that play a crucial role in cancer progression by analyzing their interactions with other proteins in the cell.

## Project Overview

The project involves the following steps:

1. Data collection: Collecting PPI network topology data from various sources, such as STRING, BioGRID, and HPRD.

2. Data preprocessing: Cleaning and filtering the PPI network topology data to remove noise and redundancy.

3. Feature extraction: Extracting topological features of genes from the PPI network topology data.

4. Model training: Using machine learning models to train on the extracted features.

5. Model evaluation: Evaluating the performance of the trained models using various metrics, such as accuracy, precision, recall, and F1 score.

6. Gene prediction: Predicting cancer genes based on the trained models and the extracted features.

## Project Structure

The project has the following structure:

- **Data folder:** Contains the data files that will be used in the project.
- **Notebooks folder:** Contains the Jupyter notebook files that are used for data analysis, preprocessing, feature extraction, model training, and evaluation.
- **Models folder:** Contains the trained models, saved in various formats such as pickle, TensorFlow saved model, Keras model, PyTorch model, etc.
- **Utils folder:** Contains the utility functions or classes that are used in the project.
- **README.md file:** A markdown file that provides a brief overview of the project and its structure.

## Setup and Requirements

To run this project, you need to have Python 3.x installed on your system along with the following libraries:

- Jupyter Notebook (for running the notebooks)
- Pandas (for data analysis)
- NumPy (for numerical computations)
- Scikit-Learn (for machine learning models)
- TensorFlow/Keras/PyTorch (for deep learning models)

You can install these libraries using pip or conda package manager.

## Getting Started

To get started, clone this project repository to your local machine using the command:

```bash
git clone https://github.com/kulsumkamal/Cancer-Gene-Prediction.git
```

Next, navigate to the project directory using the command:

```bash
cd your-repository-name
```

Then, launch the Jupyter notebook using the command:

```bash
jupyter notebook
```

This will open the Jupyter notebook interface in your web browser. From there, navigate to the "Notebooks" folder and open any notebook of your choice to get started with the project.

## License

This project is licensed under the MIT License. Feel free to modify and use it for your own projects.
