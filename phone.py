phone = input('Enter a 10 digit phone number')


area = phone[0:3]
first = phone[4:7]
last = phone[7:]

print(f'({area}) {first}-{last}')
