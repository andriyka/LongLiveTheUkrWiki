def split_list(list_for_split, number_of_partitions):
    """
    Splits list into approximately equal size sublists
    :param list_for_split: original list
    :param number_of_partitions: number of parts to split list into
    :return:
    """
    k, m = divmod(len(list_for_split), number_of_partitions)
    return (list_for_split[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(number_of_partitions)
            if list_for_split[i * k + min(i, m):(i + 1) * k + min(i + 1, m)])


def extract_chunks(l, s):
    """
    Extract chunks of the specified size from list
    :param l: list to split
    :param s: chunk size
    :return: list of chunks
    """
    step = lambda idx=None: idx + s if idx else s
    chunks = (
        l[idx:step(idx)]
        for idx in range(0, len(l), step())
    )
    return chunks