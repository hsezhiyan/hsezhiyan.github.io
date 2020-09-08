from metaflow import FlowSpec, step

class ForeachFlow(FlowSpec):
    """
    A flow to demo manual, foreach orchestration (i.e.,
    by decoupling the step run from the orchestration for the special
    foreach case.
    """

    @step
    def start(self): # type: foreach node
        print("This is a foreach node which will branch into an unknown number of nodes")
        import random

        # Let's generate a list of numbers. We do not know
        # length of this list until this piece of code executes.
        num_splits = random.randint(2,10)
        self.list_to_explore = [x for x in range(num_splits)]
        print("(For validation from inside the flow) Foreach fanout num_splits : ", len(self.list_to_explore))

        self.next(self.explore, foreach='list_to_explore')

    @step
    def explore(self): # type: linear node
        print("Inside explore...")
        print("Reading input variable: ", self.input)
        print("Done exploring...")
        self.val = '%s processed' % self.input

        self.next(self.join)

    @step
    def join(self, inputs): # type: join node
        self.results = [input.val for input in inputs]
        print("Inside join")
        print("Joining this list: ", self.results)
        self.next(self.end)

    @step
    def end(self): # type: end node
        print("END: Flow complete!")


if __name__ == '__main__':
    ForeachFlow()