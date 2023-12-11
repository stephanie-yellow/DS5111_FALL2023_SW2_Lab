'''This is a module for the lab to actually see how pylint works.'''
class Perceptron:
    '''This is a class that will apply the Perceptron rule for machine learning. '''
    def __init__(self):
        '''This is the initializer'''
        self._weights = 0

    def train(self,inputs,labels):
        '''This is the trainer'''
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for inp, label in zip(dummied_inputs,labels):
                label_delta = label - self.predict(inp)
                for index, c in enumerate(inp):
                    self._weights[index] += .1 * c * label_delta

    def predict(self,inp):
        '''This is the prediction'''
        if len(inp) == 0:
            return None
        inp = inp + [-1]
        return int(0 < sum([x[0] * x[1] for x in zip(self._weights,inp)]))
