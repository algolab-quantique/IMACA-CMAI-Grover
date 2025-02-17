def variable_name_to_int(var_name):
    """This function returns an integer associated with a given variable

    Args:
        var_name (str): the current variable. For example : x1.

    Returns:
        int: an integer associated with the variable name. For example :0.
    """
    if var_name == "x0":
        return 0
    if var_name == "x1":
        return 1
    if var_name == "x2":
        return 2
    if var_name == "x3":
        return 3
    return -1


def get_variable_list_from_clause(disj_clause):
    """This function returns a list of integers associated with the variables in a given disjunction clause

    Args:
        disj_clause (dict): the current disjunction clause. For example : {'x0' : False, 'x3' : True, 'x1' : True}.

    Returns:
        list: a list of integers associated with the variables in disj_clause. For example : [0, 3, 1].
    """
    variables = []
    for var_name in disj_clause:
        variables.append(variable_name_to_int(var_name=var_name))
    return variables


def get_disjunction_qubits(disj_clause, clause_qubit, var_qubits):
    """This function returns the right qubits to which you want to apply the disjunction clause.

    For example, if we are looking at the first clause, we would have the following parameters :

        -   disj_clause = {'x2' : True, 'x0' : True, 'x3' : True}.
        -   clause_qubit = 0. The first clause is reprensented by the index 0 and the last one (seventh), by 6.
        -   var_qubits = qubits associated with variables x2, x0 and x3

        and we would return :

        -   disjunction_qubits = [x2, x0, x3, c4]. A list of qubits representing variables x2, x0 and x3 and clause 0.

    Args:
        circuit (QuantumCircuit): the oracle circuit from which we get the right qubits
        disj_clause (dict): the current disjunction clause
        ancillar_id (int): variable that represents the ID of current clause

    Returns:
        list: Returns a list of the qubits that are involved in the disjunction clause
    """
    variables = get_variable_list_from_clause(disj_clause)

    disjunction_qubits = []

    for var in variables:
        disjunction_qubits.append(var_qubits[var])

    disjunction_qubits.append(clause_qubit)

    return disjunction_qubits


def get_disjunction_control_state(disj_clause):
    """This function returns the control state of the multi controlled x-gate according to a disjunction clause.

    Args:
        disj_clause (dict): the current disjunction clause. For example : {'x1' : False, 'x4' : True, 'x2' : True}.

    Returns:
        str : Returns a string containing the control state. For example : '001'. (Little endian notation)
    """
    ctrl_state = ""
    # Get the control state according to given clause
    for var_name in disj_clause:
        state = disj_clause[var_name]
        if state:
            ctrl_state = "0" + ctrl_state
        else:
            ctrl_state = "1" + ctrl_state
    return ctrl_state
