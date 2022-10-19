# 2)
# Napište program pro konverzi D -> DMS

d = float(input("Napiš stupně: "))

d_int = int(d)
m = (d - d_int)*60
m_int = int(m)
s = (m - m_int)*60

print("Je to",d_int,"stupňů",m_int,"minut a",s,"vteřin")
