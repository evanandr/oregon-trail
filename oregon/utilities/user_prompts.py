def ask_yes_no(prompt):
    prompt += " "
    response = str(input(prompt)).lower().strip()
    if response[0] == 'y':
        return True
    if response[0] == 'n':
        return False
    else:
        return ask_yes_no(prompt)


def ask_numeric(prompt, lower_bound=None, upper_bound=None):
    if not prompt.endswith(" "):
        prompt += " "
    response = str(input(prompt)).lower().strip()
    try:
        value = int(response)
    except ValueError:
        print("IMPOSSIBLE")
        return ask_numeric(prompt, lower_bound, upper_bound)
    if lower_bound is not None:
        if value < lower_bound:
            print("TOO LOW")
            return ask_numeric(prompt, lower_bound, upper_bound)
    if upper_bound is not None:
        if value > upper_bound:
            print("TOO HIGH")
            return ask_numeric(prompt, lower_bound, upper_bound)
    return value
