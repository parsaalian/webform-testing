# Webform testing
Source code for webform testing automation project

# Setup environment
- Install conda package manager.
- Create python environment with required dependencies

```
Create The following steps create an isolated environment webform-env and install required dependencies.
conda create --name webform-env python=3.9 # creates the webform-env environment
conda activate webform-env                 # activates the codex-env environment

conda install openai                       # installs dependency - openai
conda install -c conda-forge python-dotenv
conda install -c anaconda beautifulsoup4
conda install -c conda-forge selenium
conda install notebook
pip install webdriver-manager
```

# Subjects - dockerized-webapps
[Opensource Apps](https://github.com/parsaalian/dockerized-webapps/tree/parsa-apps)
- Use branch `parsa-apps`

# Subjects
[Opensource Apps](https://github.com/unicodeveloper/awesome-opensource-apps)

# Approach
![Fine-grained context selection](./images/method-flow.jpeg)

# Models
- [BLIP](https://huggingface.co/docs/transformers/main/model_doc/blip) for get context from image to text 
- [MarkupLM](https://github.com/microsoft/unilm/tree/master/markuplm) to understand the web page layout better
