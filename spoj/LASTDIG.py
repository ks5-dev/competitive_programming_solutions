def main():
    for _ in range(int(raw_input())):
	    a, b = map(int, raw_input().split())
	    print(pow(a, b)%10)
main()
