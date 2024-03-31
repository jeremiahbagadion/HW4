# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "An individual who is a single home owner with low annual income would satisfy rules 1, 2, and 3 at the same time, which means these rules are not mutually exclusive."
    answers["(b) explain"] = "Because there are potential scenarios (e.g., Divorced individuals or certain combinations of annual income and employment status) that are not addressed by the existing rules"
    answers["(c) explain"] = "because they are not mutually exclusive, and some rules may conflict with each other when applied to the same instance."
    answers["(d) explain"] = "because it is not exhaustive, and it ensures that every instance can be classified, even if it does not match any of the provided rules."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "No vertebrate can be both warm-blooded and not warm-blooded at the same time, nor can it be both an aquatic and an aerial creature at the same time based on these classifications."
    answers["(b) example"] = "they do not account for every possible condition present in the data set, specifically they do not classify all cold-blooded animals that do not give birth and are not aquatic or aerial (like reptiles and amphibians)."
    answers["(c) example"] = "Ordering of rules is required when rules are not mutually exclusive because it determines which rule should be applied first in case an instance satisfies multiple rules"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = True

    # explain_string: explanation in english prose
    answers["(a) explain"] = "the gradients of weights at the (k+1)th layer are computed using the chain rule, which involves the gradients of weights at the kth layer"
    answers["(b) explain"] = "This is forward propagation. The activations are calculated by applying a weighted sum of the inputs followed by a non-linear activation function."
    answers["(c) explain"] = "The vanishing gradient problem refers to the issue in deep neural networks where gradients of the loss function become increasingly small as the backpropagation algorithm progresses to earlier layers. It does not refer to the condition where training errors go to zero while test errors remain large, which is typically a sign of overfitting."
    answers["(d) explain"] = "If the ANN model perfectly classifies all training instances at a given iteration, it means that the predicted outputs match the true outputs for all examples. In this case, the error term for each training example i will be zero."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}


    # float
    answers["(a) P(X_1 = 1 | +)"] = None
    answers["(a) P(X_1 = 1 | -)"] = None
    answers["(a) P(X_2 = 1 | +)"] = None
    answers["(a) P(X_2 = 1 | -)"] = None
    answers["(a) P(X_3 = 1 | +)"] = None
    answers["(a) P(X_3 = 1 | -)"] = None

    # string
    answers["(b) label"] = None

    # float
    answers["(c) P(X_1=1)"] = None
    answers["(c) P(X_2=1)"] = None
    answers["(c) P(X_1=1,X_2=1)"] = None

    # string: "dependent" or "independent"
    answers["(c) Relationship between X_1 and X_2"] = None

    # float
    answers["(d) P(A=1)"] = None
    answers["(e) P(X_1=1, X_2=1|Class=+)"] = None
    answers["(e) P(X_1=1|Class=+)"] = None
    answers["(e) P(X_2=1|Class=+)"] = None

    # string: "yes" or "no"
    answers["(e) A and B conditionally independent?"] = None

    # float
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = None
    answers["(b) K"] = None

    # explain_string
    answers["(a) explain"] = None
    answers["(b) explain"] = None

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None  # WRONG
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
