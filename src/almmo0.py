import numpy as np


class ALMMo0Classifier:

    def __init__(self):
        self.classes = None # classes
        self.K = None # number of samples (total) / iteration
        self.N = None # number of features
        self.class_models = []
        self.class_decision = 'winner_takes_all'


    def initialize(self, X):
        pass

    def fit(self, X):
        pass

    def update(self, X):
        pass



class ALMMo0Model:

    def __init__(
            self, 
            class_label = '', 
            save_samples = False):
        
        self.K = 0
        self.class_label = class_label
        self.F = []
        self.samples = []
        self.nf = 0

        self.save_samples = save_samples



    def update(self, x):
        if self.K == 0:
            self.F = [x]
            self.nf += 1
        else:
            pass

        if self.save_samples == True:
            self.samples.append(x)
            
        self.K += 1

    def find_nearest(self, x):
        F = None
        return F

