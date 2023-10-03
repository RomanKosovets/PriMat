import numpy as np
import json

# generates an empty matrix with adequate size for variables and constraints.
def gen_matrix(var, cons):
    tab = np.zeros((cons + 1, var + cons + 2))
    return tab


# checks the furthest right column for negative values ABOVE the last row. If negative values exist, another pivot is required.
def next_round_r(table):
    m = min(table[:-1, -1])
    if m >= 0:
        return False
    else:
        return True


# checks that the bottom row, excluding the final column, for negative values. If negative values exist, another pivot is required.
def next_round(table):
    lr = len(table[:, 0])
    m = min(table[lr - 1, :-1])
    if m >= 0:
        return False
    else:
        return True


# Similar to next_round_r function, but returns row index of negative element in furthest right column
def find_neg_r(table):
    # lc = number of columns, lr = number of rows
    lc = len(table[0, :])
    # search every row (excluding last row) in final column for min value
    m = min(table[:-1, lc - 1])
    if m <= 0:
        # n = row index of m location
        n = np.where(table[:-1, lc - 1] == m)[0][0]
    else:
        n = None
    return n


# returns column index of negative element in bottom row
def find_neg(table):
    lr = len(table[:, 0])
    m = min(table[lr - 1, :-1])
    if m <= 0:
        # n = row index for m
        n = np.where(table[lr - 1, :-1] == m)[0][0]
    else:
        n = None
    return n


# locates pivot element in tableu to remove the negative element from the furthest right column.
def loc_piv_r(table):
    total = []
    # r = row index of negative entry
    r = find_neg_r(table)
    # finds all elements in row, r, excluding final column
    row = table[r, :-1]
    # finds minimum value in row (excluding the last column)
    m = min(row)
    # c = column index for minimum entry in row
    c = np.where(row == m)[0][0]
    # all elements in column
    col = table[:-1, c]
    # need to go through this column to find smallest positive ratio
    for i, b in zip(col, table[:-1, -1]):
        # i cannot equal 0 and b/i must be positive.
        if i ** 2 > 0 and b / i > 0:
            total.append(b / i)
        else:
            # placeholder for elements that did not satisfy the above requirements. Otherwise, our index number would be faulty.
            total.append(0)
    element = max(total)
    for t in total:
        if t > 0 and t < element:
            element = t
        else:
            continue

    index = total.index(element)
    return [index, c]


# similar process, returns a specific array element to be pivoted on.
def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i, b in zip(table[:-1, n], table[:-1, -1]):
            if i ** 2 > 0 and b / i > 0:
                total.append(b / i)
            else:
                # placeholder for elements that did not satisfy the above requirements. Otherwise, our index number would be faulty.
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue

        index = total.index(element)
        return [index, n]


# Takes string input and returns a list of numbers to be arranged in tableu
def convert(eq):
    mode = None
    eq = eq.split(',')
    if 'gte' in eq:
        g = eq.index('gte')
        del eq[g]
        eq = [float(i) * -1 for i in eq]
        mode = 'gte'
        return eq, mode
    if 'lte' in eq:
        l = eq.index('lte')
        del eq[l]
        eq = [float(i) for i in eq]
        mode = 'lte'
        return eq, mode
    if 'eq' in eq:
        e = eq.index('eq')
        del eq[e]
        eq = [float(i) for i in eq]
        mode = 'eq'
        return eq, mode


# The final row of the tablue in a minimum problem is the opposite of a maximization problem so elements are multiplied by (-1)
def convert_min(table):
    table[-1, :-2] = [-1 * i for i in table[-1, :-2]]
    table[-1, -1] = -1 * table[-1, -1]
    return table


# generates x1,x2,...xn for the varying number of variables.
def gen_var(table):
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    v = []
    for i in range(var):
        v.append('x' + str(i + 1))
    return v


# pivots the tableau such that negative elements are purged from the last row and last column
def pivot(row, col, table):
    # number of rows
    lr = len(table[:, 0])
    # number of columns
    lc = len(table[0, :])
    t = np.zeros((lr, lc))
    pr = table[row, :]
    if table[row, col] ** 2 > 0:  # new
        e = 1 / table[row, col]
        r = pr * e
        for i in range(len(table[:, col])):
            k = table[i, :]
            c = table[i, col]
            if list(k) == list(pr):
                continue
            else:
                t[i, :] = list(k - r * c)
        t[row, :] = list(r)
        return t
    else:
        print('Cannot pivot on this element.')


