import random, sys, time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARN = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


def print_asci(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)




os.system('cls' if os.name == 'nt' else 'clear')
def print_ladowanie(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.randint(1, 10)/13)    
          
print_asci("""                                                                                                                           
| |  | |              ( )          | |                                  
| |__| | ___ _ __ ___ |/ ___       | | ___  _   _ _ __ _ __   ___ _   _ 
|  __  |/ _ \ '__/ _ \  / __|  _   | |/ _ \| | | | '__| '_ \ / _ \ | | |
| |  | |  __/ | | (_) | \__ \ | |__| | (_) | |_| | |  | | | |  __/ |_| |
|_|  |_|\___|_|  \___/  |___/  \____/ \___/ \__,_|_|  |_| |_|\___|\__, |
                                                                   __/ |
                                                                  |___/     
 """)


def poz_odp(text : str, anw : list):
    odp = None
    while odp not in anw:
        odp = input(text).strip().lower()
        while odp == "nie" or odp == "n":
            print_slow("O ty gałganie... I tak Cię zmuszę...\n")
            odp = input(text).strip().lower()
    return odp

odp = poz_odp("Czy chcesz zaczac przygodę? ", ['tak', 'nie', 't', 'n'])
while odp != "nie" and odp!= "n":
    i = 0
    punkty = 25
    if punkty == 25:
        atrybuty = []
        while len(atrybuty) < 4:
            atrybuty.append(random.randint(0,punkty-1))
            punkty -= atrybuty[i]
            i += 1 
        if punkty > 0: 
            j = random.randint(0,3)
            atrybuty[j] += punkty
        sila = str(atrybuty[0])
        zwinnosc = str(atrybuty[1])
        inteligencja = str(atrybuty[2])
        charyzma = str(atrybuty[3])
    print_slow(bcolors.BOLD+"\nOto twoje atrybuty:"+bcolors.ENDC+"\n Siła: "+sila+"\n Zwinność: "+zwinnosc+"\n Inteligencja: "+inteligencja+"\n Charyzma: "+charyzma+".\n")
    odp = input(bcolors.BOLD+"Czy chcesz wylosować statystki jeszcze raz?: "+bcolors.ENDC).strip().lower()

print_slow("W dawnych i odległych czasach żył sobie pewien chłopak. Był on młodym wieśniakiem, który ani trochę nie wykazywał talentu do magii, walki, czy nawet takich dziedzin jak zarządzanie finansami. Być może dlatego że nigdy nie miał z nimi do czynienia. Pewnego dnia w jego wiosce zatrzymał się nadworny mag. Był on jednym z potężniejszych ludzi w całym królestwie. Zobaczył on że nasz młody bohater posiada bardzo dużą moc magiczną, więc zabrał go do stolicy w której uczył go magii, alchemii i wszystkich tajnych spraw. Podczas jednego z zadań nasz bohater się zgubił w gęstym lesie. Tutaj zaczyna się nasza historia.\n")
input("\n\n Aby kontynuować naciśnij klawisz ENTER")
os.system('cls' if os.name == 'nt' else 'clear')
print_slow(bcolors.BOLD+"ŁADOWANIE GRY\n"+bcolors.ENDC)
print_ladowanie("""▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩""")
os.system('cls' if os.name == 'nt' else 'clear')
print_slow("""
    ____             __           
   / __ \_________  / /___  ____ _
  / /_/ / ___/ __ \/ / __ \/ __ `/
 / ____/ /  / /_/ / / /_/ / /_/ / 
/_/   /_/   \____/_/\____/\__, /  
                         /____/  
\n 
""")
print_slow(bcolors.OKCYAN+"Witaj w samouczku dotyczącym gry. Nauczę Cię tu podstawowych mechanik, wiedzy o świecie, oraz wszystkiego co może Ci się przydać podczas podróży."+bcolors.ENDC)
print_slow("\nJesteś w gęstym lesie. Oprócz cichego ćwierkania ptaków i sporadycznego szelestu liści nie słyszsz nic. Widzisz przed sobą dwie drogi, jedną prowadzącą w prawo - wygląda na niebezpieczną i drugą w lewo - ta za to wygląda zachęcająco. Którą wybierasz? \n Wpisz 'prawo' lub 'lewo'")
ekwipunek = []
droga = input(bcolors.BOLD+"\nWybierz kierunek: "+bcolors.ENDC).lower()
while droga != "prawo" and droga != "lewo":
    droga = input(bcolors.BOLD+"\nWybierz kierunek: "+bcolors.ENDC).lower()
