import sys
sys.path.append(".")
import pytest

from bin.perceptron import Perceptron

@pytest.mark.parametrize("inputs, outputs", [([1,1],1),([1,0],1),([0,1],1),([0,0],0)],)
def test_perceptron_pass(inputs,outputs):
    the_perceptron = Perceptron()
    # GIVEN a Perceptron object with known objects
    the_perceptron.train([[1,1],[1,0],[0,1],[0,0]],[1,1,1,0])
    # THEN we should know the outcomes
    assert the_perceptron.predict(inputs) == outputs, f"Expected {outputs} for {inputs}"

@pytest.mark.parametrize("inputs, outputs, XFAIL", [([1,1],1,"XPASS"),([1,0],0,"XFAIL"),([0,1],1,"XPASS"),([0,0],0,"XPASS")],)
def test_perceptron_fail(inputs,outputs,XFAIL):
    the_perceptron = Perceptron()
    # GIVEN a Perceptron object with known objects
    the_perceptron.train([[1,1],[1,0],[0,1],[0,0]],[1,1,1,0])
    # THEN we should know the outcomes
    assert the_perceptron.predict(inputs) == outputs, f"Expected {outputs} for {inputs}"

@pytest.mark.skipif(sys.version_info < (3,13), reason="Skipped due to Python version below 3.13")
def test_perceptron_skipped():
    the_perceptron = Perceptron()
    the_perceptron.train([[1,1],[1,0]],[1,1])
    assert the_perceptron.predict([1,1]) == 1, "[1,1] should =1, skipped if Python < 3.13"
    assert the_perceptron.predict([1,0]) == 1, "[1,0] should =1, skipped if Python < 3.13"

@pytest.mark.skip(reason="This test rolled a nat 1!")
def test_silly_nat1():
    dnd = 100 * 10
    assert dnd == 1000

@pytest.mark.parametrize("training_set,expected,label",[([5,-1],1,1),([2,3],1,2),([-3,6],1,3),([7,9],1,4),([2,9],1,5),])
def test_perceptron_more(training_set,expected,label):
    the_perceptron = Perceptron()
    the_perceptron.train([[5,-1],[2,3],[-3,6],[7,9],[2,9]],[1,5,3,16,11])
    predicted = the_perceptron.predict(training_set)
    assert predicted == expected, f"Expected {expected}, got {predicted} for {label}: {training_set}"
