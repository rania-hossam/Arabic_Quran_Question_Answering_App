# Readme for Quran Question Answering System

## Overview

This repository presents a Quran Question Answering System developed using Python and Streamlit. It utilizes a fine-tuned version of the "wissamantoun/araelectra-base-artydiqa" model to provide answers to questions based on context from the Quran.

## Features

- Efficient question answering using Quranic context.
- User-friendly web interface powered by Streamlit.
- Harnesses advanced NLP models for precise responses.

## Installation

To set up this project, follow the steps below:

1. **Clone the Repository:**
    ```bash
    git clone [your-repository-link]
    cd Arabic_Quran_QA
    ```

2. **Install Dependencies:**
   Ensure that you have Python installed on your system. Then install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To launch the Streamlit app, use the following command:
```bash
streamlit run your_streamlit_app.py
```
Replace `your_streamlit_app.py` with the actual name of your main Streamlit script file.

## Docker Support

You can also run this application as a Docker container:

1. **Build the Docker Image:**
    ```bash
    docker build -t streamlit-app .
    ```

2. **Run the Docker Container:**
    ```bash
    docker run -p 8501:8501 streamlit-app
    ```

## Contributing

Contributions to this project are encouraged. Please fork the repository and submit a pull request with your modifications.

## License

[Specify your license or state that it's unlicensed.]

## Instructions for Use

- Replace `[your-repository-link]` with the actual link to your GitHub repository.
- Update any file names, commands, or additional instructions specific to your project setup.
- Choose an appropriate license for your project or explicitly state if it's unlicensed.
