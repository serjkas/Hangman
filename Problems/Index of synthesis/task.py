text_input = float(input())
if text_input < 2:
    print("Analytic")
elif 2 <= text_input <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