# checks if there is room in the matrix to add another constraint
def add_cons(table):
    lr = len(table[:, 0])
    # want to know IF at least 2 rows of all zero elements exist
    empty = []
    # iterate through each row
    for i in range(lr):
        total = 0
        for j in table[i, :]:
            # use squared value so (-x) and (+x) don't cancel each other out
            total += j ** 2
        if total == 0:
            # append zero to list ONLY if all elements in a row are zero
            empty.append(total)
    # There are at least 2 rows with all zero elements if the following is true
    if len(empty) > 1:
        return True
    else:
        return False


# adds a constraint to the matrix
def constrain(table, eq):
    if add_cons(table) == True:
        lc = len(table[0, :])
        lr = len(table[:, 0])
        var = lc - lr - 1
        # set up counter to iterate through the total length of rows
        j = 0
        while j < lr:
            # Iterate by row
            row_check = table[j, :]
            # total will be sum of entries in row
            total = 0
            # Find first row with all 0 entries
            for i in row_check:
                total += float(i ** 2)
            if total == 0:
                # We've found the first row with all zero entries
                row = row_check
                break
            j += 1

        data = convert(eq)
        eq = data[0]
        mode = data[1]
        i = 0
        # iterate through all terms in the constraint function, excluding the last
        while i < len(eq) - 1:
            # assign row values according to the equation
            row[i] = eq[i]
            i += 1
        # row[len(eq)-1] = 1
        row[-1] = eq[-1]

        # add slack variable according to location in tableau.
        if (mode != 'eq'):
            row[var + j] = 1
    else:
        print('Cannot add another constraint.')


# checks to determine if an objective function can be added to the matrix
def add_obj(table):
    lr = len(table[:, 0])
    # want to know IF exactly one row of all zero elements exist
    empty = []
    # iterate through each row
    for i in range(lr):
        total = 0
        for j in table[i, :]:
            # use squared value so (-x) and (+x) don't cancel each other out
            total += j ** 2
        if total == 0:
            # append zero to list ONLY if all elements in a row are zero
            empty.append(total)
    # There is exactly one row with all zero elements if the following is true
    if len(empty) == 1:
        return True
    else:
        return False


# adds the onjective functio nto the matrix.
def obj(table, eq):
    if add_obj(table) == True:
        eq = [float(i) for i in eq.split(',')]
        lr = len(table[:, 0])
        row = table[lr - 1, :]
        i = 0
        # iterate through all terms in the constraint function, excluding the last
        while i < len(eq) - 1:
            # assign row values according to the equation
            row[i] = eq[i] * -1
            i += 1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')


# solves maximization problem for optimal solution, returns dictionary w/ keys x1,x2...xn and max.
def maxz(table, output='summary'):
    while next_round_r(table) == True:
        table = pivot(loc_piv_r(table)[0], loc_piv_r(table)[1], table)
    while next_round(table) == True:
        table = pivot(loc_piv(table)[0], loc_piv(table)[1], table)

    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    i = 0
    val = {}
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc, -1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1, -1]
    for k, v in val.items():
        val[k] = round(v, 6)
    if output == 'table':
        return table
    else:
        return val


# solves minimization problems for optimal solution, returns dictionary w/ keys x1,x2...xn and min.
def minz(table, output='summary'):
    table = convert_min(table)

    while next_round_r(table) == True:
        table = pivot(loc_piv_r(table)[0], loc_piv_r(table)[1], table)
    while next_round(table) == True:
        table = pivot(loc_piv(table)[0], loc_piv(table)[1], table)

    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    i = 0
    val = {}
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc, -1]
        else:
            val[gen_var(table)[i]] = 0
    val['min'] = table[-1, -1] * -1
    for k, v in val.items():
        val[k] = round(v, 6)
    if output == 'table':
        return table
    else:
        return val


if __name__ == "__main__":

    FileName = 'task.json'
    with open(FileName, 'r') as file:
        data = json.load(file)

    matrix_demention = int(input())
    number_restrictions = int(input())
    m = gen_matrix(matrix_demention, number_restrictions)

    if 'f' in data and 'goal' in data and 'constraints' in data:
        f = data['f']
        goal = data['goal']
        constraints = data['constraints']
        z_constrains = ','.join(map(str, f))

        for elements in constraints:
            coefs = elements['coefs']
            constraint_type = elements['type']
            b = elements['b']
            constraint_str = ','.join(map(str, coefs + [constraint_type, b]))
            constrain(m, constraint_str)
        obj(m, '1,2,3,0')
    else:
        print("Некорректная структура JSON файла")

    print(maxz(m))