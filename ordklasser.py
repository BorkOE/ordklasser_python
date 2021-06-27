# Detta är ett program där spelaren ska träna på ordklasser 
import random, pyinputplus, sys, time

# En funktion som skriver ut tre punkter efter varandra 
def punktFunktion():
    time.sleep(0.5)
    for i in range(0,3): # loopa 3 gånger
        i # bara för att inte få ett error när jag inte använder variabeln
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)
    print()

# Ordklasser
verb = ['springa', 'hoppa', 'cykla', 'städa', 'studera', 'titta', 'undersöka', 'spela', 'ropa', 'skratta']
substantiv = ['bord', 'gitarr', 'äpple', 'dator', 'träd', 'berg', 'pinne', 'tallrik', 'låda', 'säng', 'högtalare', 'flygplan', 'bil']
adjektiv = ['röd', 'snabb', 'stor', 'liten', 'kraftig', 'rund', 'bred', 'rik', 'fattig', 'sned', 'rak', 'trött', 'glad'
, 'rolig', 'pigg']
ordklasser = ['verb', 'substantiv', 'adjektiv']

räkneOrd = ['första', 'andra', 'tredje', 'fjärde', 'femte', 'sjätte', 'sjunde', 'åttonde', 'nionde', 'tionde', 'elfte', 'tolfte', 'trettonde'
, 'fjortonde', 'femtonde','sextonde', 'sjuttonde', 'artonde', 'nittonde', 'tjugonde']

antalRättSvar = 0

# Fråga efter antal frågor
antalFrågor = pyinputplus.inputNum('Hur många frågor ska det vara? ')
punktFunktion()
print('Okej, då tar jag fram', antalFrågor, 'frågor.')
punktFunktion()

# Listor för de slumpmässiga orden
valdaVerb = []
valdaSubstantiv = []
valdaAdjektiv = []

print() # Lite luft i utskriften

# Main-loop
for i in range(0,antalFrågor): # Sätt längd på spel

    print('Här kommer', räkneOrd[i], 'frågan.')
    felUpptäckt = False # Gör så att spelaren kan få poäng om den svarar rätt på första försöket
    punktFunktion()
 
    # Välj en ordklass
    valdOrdklass = random.choice(ordklasser)

    if valdOrdklass == 'verb':
        valtOrd = random.choice(verb)
        rättSvar = 'verb'
        print('Vilken ordklass tillhör ordet ' + "\"" + valtOrd + "\"" + '?')
        # print verb
    
    if valdOrdklass == 'substantiv':
        valtOrd = random.choice(substantiv)
        rättSvar = 'substantiv'
        print('Vilken ordklass tillhör ordet ' + "\"" + valtOrd + "\"" + '?')
        # print substantiv

    if valdOrdklass == 'adjektiv':
        valtOrd = random.choice(adjektiv)
        rättSvar = 'adjektiv'
        print('Vilken ordklass tillhör ordet ' + "\"" + valtOrd + "\"" + '?')
        # print adjektiv

    # Inhämta-svar-loop
    while True:
        punktFunktion()
        print()
        svar = pyinputplus.inputMenu(['verb', 'substantiv', 'adjektiv'], lettered=False, numbered=True) # Inhämta svar
        print()
        punktFunktion()
        
        # Om rätt:
        if svar == rättSvar:
            print('Helt rätt')
            if not felUpptäckt: # Om spelaren svarar rätt på första försöket
                antalRättSvar += 1
            break
        
        # Om fel:
        else:
            print('Inte helt rätt.')
            felUpptäckt = True # Gör så att det inte räknas som rätt vid nästa försök
            punktFunktion()

            # Ge tips om vilken ordklass det är. 
            if valtOrd in verb:
                print('Tips: det är något en kan göra.')
            if valtOrd in substantiv:
                print('Tips: det är någon man kan sätta \"en\" eller \"ett\" framför.')
            if valtOrd in adjektiv:
                print('Tips: det är någon som beskriver hur saker är eller ser ut.')

            print('Vilken ordklass tillhör ordet ' + "\"" + valtOrd + "\"" + '?')
    
    # Ta bort det valda ordet från sin lista
    if valtOrd in verb:
        verb.remove(valtOrd)
        valdaVerb.append(valtOrd)
    if valtOrd in substantiv:
        substantiv.remove(valtOrd)
        valdaSubstantiv.append(valtOrd)
    if valtOrd in adjektiv:
        adjektiv.remove(valtOrd)
        valdaAdjektiv.append(valtOrd)
    print()

# Skriv ut resultatet efter alla frågor är klara
punktFunktion()
print('Du svarare rätt på', antalRättSvar, 'av', antalFrågor, 'frågor.')

# Bedömning
procentRätt = antalRättSvar/antalFrågor*100
print('Du hade ' + str(round(procentRätt)) + r'% rätt.')
if procentRätt > 90:
    print('Wow, det var jättemånga rätt! Snyggt jobbat.')
elif procentRätt > 50:
    print('Fler än hälften rätt, bra jobbat!')
elif procentRätt >= 20:
    print('Bra kämpat, fortsätt öva ordklasserna så att de sitter ännu bättre.')
elif procentRätt < 20:
    print('Ett tappert försök! Fortsätt öva för att få högre poäng.')


punktFunktion()
# Skriv ut vilka ord som fanns i de olika kategorierna av ordklasser. OBS. detta skulle kunna göras till en funktion. 
print('Verben var: ', end='')
for i in valdaVerb:
    if len(valdaVerb) > 1:
        if i != valdaVerb[-1]:
            print(i, end='')
            if i != valdaVerb[-2]:
                print(', ', end='')
            elif i == valdaVerb[-2]:
                print(' ', end='')
        else:
            print('och', i +'.')
    else:
        print(i)
if valdaVerb == []:
    print() #skriv ut en tom rad om det inte finns några ord här

print('Substantiven var: ', end='')
for i in valdaSubstantiv:
    if len(valdaSubstantiv) > 1:
        if i != valdaSubstantiv[-1]:
            print(i, end='')
            if i != valdaSubstantiv[-2]:
                print(', ', end='')
            elif i == valdaSubstantiv[-2]:
                print(' ', end='')
        else:
            print('och', i +'.')
    else:
        print(i)
if valdaSubstantiv == []:
    print() #skriv ut en tom rad om det inte finns några ord här

print('Adjektiven var: ', end='')
for i in valdaAdjektiv:
    if len(valdaAdjektiv) > 1: # Denna ser lite bökig ut för att listan ska bli snygg - sluta med 'element 2, element 3 och element 4.'
        if i != valdaAdjektiv[-1]:
            print(i, end='')
            if i != valdaAdjektiv[-2]:
                print(', ', end='')
            elif i == valdaAdjektiv[-2]:
                print(' ', end='')
        else:
            print('och', i +'.')
    else:
        print(i)
if valdaAdjektiv == []:
    print() #skriv ut en tom rad om det inte finns några ord här

print()

print('Bra jobbat!')