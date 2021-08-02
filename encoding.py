from nnf import And, NNF, config

class Encoding:
  def __init__(self):
    self.constraints = []

  def add_constraint(self, newConstraint):
    assert isinstance(newConstraint, NNF), "Need to add NNF"
    self.constraints.append(newConstraint)

  @config(sat_backend="kissat")
  def is_satisfiable(self):
    return And(self.constraints).satisfiable()