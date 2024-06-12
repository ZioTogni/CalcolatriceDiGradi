#VARIABILI
nome_aiutante="Calcolatrice di gradi"
celsius_kelvin="da Celsius a Kelvin"
kelvin_celsius="da Kelvin a Celsius"
#PROGRAMMA
print("Salve, io sono la "+nome_aiutante+"!")
print("Sono qui per aiutarti a calcolare i gradi "+celsius_kelvin+" e "+kelvin_celsius+".")
print("\nPerfavore, scegli il servizio che vuoi!")
servizio_richiesto=input()
if servizio_richiesto==celsius_kelvin:
    print("Perfetto, hai scelto il servizio "+servizio_richiesto+" ! ")
    x=input("Inserisci il numero da convertire in Kelvin!")
    s=input("Inserisci 273.15! (per convertire il tuo numero in Kelvin)")
    a=float(x)+float(s)
    print("Il numero che vuoi convertire in Kelvin risulta",a)
elif servizio_richiesto==kelvin_celsius:
    print("Perfetto, hai scelto il servizio "+servizio_richiesto+" ! ")
    x=input("Inserisci il numero da convertire in Celsius!")
    s=input("Inserisci 273.15 (per convertire il tuo numero in Celsius)")
    a=float(x)-float(s)
    print("Il numero che vuoi convertire in Celsius risulta",a)
else: 
    print("Non sono ancora capace a calcolare il servizio richiesto, perfavore riavvia il programma!")
