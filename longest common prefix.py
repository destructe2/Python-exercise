def longestCommonPrefix(input):
    if not input:
        return "please enter a string"

    prefix = input[0]

    for s in input[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longestCommonPrefix(["drag", "drink", "drool"]))
