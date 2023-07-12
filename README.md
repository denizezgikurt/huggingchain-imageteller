# huggingchain-imageteller

A Streamlit app that turns any uploaded image to an audio story.

Requires:
Transformers,
Tensorflow or Pytorch,
Langchain,
Python-dotenv,
Streamlit.

# huggingchain-imageteller

A Streamlit app that turns any uploaded image to an audio story.

Requires:
Transformers ,
Tensorflow or Pytorch,
Langchain,
Python-dotenv,
Streamlit.


# [Transformers](https://huggingface.co/docs/transformers/installation): 
Install 🤗 Transformers for whichever deep learning library you’re working with, setup your cache, and optionally configure 🤗 Transformers to run offline.

PyTorch[ installation instructions.](https://pytorch.org/get-started/locally/)
TensorFlow 2.0 [installation instructions.](https://www.tensorflow.org/install/pip)https://www.tensorflow.org/install/pip

Install with pip
You should install 🤗 Transformers in a virtual environment. If you’re unfamiliar with Python virtual environments, take a look at this guide. A virtual environment makes it easier to manage different projects, and avoid compatibility issues between dependencies.

Start by creating a virtual environment in your project directory:

`python -m venv .env`

Activate the virtual environment. On Linux and MacOs:
`source .env/bin/activate`

Activate Virtual environment on Windows

`.env/Scripts/activate`


Now you’re ready to install 🤗 Transformers with the following command:
`pip install transformers`


# [Langchain](https://python.langchain.com/docs/get_started/installation): 

PIP: 
`pip install openai`

`pip install langchain`

To install modules needed for the common LLM providers, run:

`pip install langchain[llms]`

To install all modules needed for all integrations, run:

`pip install langchain[all]`

Note that if you are using zsh, you'll need to quote square brackets when passing them as an argument to a command, for example:

`pip install 'langchain[all]'`

CONDA:
`conda install langchain -c conda-forge`

# [Dotenv](https://pypi.org/project/python-dotenv/): 

`pip install python-dotenv`

# [Streamlit](https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-macoslinux)

`pip install streamlit`


# RUN the app:

* to run in terminal:
`python3 app.py`
or
`python app.py`

* to run locally in Streamlit:
`streamlit run app.py`