if droga == "prawo":
    print_slow(bcolors.BOLD+"Poszedłeś w prawo... odważnie..."+bcolors.ENDC)
    print_slow("\nKrocząc niebezpiecznie wyglądającą ścieżką rozglądasz się po lesie chłonąc oczami każdą piękną rzecz. Nieopodal słyszysz strumień. Nagle zamierasz w bezruchu. Przed tobą, w niedalekiej odległości leży trup. Wygląda na coś co można zbadać.\n")
    badanie = input(bcolors.BOLD+"\nCzy chcesz zbadać trupa?: "+bcolors.ENDC).lower()
    while badanie != "tak" and badanie != "nie":
         badanie = input(bcolors.BOLD+"\nCzy chcesz zbadać trupa?: "+bcolors.ENDC).lower()
    if badanie == "tak":
        print_slow("Jego rany wylądają na świeże. Prawdopodobnie zabiło go jakieś dzikie zwierze - wilk, lub coś nie większego, zgadujesz po rozmiarze ran. W jego ręce błyszczy sztylet. Powoli po niego sięgasz, próbując wstrzymać oddech - nie tylko dlatego że trup cuchnie, ale dlatego też, że boisz się go obudzić. Całe szczęście, nie obudził się. W końcu to tylko trup.\n")
        
        print_slow(bcolors.BOLD+"\nZDOBYWASZ SZTYLET!!!\n"+bcolors.ENDC)
        sztylet = 3
        ekwipunek.append(sztylet)
        print_slow(bcolors.BOLD+"\nSztylet: + 3 DMG\n"+bcolors.ENDC)
        
        print_slow(bcolors.OKCYAN+"\nSAMOUCZEK: Bronie posiadają statystyki. Mogą być one przydatne w walce, zwiększając zadawane obrażenia.\n"+bcolors.ENDC)
        
    else:
        print_slow(bcolors.BOLD+"Zostawiasz trupa w spokoju.\n"+bcolors.ENDC)
        ekwipunek.append(0)
else: 
    print_slow("Idąc spokojną drogą docierasz do pewnego tajemniczego miejsca. Wygląda ono na strzelnice - prawopodobnie używana kilka lub kilkanaście lat temu do szkolenia królewskich łuczników. Miejsce to wydaje się idealne ze względu na swoje odosobnienie. Możesz zbadać to miejsce.\n")
    miejsce = input(bcolors.BOLD+"Czy chcesz zbadać strzelnice?: "+bcolors.ENDC).lower()
    while miejsce != "tak" and miejsce != "nie":
        miejsce = input(bcolors.BOLD+"Czy chcesz zbadać strzelnice?: "+bcolors.ENDC).lower()
    if miejsce == "tak":
        print_slow("Badając okolice twoją uwagę przykuwa pewna rzecz, a dokładniej broń. Jest to łuk. Wykonany ze szlachetnego drewna, znajdującego się wyłącznie na terenach dalekiej północy. Zabierasz go ze sobą - może się przydać\n")
        
        print_slow(bcolors.BOLD+"\nZDOBYWASZ ŁUK!!!\n"+bcolors.ENDC)
        luk = 3
        ekwipunek.append(luk)
        print_slow(bcolors.BOLD+"\nŁuk: + 3 DMG\n"+bcolors.ENDC)
    
        print_slow(bcolors.OKCYAN+"\nSAMOUCZEK: Bronie posiadają statystyki. Mogą być one przydatne w walce, zwiększając zadawane obrażenia.\n"+bcolors.ENDC)
        
    else: 
        print_slow("Postanawiasz nie badać strzelnicy i iść dalej.\n")
        ekwipunek.append(0)

