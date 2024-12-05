# Spelling correction: usage demo
#
# @author Emilio Garzia, 2024

from spelling_correction.SpellingCorrector import SpellCorrector, reuters_vocabulary

# Driver code
if __name__ == "__main__":
    query = "Iranin financal banks are strongss"

    corrector = SpellCorrector(string=query, vocabulary=reuters_vocabulary)
    corrected_query = corrector.retrive_corrected()

    print(f"Query before correction: {query}")
    print(f"Query after correction: {corrected_query}")
