import email.utils
import re
def fun(s):
    check=0
    regex = re.compile('[!#$%^&*()<>?/\|}{~:]')
    rege = re.compile('.')
    st=email.utils.parseaddr(s)
    gmail=st[1]
    if gmail[0].isalpha():
        if regex.search(gmail) == None:
            if gmail.count("@") == 1 and 0<gmail.count(".")<3:
                a_index = gmail.index("@")
                user = gmail[0:a_index]
                if "_" in user:
                    check+=1
                if "." in user:
                    return False
                if "-" in user:
                    check+=1
                if check==2 or check>2:
                    return False
                temp = gmail[a_index:]
                b_index = temp.index(".")
                domain = temp[0:b_index]
                extension = temp[b_index:]
                if len(extension) > 4 or not extension[1:].isalpha():
                    return False
                elif not domain[1:].isalpha():
                    if not domain[1:].isalnum():
                        return False
                elif not user.isalnum():
                    if "-" not in user:
                        if "." not in user:
                            if "_" not in user:
                                return False
            else:
                return False
        else:
            return False
    else:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)