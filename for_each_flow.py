from metaflow import FlowSpec, step

class ForeachFlow(FlowSpec):

    @step
    def start(self): # for each step
        print("Test message.")
        self.titles = ['Stranger Things',
                       'House of Cards',
                       'Narcos']
        print("Titles: ", self.titles)
        self.next(self.a, foreach='titles')

    @step
    def a(self): # linear step
        self.title = '%s processed' % self.input
        print("We have processed title: ", self.input)
        self.next(self.join)

    @step
    def join(self, inputs): # join step (has 'inputs')
        self.results = [input.title for input in inputs]
        print("We have joined the following inputs: ", self.results)
        self.next(self.end)

    @step
    def end(self):
        print('\n'.join(self.results))

if __name__ == '__main__':
    ForeachFlow()