#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

answer = None
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    global answer
    if length < 2:
        return None

    hash_table_insert(ht, limit - weights[0], 0)

    for idx in range(1, length):
        package = weights[idx]
        in_table = hash_table_retrieve(ht, package)
        if in_table is not None and in_table != idx:
            if weights[in_table] > package:
                answer = [in_table, idx]
                return answer
            else:
                answer = [idx, in_table]
                return answer
        hash_table_insert(ht, limit - package, idx)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
