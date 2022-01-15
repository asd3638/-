n = int(input())

for i in range(n):
    string = input().lower()
    missing = ''
    for alpa in range(ord('a'), ord('z') + 1):
        if string.find(chr(alpa)) == -1:
            missing += chr(alpa)
    if missing == '':
        print("pangram")
        continue
    print(f"missing {missing}")