print_slow("Idąc dalej spotykasz swojego pierwszego wroga. Jest to goblin, stoi on na twojej drodze, ale wiesz jak sobie z nim poradzić - w końcu zdobyłeś swoją broń. Możesz też spróbować się przekraść - jeśli jesteś wystarczająco zwinny, ale czy nie warto spróbować dla odrobiny bitewnego doświadczenia?...\n")


poziom = 1
exp = 0
sila = int(sila)
inteligencja = int(inteligencja)
charyzma = int(charyzma)
zwinnosc = int(zwinnosc)
hp = 100 + sila
mana = 40 + inteligencja
goblin_hp = 70
doswiadczenie = 0
gracz_dmg = random.randint(10,15) + sila + int(ekwipunek[0])
goblin_dmg = random.randint(5,10)

def walka(hp, mana, wrog_hp, gracz_dmg, wrog_dmg):
    exp = int(wrog_hp/2)
    zak_odp = input(bcolors.BOLD+"Czy chciałbyś użyć jakiegoś zaklęcia?:  "+bcolors.ENDC).lower()
    if zak_odp == "tak" or zak_odp == "t":
        print_slow(bcolors.BOLD+"Masz do wyboru:"+bcolors.ENDC+"\n1. Kula ognia - 20 MANA - 20 DMG \n2. Buff do obrażeń - 10 MANA")
        zaklecie = int(input(bcolors.BOLD+"\nWybierz numer zaklęcia: "+bcolors.ENDC))
        while zaklecie != 1 and zaklecie != 2:
            zaklecie = int(input(bcolors.BOLD+"\nWybierz numer zaklęcia: "+bcolors.ENDC))
        if zaklecie == 1:
            wrog_hp -= 20
            mana -= 20
        else: 
            gracz_dmg += int(gracz_dmg*0.3)
            mana -= 10
    while wrog_hp > 0: 
        wrog_hp -= gracz_dmg + random.randint(-5, 5)
        print_slow(bcolors.OKGREEN+"Wróg otrzymał "+str(gracz_dmg)+" obrażeń."+bcolors.ENDC)
        wrog_dmg = random.randint(5,10)
        hp -= wrog_dmg
        print_slow(bcolors.RED+"\nGracz otrzymał "+str(wrog_dmg)+" obrażeń\n"+bcolors.ENDC)
        print_slow(bcolors.WARN+"Twoje HP wynosi:"+str(hp)+"\nTwoja mana wynosi: "+str(mana)+"\n"+bcolors.ENDC)
    print_slow(bcolors.WARN+"\nBrawo, udało Ci się wygrać walkę!\n"+bcolors.ENDC)
    return exp, hp, mana
    
    

if zwinnosc < 5:
    print_slow(bcolors.RED+"Niestety nie udało Ci się ominąć goblina bez walki, musisz ją stoczyć, ale całe szczęście jesteś na to przygotowany.\n"+bcolors.ENDC)
    print_slow(bcolors.OKCYAN+"SAMOUCZEK: Walka odbywa się w systemie turowym. Raz uderza goblin, a raz Ty. Jeśli chcesz możesz zwiększyć swoje szanse używając zaklęć. Twoje statystyki takie jak HP i MANA są podniesione w zależnośći od twojej siły i inteligencji. Twoje HP i MANA są regenerowane w każdej turze o odpowiednio: 5 HP i 3 MANA.\n"+bcolors.ENDC)
    wynik = walka(hp, mana, goblin_hp, gracz_dmg, goblin_dmg)
    exp = wynik[0]
    hp = wynik[1]
    mana = wynik[2]
    print_slow(bcolors.WARN+"\nZdobyłeś "+str(exp)+" doświadczenia."+bcolors.ENDC)
