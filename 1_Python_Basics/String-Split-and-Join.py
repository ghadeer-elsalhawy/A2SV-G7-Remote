# Problem link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(line):
    # write your code here
    temp = line.split(" ")
    res = "-".join(temp)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
