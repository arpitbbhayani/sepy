import re


def cleanse(text):
    """Given a string `text`, the function should return
    another a "cleansed" string that you want to pass to
    a tokenizer.

    Ex: given a string "{{Hi! I'm Harry Potter. Nice to meet you]]"
    convert it to

    "hi im harry potter nice to meet you"

    You need to do the following
      - case-folding
      - decide which characters are junk and remove them
    """
    return re.sub(r'[^a-zA-Z0-9]', ' ', text.lower())
