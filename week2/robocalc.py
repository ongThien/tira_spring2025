def calculate(input: str, rules: list[tuple]) -> bool:
    symbols = list("L" + input + "R")  # list for mutability
    cur_ptr = 0  # initial pointer
    cur_state = 1  # initial state
    action_cnt = 0  # action counter

    while action_cnt < 1000:
        cur_sym = symbols[cur_ptr]

        # find matching rule
        matched_rule = None
        for r in rules:
            r_sym, r_state, new_sym, new_state, action = r
            if cur_sym == r_sym and cur_state == r_state:
                matched_rule = (new_sym, new_state, action)
                break  # stop at first match

        # reject if no matching rule
        if matched_rule is None:
            return False

        # apply rule
        new_sym, new_state, action = matched_rule

        symbols[cur_ptr] = new_sym
        cur_state = new_state

        if action == "RIGHT":
            cur_ptr += 1
        elif action == "LEFT":
            cur_ptr -= 1

        # if out of bounds
        if cur_ptr < 0 or cur_ptr >= len(symbols):
            return False

        if action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False

        action_cnt += 1

    return False  # timeout after 1000 actions


if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules))  # False
    print(calculate("00", rules))  # False
    print(calculate("01", rules))  # True
    print(calculate("0110", rules))  # True
    print(calculate("0101", rules))  # True
    print(calculate("1000", rules))  # False
    print(calculate("00110101", rules))  # True
    print(calculate("00111101", rules))  # False
