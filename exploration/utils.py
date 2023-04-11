import string
from collections import Counter

def replace_punctuation_with_space(text):
    # Create a translation table with punctuation replaced by spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    # Use the translation table to replace punctuation with spaces
    return text.translate(translator)


def get_ocm_counts(df, id_to_category=None, limit=626):
    ocms_list = df['ocms'].str.split(expand=True).values.ravel()
    ocms_list = [id_to_category[int(i)] if id_to_category else int(i) for i in ocms_list if i and int(i) <= limit]
    ocms_counts = Counter(ocms_list)
    return ocms_counts


def make_id_category(ocms, label_to_id):
    id_to_category = {000: 000}
    for item in ocms:
        category, values = list(item.items())[0]
        cat_id = label_to_id[category]

        id_to_category[cat_id] = cat_id
        for x in values:
            id_to_category[int(x[0])] = cat_id
    return id_to_category