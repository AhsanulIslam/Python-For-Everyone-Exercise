text = "X-DSPAM-Confidence:    0.8475";

f = text.find('0')
print(f)

sli = text[f:]
flo = float(sli)
print(flo)

[int(s) for s in text.split() if s.isdigit()]
print(s)


