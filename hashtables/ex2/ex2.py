#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    first_ticket = None
    for tik in tickets:
        if tik.source != "NONE":
            hash_table_insert(ht, tik.source, tik.destination)
        else:
            first_ticket = tik
    route[0] = first_ticket.destination
    for idx in range(1, length):
        route[idx] = hash_table_retrieve(ht, route[idx-1])
    return route
