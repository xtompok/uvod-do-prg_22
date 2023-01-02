# importujeme modul Transformer z balíčku pyproj
# (nutno doinstalovat pomocí `py -m pip install pyproj`)
from pyproj import Transformer

# Vyrobíme transformační objekt z WGS-84 (EPSG 4326) do S-JTSK (EPSG 5514)
# `always_xy` říká, že při transformaci vždy zadáváme (a dostaneme) x souřadnici jako první
wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)
# Vyrobíme tranformační objekt z S-JTSK do WGS-84. 
jtsk2wgs = Transformer.from_crs(5514,4326,always_xy=True)

# Podíváme se, co jsme vytvořili (jen pro kontrolu)
print(wgs2jtsk)

# Ztransformujeme souřadnice 15 stupňů východní délky a 50 stupňů severní šířky do S-JTSK 
jtsk = wgs2jtsk.transform(15,50)
# Vypíšeme souřadnice, co jsme získali
print(jtsk)
# Ztransformujeme souřadnice zpět do WGS-84
wgs = jtsk2wgs.transform(jtsk[0],jtsk[1])
# Zkontrolujeme, zda jsme dostali přibližně 15, 50, protože jsme tranformovali tam a zpět
print(wgs)
