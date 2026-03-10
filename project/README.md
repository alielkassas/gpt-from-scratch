# Build Your Own GPT from Scratch

Congratulations! You have reached the final stage of the course. Now that you understand the internals of the **Transformer architecture**—from self-attention and layer normalization to residuals and feed-forward blocks—it is time to apply that knowledge to a real-world problem.

## Project Overview

The goal of this project is to implement, pretrain, fine tune GPT (*Decoder-Only Transformer architecture*) entirely from scratch using PyTorch. You will handle data preprocessing, build the neural network layers (Attention, MLP, LayerNorm), write the training loop, and generate text.

## Learning Objectives

- Understand Tokenization (Byte-Pair Encoding).
- Implement Self-Attention and Multi-Head Attention mechanisms.
- Master the Training Loop (Gradient Descent, Backpropagation).
- (Bonus) Handle Multi-language Data (specifically UTF-8/Arabic support).
- Evaluate model performance using Loss Curves and Text Generation.

---

## Data Requirements & Examples

This project consists of two distinct phases. You must prepare data for both phases to demonstrate the full lifecycle of an LLM.

### Phase 1: Pretraining Data (Base Model)
**Goal:** Teach the model the structure of the language (Next Token Prediction).  
**Format:** Raw text file (`.txt`).  
**Encoding:** `UTF-8` (Critical for Arabic support).

| Requirement | Specification |
| :--- | :--- |
| **Minimum Size** | **1,000 lines** of text OR **2 MB** of raw text. |
| **Content** | Cleaned text (remove excessive HTML, special chars). |
| **Language** | English, Arabic, or Mixed. |

#### Pretraining Data Examples
```
تتطلب نماذج التعلم الآلي مجموعات بيانات كبيرة لتعمل بفعالية.
...
```

### Phase 2: Supervised Fine-Tuning (SFT) Data
**Goal:** Teach the model to follow instructions and complete tasks.  
**Format:** JSON Lines (`.jsonl`) or JSON list.  
**Structure:** Each record must contain an `instruction`, optional `input`, and a `output`.

| Requirement | Specification |
| :--- | :--- |
| **Minimum Samples** | **200 unique instruction-response pairs**. |
| **Quality** | High quality, diverse instructions (Q&A, Summarization, Translation). |
| **Language** | Must match the target language of your model. |

#### SFT Data Examples (`sft_data.json`)
```
[
  {
    "instruction": "ترجم إلى الإنجليزية.",
    "input": "مرحباً، كيف حالك؟",
    "output": "Hello, how are you?"
  },
  {
    "instruction": "اكتب شعراً عن القهوة.",
    "input": "",
    "output": "يا قهوة الصباح يا رائحة العمر ... أنتِ في قلبي سكنى ومستقر"
  }
]
```

---

## Project Examples

To demonstrate the model's versatility, you are encouraged to train or test on Arabic corpora. Below are examples for your final demo.

1. Local (Khaligi) Dialect: Train the model to understand and generate Gulf Arabic dialect (Saudi, Kuwaiti, Emirati, etc.).
2. Poetry: Train the model to generate rhyming verses.
3. Stories:Train the model to generate coherent narratives with a beginning, middle, and end.

---

## Project Rubric (Total: 100 Points)
Your project will be graded out of 100 Points based on the following criteria:

| Category | Weight | Criteria |
| :--- | :--- | :--- |
| **Data & Tokenization** | 20 pts | Cleanliness of the dataset; logic behind the chosen vocabulary size; handling of Arabic diacritics/normalization. |
| **Linguistic Versatility (Bonus)** | 10 pts | Native support for Arabic or a multilingual framework optimized for the Arabic script. |
| **Model Architecture** | 10 pts | Correct implementation of the Transformer blocks (Attention, Residuals, Norms). Evidence of "training from scratch." |
| **Training & Optimization** | 10 pts | Analysis of the loss curve; addressing overfitting; choice of hyperparameters (Learning Rate, Batch Size). |
| **Text Generation** | 15 pts | Quality of generated text ( coherent, fluent, grammatically correct).|
| **Evaluation** | 25 pts | Calculating Perplexity, using LLM as a judge, verifying that generated text follows instructions accurately, and providing a report identifying failure modes (e.g., repetition or context loss)..|
| **Deployment (Bonus)** | 10 pts | (Bonus) A functional interface (Streamlit/Gradio) that allows users to test the model in real-time. |
| **Documentation & Recorded Demo** | 20 pts | A clear README explaining the project phases and the technical limitations of the model. |

---

## Demo Requirements

```
1. Introduction
   - Project overview
   - Data summary

2. Pre-trained Model Demo
   - text generation (3 examples)
   - Show strengths/weaknesses

3. Fine-tuned Model Demo
   - Task 1 demonstration (with comparison)
   - Task 2 demonstration (with comparison)

4. Evaluation Results
   - Key metrics
   - Sample generations
   - Error analysis highlights

5. Conclusion
   - Key learnings
   - Future work
```

---

## Project Structure
The recommended structure for your repo is as follows:
```
gpt-from-scratch/
├── data/
│   ├── pretrain/
│   │   └── data.txt
│   └── finetune/
│       ├── story_completion/
│       └── poetry/
├── src/
│   ├── model/
│   │   ├── transformer.py
│   │   ├── attention.py
│   ├── tokenizer/
│   │   ├── bpe_tokenizer.py
│   │   └── vocab.py
│   ├── training/
│   │   ├── pretrain.py
│   │   ├── finetune.py
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── human_eval.py
│   │   └── error_analysis.py
│   └── demo/
│       ├── app.py
│       ├── interface.py
│       └── static/
├── checkpoints/
│   ├── pretrained/
│   └── finetuned/
├── results/
│   ├── sample_generations/
│   └── plots/
├── demo/
│   ├── recording/
│   └── screenshots/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_evaluation.ipynb
├── requirements.txt
└── README.md
```