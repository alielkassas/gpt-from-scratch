# Optional Setup Instructions


This document lists different approaches for setting up your machine and using the code in this repository. I recommend browsing through the different sections from top to bottom and then deciding which approach best suits your needs.

&nbsp;

## Quickstart

If you already have a Python installation on your machine, the quickest way to get started is to install the package requirements from the [../requirements.txt](../requirements.txt) file by executing the following pip installation command from the root directory of this code repository:

```bash
pip install -r requirements.txt
```

<br>

> **Note:** If you are running any of the notebooks on Google Colab and want to install the dependencies, simply run the following code in a new cell at the top of the notebook:
> `pip install uv && uv pip install --system -r https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/requirements.txt`
> Optionally, after cloning the repository, you install the dependencies for all bonus materials with `uv pip install --group bonus` from the project root. This is useful if you don't want to install them separately as you check out the optional bonus materials later on.



In the video below, Raschka share my personal approach to setting up a Python environment on my computer:

<br>
<br>

[![Link to the video](https://img.youtube.com/vi/yAcWnfsZhzo/0.jpg)](https://www.youtube.com/watch?v=yAcWnfsZhzo)


&nbsp;
# Local Setup

This section provides recommendations for running the code in this book locally. Note that the code in the main chapters of this book is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware. I tested all main chapters on an M3 MacBook Air laptop. Additionally, if your laptop or desktop computer has an NVIDIA GPU, the code will automatically take advantage of it.

&nbsp;
## Setting up Python

If you don't have Python set up on your machine yet, Raschka have written about his personal Python setup preferences in the following directories:

- [01_optional-python-setup-preferences](./01_optional-python-setup-preferences)
- [02_installing-python-libraries](./02_installing-python-libraries)

The *Using DevContainers* section below outlines an alternative approach for installing project dependencies on your machine.

&nbsp;



## Visual Studio Code Editor

There are many good options for code editors. My preferred choice is the popular open-source [Visual Studio Code (VSCode)](https://code.visualstudio.com) editor, which can be easily enhanced with many useful plugins and extensions (see the *VSCode Extensions* section below for more information). Download instructions for macOS, Linux, and Windows can be found on the [main VSCode website](https://code.visualstudio.com).

&nbsp;

## VSCode Extensions

If you are using Visual Studio Code (VSCode) as your primary code editor, you can find recommended extensions in the `.vscode` subfolder. These extensions provide enhanced functionality and tools helpful for this repository.

To install these, open this "setup" folder in VSCode (File -> Open Folder...) and then click the "Install" button in the pop-up menu on the lower right.

<img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/setup/README/vs-code-extensions.webp?1" alt="1" width="700">

Alternatively, you can move the `.vscode` extension folder into the root directory of this GitHub repository:

```bash
mv setup/.vscode ./
```

Then, VSCode automatically checks if the recommended extensions are already installed on your system every time you open the `LLMs-from-scratch` main folder.

&nbsp;

# Cloud Resources

This section describes cloud alternatives for running the code presented in this book.

While the code can run on conventional laptops and desktop computers without a dedicated GPU, cloud platforms with NVIDIA GPUs can substantially improve the runtime of the code, especially in chapters 5 to 7.

&nbsp;


## Using Google Colab

To use a Google Colab environment in the cloud, head over to [https://colab.research.google.com/](https://colab.research.google.com/) and open the respective chapter notebook from the GitHub menu or by dragging the notebook into the *Upload* field as shown in the figure below.

<img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/setup/README/colab_1.webp" alt="1" width="700">


Also make sure you upload the relevant files (dataset files and .py files the notebook is importing from) to the Colab environment as well, as shown below.

<img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/setup/README/colab_2.webp" alt="2" width="700">


You can optionally run the code on a GPU by changing the *Runtime* as illustrated in the figure below.

<img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/setup/README/colab_3.webp" alt="3" width="700">


&nbsp;