else: 
    print_slow(bcolors.WARN+"Udało Ci się prześlizgnąć obok goblina niezauważonym.\n"+bcolors.ENDC)
    exp = int(goblin_hp/2)

def awans(ex):
    poz = 1
    pkt = 0
    if ex > 30:
        poz += 1
        ex -= 30
        print_slow(bcolors.WARN+"Gratulacje zdobyłeś nowy poziom!"+bcolors.ENDC)
        pkt += 1 
    return ex, poz, pkt


print_slow("Dochodzisz do miejsca odpoczynku.\n")
odpoczynek = input(bcolors.BOLD+"Czy chciałbyś odpocząć i zregenerować siły?: " +bcolors.ENDC).lower() 
while odpoczynek != "tak" and odpoczynek != "nie":
    odpoczynek = input(bcolors.BOLD+"Czy chciałbyś odpocząć i zregenerować siły?: "+bcolors.ENDC ).lower() 
if odpoczynek == "tak":
    awans = awans(exp)
    exp = awans[0]    
    poziom = awans[1]
    punkty = awans[2]
    print_slow("\nPowoli kładziesz się spać. Przez chwilę rozmyślasz o walce z goblinem. Czujesz jak twoje powieki robią się ciężkie i postanawiasz oddać się snu w pobliżu ogniska.\n")
    print_slow(bcolors.WARN+"Twoje HP i MANA zostały zregenerowane\n"+bcolors.ENDC)
    print_slow(bcolors.WARN+"Masz: "+str(poziom)+" poziom\n"+bcolors.ENDC)
    print_slow(bcolors.WARN+"Posiadasz: "+str(exp)+" PD\n"+bcolors.ENDC)
    hp = 100 + sila
    mana = 40 + inteligencja
else: 
    awans = awans(exp)
    exp = awans[0]    
    poziom = awans[1]
    punkty = awans[2]
    print_slow("Czuwasz całą noc, Twoje ciało powoli opada z sił. \nDo następnego miejsca odpoczynku twoje obrażenia zmniejszą się  o 30%")
    print_slow(bcolors.WARN+"Masz: "+str(poziom)+" poziom\n"+bcolors.ENDC)
    print_slow(bcolors.WARN+"Posiadasz: "+str(exp)+" PD\n"+bcolors.ENDC)
    gracz_dmg = (random.randint(10,15) + sila + int(ekwipunek[0])) - 0.3*gracz_dmg

input(bcolors.BOLD+"\n\n Aby kontynuować naciśnij klawisz ENTER"+bcolors.ENDC)
os.system('cls' if os.name == 'nt' else 'clear')
print_slow(bcolors.BOLD+"ŁADOWANIE GRY\n"+bcolors.ENDC)
print_ladowanie("""▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩""")
os.system('cls' if os.name == 'nt' else 'clear')

print_asci("""

    ____             __                               ________
   / __ \_________  / /___  ____ _   _________       /  _/  _/
  / /_/ / ___/ __ \/ / __ \/ __ `/  / ___/_  /       / / / /  
 / ____/ /  / /_/ / / /_/ / /_/ /  / /__  / /__    _/ /_/ /   
/_/   /_/   \____/_/\____/\__, /   \___/ /___(_)  /___/___/   
                         /____/                               
\n
""")
print_slow("Podczas snu czujesz jak tracisz panowanie nad swoimi kończynami. Wisisz w przestrzeni, a dookoła Ciebie roztacza się czerń i mrok. Nagle przed Tobą pojawia się postać, niestety nie widzisz kto to jest, tylko słyszysz cichy pomruk. Nagle jego głos staje się wyraźny i słyszysz: \n"+bcolors.RED+"Młodzieńcze, świat czeka zagłada i tylko ty możesz ją powstrzymać."+bcolors.ENDC+"\nBudzisz się i nagle czujesz preszywający ból na dłoni. Widzsisz jak powoli zaczyna się na niej rysować jakiś symbol, lecz nie wiesz co on oznacza.\n")
print_slow(bcolors.OKCYAN+"SAMOUCZEK: Nauczę Cię teraz jak wydawać punkty umiejętności, żebyś mógł rosnąć w siłe i pokonywać coraz to większych przeciwników.\n"+bcolors.ENDC)

