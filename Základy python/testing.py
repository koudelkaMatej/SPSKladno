PI = 3.14 # PI používáme jako konstantu - jeho hodnota se nikdy neměnní
pocet_pouziti_funkce = 0
E = 2.17 # při druhém spuštění této buňky už E existuje, takže podruhé to projde...
obvod = 0
def obvod_kruhu(polomer):
  global pocet_pouziti_funkce #
  global obvod
  pocet_pouziti_funkce += 1
  obvod = 2*PI*polomer # hodnotu PI můžeme číst
  print("E uvnitř funkce:",E) # hodnotu E nemůžeme číst - vytváříme ji až po zavolání funkce
  return obvod

O1 = obvod_kruhu(5)
O1 = obvod_kruhu(5)
O1 = obvod_kruhu(5)
E = 2.17 # při druhém spuštění této buňky už E existuje, takže podruhé to projde...

print("Počet použítí funkce:",pocet_pouziti_funkce)
print("Obvod O1:",O1)
print("obvod:",obvod) # obvod zde neexistuje - existuje pouze uvnitř funkce