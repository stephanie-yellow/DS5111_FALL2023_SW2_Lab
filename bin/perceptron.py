'''
This is a module for the lab to actually see how pylint works.
'''
class Perceptron:
    '''
    This is a class that will apply the Perceptron rule for machine learning.
    '''
    def __init__(self):
        '''
        This is the iniator.
        '''
        self._weights: []

    def train(self, inputs, labels):
        '''
        This is the train function for the Perceptron class. It requires inputs and labels.
        '''
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        inp = None
        for _ in range(5000):
            for inp, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(inp)
            for index, x in enumerate(inp):
                self._weights[index] += .1 * x * label_delta
    def predict(self, input_pre):
        '''
        This is the predict function for the Perceptron class.
        It takes the output from the train function. 
        '''
        if len(input_pre) == 0:
            return None
        input_pre = input_pre + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights,input_pre)]))
