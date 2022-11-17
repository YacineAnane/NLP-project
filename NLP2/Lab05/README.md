### Project Summary
In this lab, we are implementing four different decoding approaches that will be used in combination with a well-trained translation model (DEUTSCH to ENGLISH).

The four decoding approaches will be used to provide different final translations of different qualities, and are the following:
- Greedy decode (simplest decoding function, only takes the most probable translation for each token to translate)
- Top-k decode (For each token to translate, randomly chooses between the k most probable translations)
- Top-k decode (Same as top-k but uses temperature to exacerbate existing probabilities: high probabilities becomes higher etc. The effect is null at temperature=1.0, and strongest when close to 0.0)
- Beam Search decode (A powerful approach that parallelize "beam_width" different translations and keep the "beam_width" most probable ones)

After testing these 4 approaches, we will use the BLEU scoring system to (approximately) see how accurate each approach is.

### Architecture
Everything can be found in the notebook named : 'NLP_lab05.ipynb'.