text = "X-DSPAM-Confidence:    0.8475"
count = text.find("0")
print(float(text[count:]))
