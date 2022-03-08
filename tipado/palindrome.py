def palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

if __name__ == "__main__":
    #Utilizar mypy <archivo> --check-untyped-defs
    print(palindrome(100))