import re


def evaluate(data):
    # Match function calls: add(x,y) or mul(x,y)
    pattern = re.compile(r"(add|mul)\((\d+),(\d+)\)")

    def replacer(match):
        op, x, y = match.groups()

        # Accept only positive integers (no zero, no leading zeros)
        if not (x.isdigit() and y.isdigit()):
            return match.group(0)

        if x.startswith("0") or y.startswith("0"):
            return match.group(0)

        x, y = int(x), int(y)

        return str(x + y) if op == "add" else str(x * y)

    return pattern.sub(replacer, data)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


if __name__ == "__main__":
    print(evaluate("add(1,2)"))  # 3
    print(evaluate("aybabtu"))  # aybabtu
    print(evaluate("mul(6,7),mul(7,191)"))  # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)"))  # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)"))  # mul()mul(13)mul(0,1)
    print(
        evaluate(
            "mumul(731,456add(524,786mul(746,170)mul(419,726)add(68add(351,add(225,776)"
        )
    )

    data = "mul(6,7)" * 10**5
    result = evaluate(data)
    print(len(result))  # 200000
    print(result[:20])  # 42424242424242424242
