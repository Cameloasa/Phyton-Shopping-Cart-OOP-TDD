4 Webbshop
Skapa klasser som representerar en webbshop:
produkter (Product)
beställningar (Order)
kundvagn (ShoppingCart)

Tips 1! Ge varje klass en egenskap "__id". Man kan använda den för att referera till ett annat objekt. Detta behövs eftersom både kundvagn och beställningar kommer att innehålla befintliga produkter.
Tips 2! Du kan använda AI för att skapa realistisk testdata. Prova till att börja med:
"Skapa testdata för 10 produkter till en webbshop, som säljer verktyg. Visa datan i en tabell. Varje produkt ska ha namn, pris och ett unikt id."

add __init__.py  for src and tests and install pytest with pip install pytest
