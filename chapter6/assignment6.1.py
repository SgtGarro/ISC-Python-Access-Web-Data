text = "X-DSPAM-Confidence:    0.8475"
number = float(text[slice(text.find("0"), len(text))])
print(number)