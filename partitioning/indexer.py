class Indexer(object):
    def __init__(self, first):
        self.next_id = first

    def next(self, result=None):
        '''
        Unmodified :: else return the next ID 
        and increment the internal counter
        '''
        if result is None:
            result = self.next_id
            self.next_id += 1
        return result

    def clear(self):
        self.next_id = 1


# If the scheme needs to be configurable, then the key member
# of connection should be used everywhere instead of having
# hard-coded (input, output) tuple keys sprinkled all over the code.
class InnovationIndexer(object):
    def __init__(self, first):
        self.indexer = Indexer(first)
        self.innovations = {}

    def get_innovation_id(self, in_node_id, out_node_id):
        innovation_id = self.innovations.get((in_node_id, out_node_id))
        if innovation_id is None:
            innovation_id = self.indexer.next()
            self.innovations[in_node_id, out_node_id] = innovation_id

        return innovation_id
