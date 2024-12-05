<!-- toc start: 3 [do not erase this comment] -->
**Table of contents**
- [Spelling Correction](#spelling-correction)
- [How to use](#how-to-use)
- [Possible improvements](#possible-improvements)
- [Dependencies](#dependencies)
- [Author](#author)
<!-- toc end [do not erase this comment] -->

# Spelling Correction

This repository provides an implementation of a Spell Checker leveraging the power of NLTK and NumPy. The project is designed to efficiently detect and correct spelling errors in text using probabilistic models and distance-based algorithms. This project is divided in two different python source code, one dedicated to the `Levenshtein edit distance` and the other to apply the **Spelling correction** using: *preprocessing, Levenshtein edit distance* and a *naive probability approach*.

# How to use

```python
from spelling_correction.Levenshtein import levenshtein
edit_distance_calculator = levenshtein(source="play", target="stay")
levenshtein_matrix = edit_distance_calculator.distance_matrix
```
> `Levenshtein.py`


```python
from spelling_correction.SpellingCorrector import SpellCorrector
query = "Iranin financal banks are strongss"
corrector = SpellCorrector(string=query)
corrected_query = corrector.retrive_corrected()
```
> `SpellingCorrector.py`

# Possible improvements

Could be interesting implements different probability computation into the `__compute_probabilities__(self)` of the class `SpellCorrector`, current implementation is a very naive solution to compute the words probability. I suggest to try implement others approach, such that *[Kernighan](https://aclanthology.org/C90-2036.pdf)*, *[Noisy Channel model](https://aclanthology.org/D08-1025.pdf)*

# Dependencies

* [NLTK](https://www.nltk.org/)
* [Numpy](https://numpy.org/)

# Author

*Emilio Garzia, 2024*
