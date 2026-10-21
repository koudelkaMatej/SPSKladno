# === Pojmenované argumenty ===
def zmena_jmena(jmeno):
    print(jmeno)
    jmeno = jmeno[::-1]
    return jmeno

jmeno = "petr"
print(jmeno)

print(jmeno)
def zmena_jmena(jmeno):
    print(jmeno)
    jmeno = jmeno[::-1]
    return jmeno
jmeno1= zmena_jmena(jmeno)
print(jmeno1)
print(jmeno)