wrogowie = {
    1: "Mrocznoskrzydły",
    2: "Żelaznozęby",
    3: "Kwasochłonny",
    4: "Goblin",
    5: "Ognistopazur",
    6: "Krwawołap",
}

statystyki = {
    "Mrocznoskrzydły": [90, random.randint(6,11)],
    "Żelaznozęby": [70, random.randint(5,10)],
    "Kwasochłonny": [80, random.randint(7,15)],
    "Goblin": [50, random.randint(2,7)],
    "Ognistopazur": [110, random.randint(10,14)],
    "Krwawołap": [60, random.randint(6,9)],
}

def przypisanie():
    def dodawanie():
        sila = atrybuty[0]
        zwinnosc = atrybuty[1]
        inteligencja = atrybuty[2]
        charyzma = atrybuty[3]
        punkty = awans[2]
        stat = int(input(bcolors.BOLD+"Jaką statystykę chcesz ulepszyć?: \n1. Siła\n2. Zwinność\n3. Inteligencja\n4. Charyzma\n"+bcolors.ENDC))
        if stat == 1:
            sila += punkty
        elif stat == 2:
            zwinnosc += punkty
        elif stat == 3:
            inteligencja += punkty
        elif stat == 4:
            charyzma += punkty
        return sila,zwinnosc,inteligencja,charyzma
    staty = dodawanie()
    atrybuty[0] = int(staty[0]) 
    atrybuty[1] = int(staty[1]) 
    atrybuty[2] = int(staty[2]) 
    atrybuty[3] = int(staty[3])
    sila = str(atrybuty[0])
    zwinnosc = str(atrybuty[1])
    inteligencja = str(atrybuty[2])
    charyzma = str(atrybuty[3])
    print_slow(bcolors.BOLD+"\nOto twoje atrybuty:"+bcolors.ENDC+"\n Siła: "+sila+"\n Zwinność: "+zwinnosc+"\n Inteligencja: "+inteligencja+"\n Charyzma: "+charyzma+".\n")
    return atrybuty

atrybuty = przypisanie()  
del() 
def losowanie():
    wrog = wrogowie[random.randint(1,6)]
    stat = statystyki[wrog]
    wrog_hp = stat[0]
    wrog_dmg = stat[1]
    return wrog, wrog_hp, wrog_dmg


wrog = losowanie()
wrog_nazwa = str(wrog[0])
wrog_hp = int(wrog[1])
wrog_dmg = int(wrog[2])

