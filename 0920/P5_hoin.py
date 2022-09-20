n = 5
st = []
for i in range(n+1):
    b = bin(i)[2:]
    k = b.count("1")
    st.append(k)
return st