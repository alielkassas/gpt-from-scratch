# GPT From Scratch  
## Build a GPT-Style Large Language Model in PyTorch — Step by Step

> A complete hands-on course for understanding, building, pretraining, and fine-tuning Large Language Models — without relying on high-level abstractions.

---

<p align="center">
  <b>Understand Transformers.</b>  
  <b>Implement Attention.</b>  
  <b>Train GPT.</b>  
  <b>Fine-Tune for Real Tasks.</b>
</p>

---

## Course Outline

| Module | Title | Core Topics | Hands-On Outcome |
|--------|--------|------------|------------------|
| 0 | **Deep Learning, PyTorch , and Linear Algebra Recap** | backprob, activations, Tensors, autograd, nn.Module, optimizers, GPU training, model saving/loading, matrixmultiplication | Recap PyTorch & Deep Learning foundations |
| 1 | **Understanding Large Language Models** | Next-token prediction, tokens & embeddings, Transformer intuition, GPT overview, scaling laws | Strong conceptual understanding of how LLMs work |
| 2 | **Working With Text Data** | Tokenization, vocabulary building, encoding/decoding, PyTorch Dataset & DataLoader, batching | Convert raw text into training-ready tensors |
| 3 | **Coding Attention Mechanisms** | Scaled dot-product attention, QKV math, causal masking, multi-head attention, Transformer block | Implement attention from scratch in PyTorch |
| 4 | **Implementing a GPT Model From Scratch** | Token & positional embeddings, stacked Transformer blocks, residual connections, layer norm, output head, sampling strategies | Build and train a mini GPT-style model |
| 5 | **Pretraining on Unlabeled Data** | Self-supervised learning, cross-entropy loss, training loops, optimization, checkpointing | Pretrain a language model on raw text |
| 6 | **Fine-Tuning for Classification** | Transfer learning, classification head, freezing vs full fine-tuning, evaluation metrics | Adapt GPT for sentiment or text classification |
| 7 | **Fine-Tuning to Follow Instructions** | Instruction datasets, prompt formatting, supervised fine-tuning (SFT), loss masking | Build an instruction-following mini-LLM |


---

## How to Approach This Course

The notebooks in this course **build upon each other sequentially**, guiding you from foundational concepts to advanced LLM implementation.  

> 💡 **Pro tip:** If you are already familiar with **Deep Learning, Linear Algebra, and PyTorch basics**, you can safely skip the first module and jump to the sections that interest you most.


To get the most out of this learning experience — We recommend learn by doing, experimenting, and visualizing (inspired by [Learn PyTorch](https://www.learnpytorch.io/) book):

<p align="center">
  <img src="https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/images/docs-how-to-approach-this-course-no-header.png" width="300" alt="Build a Large Language Model From Scratch Book Cover">
</p>


1. **Code Along First**  
   Run and write the code yourself — this builds muscle memory and confidence.

2. **Explore and Experiment**  
   Try variations and small changes to see how behavior differs. Deep learning is highly experimental.

3. **Visualize What You Don’t Understand**  
   Plot attention scores, masks, losses, embeddings — visual intuition accelerates understanding.

4. **Ask Questions Early**  
   If something isn’t making sense, search for answers, ask peers, reach us or open discussions.

5. **Complete the Exercises**  
   Each section includes exercises designed to solidify core ideas.

6. **Share Your Work**  
   Share notebooks, results, and insights — teaching others reinforces your own knowledge.

---

## Acknowledgment

This course is built loosely on [*Build a Large Language Model (From Scratch)* book](https://learning.oreilly.com/library/view/build-a-large/9781633437166/) by Sebastian Raschka.

<p align="center">
  <img src="https://m.media-amazon.com/images/I/71eljkULtwL._SY385_.jpg" width="300" alt="Build a Large Language Model From Scratch Book Cover">
</p>

This is the official code [repository](https://github.com/rasbt/LLMs-from-scratch). The author also provides [video content](https://www.youtube.com/playlist?list=PLTKMiZHVd_2IIEsoJrWACkIxLRdfMlw11) explaining the book concepts. We strongly encourage supporting the author by purchasing the book, star the official repo and watching the official videos.

 
This repository is an independent educational project that:

- Follows similar concepts/notebooks
- Supplies support materials for each subject
- Adds additional DL, Linear Algebra, and PyTorch recaps  
- Includes expanded fine-tuning and instruction-tuning sections (future) 

This course exists to deepen understanding and provide supportive materials — while respecting and crediting the original source.