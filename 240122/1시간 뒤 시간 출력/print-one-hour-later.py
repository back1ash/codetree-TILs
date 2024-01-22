h,m = map(int, input().split(':'))

print(f"{(h+1)%24}:{m}")