print_slow("Otwierasz oczy i podnosisz się z zimnej ziemi, na której spałeś. Twoje ubrania są przemoczone, lecz nie może Cię to powstrzymać przed ruszeniem w dalszą drogę. Ciągle rozmyślasz od swoim śnie. Co on mógł oznaczać. Z letargu wyrywa Cię nadciągający potwór. Jest to "+str(wrog_nazwa)+". Musisz z nim walczyć nie ma odwrotu.\n")
wynik = walka(hp, mana, wrog_hp, gracz_dmg, wrog_dmg)
exp = wynik[0]
hp = wynik[1]
mana = wynik[2]
print_slow(bcolors.WARN+"\nZdobyłeś "+str(exp)+" doświadczenia."+bcolors.ENDC)
print_slow("Po wygranej walce ruszasz dalej w drogę. Po kilku chwilach marszu zauważasz skrzynię. Twoją uwagę przykuwa fakt, że skrzynia wygląda na nową, pomimo faktu że reszta otoczenia najprawopodobniej nie widziała żadnej żywej intelignetej istoty od wieków.")
print_slow("Tutaj kończy się twoja przygoda.")
os.system('cls' if os.name == 'nt' else 'clear')
print_asci("""
██████╗░███████╗██╗███████╗██╗░░██╗██╗░░░██╗░░░░░██╗███████╗  ███████╗░█████╗░
██╔══██╗╚════██║██║██╔════╝██║░██╔╝██║░░░██║░░░░░██║██╔════╝  ╚════██║██╔══██╗
██║░░██║░░███╔═╝██║█████╗░░█████═╝░██║░░░██║░░░░░██║█████╗░░  ░░███╔═╝███████║
██║░░██║██╔══╝░░██║██╔══╝░░██╔═██╗░██║░░░██║██╗░░██║██╔══╝░░  ██╔══╝░░██╔══██║
██████╔╝███████╗██║███████╗██║░╚██╗╚██████╔╝╚█████╔╝███████╗  ███████╗██║░░██║
╚═════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚══════╝  ╚══════╝╚═╝░░╚═╝

███████╗░█████╗░░██████╗░██████╗░░█████╗░███╗░░██╗██╗███████╗  ░██╗░░░░░░░██╗  ░██████╗░██████╗░███████╗██╗
╚════██║██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░██║██║██╔════╝  ░██║░░██╗░░██║  ██╔════╝░██╔══██╗██╔════╝██║
░░███╔═╝███████║██║░░██╗░██████╔╝███████║██╔██╗██║██║█████╗░░  ░╚██╗████╗██╔╝  ██║░░██╗░██████╔╝█████╗░░██║
██╔══╝░░██╔══██║██║░░╚██╗██╔══██╗██╔══██║██║╚████║██║██╔══╝░░  ░░████╔═████║░  ██║░░╚██╗██╔══██╗██╔══╝░░╚═╝
███████╗██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║██║███████╗  ░░╚██╔╝░╚██╔╝░  ╚██████╔╝██║░░██║███████╗██╗
╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚══════╝  ░░░╚═╝░░░╚═╝░░  ░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝

██╗░░██╗░█████╗░██╗░░░░░███████╗░░░░░██╗███╗░░██╗░█████╗░  ░█████╗░███████╗███████╗░██████╗░█████╗░  ░██╗░░░░░░░██╗
██║░██╔╝██╔══██╗██║░░░░░██╔════╝░░░░░██║████╗░██║██╔══██╗  ██╔══██╗╚════██║██╔════╝██╔════╝██╔══██╗  ░██║░░██╗░░██║
█████═╝░██║░░██║██║░░░░░█████╗░░░░░░░██║██╔██╗██║███████║  ██║░░╚═╝░░███╔═╝█████╗░░╚█████╗░██║░░╚═╝  ░╚██╗████╗██╔╝
██╔═██╗░██║░░██║██║░░░░░██╔══╝░░██╗░░██║██║╚████║██╔══██║  ██║░░██╗██╔══╝░░██╔══╝░░░╚═══██╗██║░░██╗  ░░████╔═████║░
██║░╚██╗╚█████╔╝███████╗███████╗╚█████╔╝██║░╚███║██║░░██║  ╚█████╔╝███████╗███████╗██████╔╝╚█████╔╝  ░░╚██╔╝░╚██╔╝░
╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═════╝░░╚════╝░  ░░░╚═╝░░░╚═╝░░

██████╗░██████╗░░█████╗░██████╗░███████╗███████╗██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚════██║██╔════╝██║
██║░░██║██████╔╝██║░░██║██║░░██║░░███╔═╝█████╗░░██║
██║░░██║██╔══██╗██║░░██║██║░░██║██╔══╝░░██╔══╝░░╚═╝
██████╔╝██║░░██║╚█████╔╝██████╔╝███████╗███████╗██╗
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝╚══════╝╚═╝
""")

