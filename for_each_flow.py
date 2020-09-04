from metaflow import FlowSpec, step

class ForeachFlow(FlowSpec):

    @step
    def start(self):
        print("Test message.")
        self.titles = ['Stranger Things',
                       'House of Cards',
                       'Narcos']
        print("Titles: ", self.titles)
        self.next(self.a, foreach='titles')

    @step
    def a(self):
        self.title = '%s processed' % self.input
        self.next(self.join)

    @step
    def join(self, inputs):
        self.results = [input.title for input in inputs]
        self.next(self.end)

    @step
    def end(self):
        print('\n'.join(self.results))

if __name__ == '__main__':
    ForeachFlow()