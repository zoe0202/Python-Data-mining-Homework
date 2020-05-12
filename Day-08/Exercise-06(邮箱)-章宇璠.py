if __name__ == "__main__":
    import re

    p = re.compile(r'([^@]+)@([^@]+)\.([^@]+)')
    emails = input('请输入电子邮箱:')
    while emails:
        if not p.match(emails):
            print(emails, " NOT valid")
            break
        else:
            print(emails, ' is valid')
            break




