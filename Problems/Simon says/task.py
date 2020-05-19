def what_to_do(instructions: str):
    # instructions = str(instructions)

    if instructions.startswith("Simon says"):
        return f'I {instructions[11:]}'
    elif instructions.endswith("Simon says"):
        return f'I {instructions[:11]}'
    else:
        return "I won't do it!"
    # return f'I {instructions[:result]}'


# print(what_to_do(input()))
