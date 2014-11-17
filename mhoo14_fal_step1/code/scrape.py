import requests
import re

fermate = [{"type": "treno", "list": [{"id":"16528","value":"Acerenza"},{"id":"16529","value":"Altamura"},{"id":"16530","value":"Avigliano Citt\u00e0"},{"id":"16531","value":"Avigliano Lucania"},{"id":"16532","value":"Bari Centrale FAL"},{"id":"16560","value":"Bari Policlinico"},{"id":"16533","value":"Bari Scalo"},{"id":"16534","value":"Bari Zona Industriale"},{"id":"16535","value":"Basentello"},{"id":"16561","value":"Binetto"},{"id":"17557","value":"Cancellara"},{"id":"16536","value":"Genzano"},{"id":"16537","value":"Gravina"},{"id":"16538","value":"Grumo A."},{"id":"16562","value":"Irsina"},{"id":"16539","value":"Marinella"},{"id":"16540","value":"Matera Centrale"},{"id":"17554","value":"Matera Serra Rifusa"},{"id":"16541","value":"Matera Sud"},{"id":"16563","value":"Matera Villa Longo"},{"id":"16542","value":"Mellitto"},{"id":"16543","value":"Moccaro"},{"id":"16544","value":"Modugno"},{"id":"16545","value":"Oppido Lucano"},{"id":"17553","value":"Palo del Colle"},{"id":"17556","value":"Pellicciari"},{"id":"16547","value":"Pescariello"},{"id":"16548","value":"Pietragalla"},{"id":"16549","value":"Posto Movimento Tiera"},{"id":"16550","value":"Potenza Citt\u00e0"},{"id":"16554","value":"Potenza Inf. Scalo"},{"id":"16564","value":"Potenza Inferiore"},{"id":"16551","value":"Potenza Macchia Romana"},{"id":"16552","value":"Potenza Rione Mancusi"},{"id":"16565","value":"Potenza S. Rocco"},{"id":"16553","value":"Potenza S.Maria"},{"id":"16555","value":"Ripa D'Api"},{"id":"16556","value":"S.Nicola"},{"id":"17555","value":"Santa Teresa di Gravina"},{"id":"16557","value":"Taccone"},{"id":"16566","value":"Tiera"},{"id":"16567","value":"Toritto"},{"id":"16558","value":"Torre Vosa"},{"id":"16559","value":"Venusio"}]}, {"type": "bus", "list": [{"id":"25","value":"Abriola"},{"id":"26","value":"Acerenza"},{"id":"17","value":"Altamura"},{"id":"119","value":"Arioso"},{"id":"80","value":"Atena"},{"id":"27","value":"Avigliano"},{"id":"118","value":"Badia S. Angelo"},{"id":"5","value":"Bari"},{"id":"121","value":"Basentello"},{"id":"18","value":"Binetto"},{"id":"19","value":"Bitetto"},{"id":"117","value":"Bivio Anzi"},{"id":"116","value":"Bivio Latronico"},{"id":"115","value":"Bivio Lauria"},{"id":"114","value":"Bivio Rotonda"},{"id":"112","value":"Borgo Venusio"},{"id":"81","value":"Brienza"},{"id":"28","value":"Calvello"},{"id":"122","value":"Cancellara"},{"id":"79","value":"Castelluccio"},{"id":"78","value":"Epitaffio"},{"id":"29","value":"Ferrandina"},{"id":"111","value":"Galdo"},{"id":"110","value":"Genzano di Lucania"},{"id":"109","value":"Grassano"},{"id":"20","value":"Gravina"},{"id":"77","value":"Grumo Appula"},{"id":"33","value":"Irsina"},{"id":"75","value":"Lagonegro"},{"id":"113","value":"Laino Borgo"},{"id":"34","value":"Laurenzana"},{"id":"108","value":"Lauria"},{"id":"107","value":"Mad. Pantano"},{"id":"35","value":"Marconia"},{"id":"123","value":"Marinella"},{"id":"106","value":"Marsico Nuovo"},{"id":"36","value":"Matera"},{"id":"124","value":"Mellitto"},{"id":"125","value":"Moccaro"},{"id":"22","value":"Modugno"},{"id":"37","value":"Montalbano"},{"id":"105","value":"Monteforte"},{"id":"38","value":"Montescaglioso"},{"id":"104","value":"Montocchio"},{"id":"103","value":"Nemoli"},{"id":"126","value":"Oppido Lucano"},{"id":"16","value":"Paestum"},{"id":"76","value":"Palo del Colle"},{"id":"127","value":"Pellicciari"},{"id":"102","value":"Pergola"},{"id":"128","value":"Pescariello"},{"id":"101","value":"Peschiera-Craco"},{"id":"39","value":"Pietragalla"},{"id":"40","value":"Pignola"},{"id":"41","value":"Pisticci"},{"id":"100","value":"Poggiorsini"},{"id":"99","value":"Ponte Camastra"},{"id":"98","value":"Ponte d'Inferno"},{"id":"97","value":"Ponte Mallardi"},{"id":"43","value":"Potenza"},{"id":"95","value":"Pozzi"},{"id":"94","value":"Praia a Mare"},{"id":"93","value":"Prestieri"},{"id":"129","value":"Ripa D'Api"},{"id":"92","value":"Rotonda"},{"id":"91","value":"S. Nicola"},{"id":"216","value":"Sala Consilina"},{"id":"44","value":"Salandra"},{"id":"90","value":"Sasso di Castalda"},{"id":"89","value":"Sciffra"},{"id":"88","value":"Sellata"},{"id":"87","value":"Serrapotamo"},{"id":"86","value":"Spinazzola"},{"id":"130","value":"Taccone"},{"id":"85","value":"Taverna Foia"},{"id":"96","value":"Tiera"},{"id":"84","value":"Tinchi"},{"id":"83","value":"Tora"},{"id":"24","value":"Toritto"},{"id":"82","value":"Villa d'Agri"}]}]
#fermate = [{"type": "bus", "list": [{"id":"25","value":"Abriola"},{"id":"26","value":"Acerenza"},{"id":"17","value":"Altamura"},{"id":"119","value":"Arioso"},{"id":"80","value":"Atena"},{"id":"27","value":"Avigliano"},{"id":"118","value":"Badia S. Angelo"},{"id":"5","value":"Bari"},{"id":"121","value":"Basentello"},{"id":"18","value":"Binetto"},{"id":"19","value":"Bitetto"},{"id":"117","value":"Bivio Anzi"},{"id":"116","value":"Bivio Latronico"},{"id":"115","value":"Bivio Lauria"},{"id":"114","value":"Bivio Rotonda"},{"id":"112","value":"Borgo Venusio"},{"id":"81","value":"Brienza"},{"id":"28","value":"Calvello"},{"id":"122","value":"Cancellara"},{"id":"79","value":"Castelluccio"},{"id":"78","value":"Epitaffio"},{"id":"29","value":"Ferrandina"},{"id":"111","value":"Galdo"},{"id":"110","value":"Genzano di Lucania"},{"id":"109","value":"Grassano"},{"id":"20","value":"Gravina"},{"id":"77","value":"Grumo Appula"},{"id":"33","value":"Irsina"},{"id":"75","value":"Lagonegro"},{"id":"113","value":"Laino Borgo"},{"id":"34","value":"Laurenzana"},{"id":"108","value":"Lauria"},{"id":"107","value":"Mad. Pantano"},{"id":"35","value":"Marconia"},{"id":"123","value":"Marinella"},{"id":"106","value":"Marsico Nuovo"},{"id":"36","value":"Matera"},{"id":"124","value":"Mellitto"},{"id":"125","value":"Moccaro"},{"id":"22","value":"Modugno"},{"id":"37","value":"Montalbano"},{"id":"105","value":"Monteforte"},{"id":"38","value":"Montescaglioso"},{"id":"104","value":"Montocchio"},{"id":"103","value":"Nemoli"},{"id":"126","value":"Oppido Lucano"},{"id":"16","value":"Paestum"},{"id":"76","value":"Palo del Colle"},{"id":"127","value":"Pellicciari"},{"id":"102","value":"Pergola"},{"id":"128","value":"Pescariello"},{"id":"101","value":"Peschiera-Craco"},{"id":"39","value":"Pietragalla"},{"id":"40","value":"Pignola"},{"id":"41","value":"Pisticci"},{"id":"100","value":"Poggiorsini"},{"id":"99","value":"Ponte Camastra"},{"id":"98","value":"Ponte d'Inferno"},{"id":"97","value":"Ponte Mallardi"},{"id":"43","value":"Potenza"},{"id":"95","value":"Pozzi"},{"id":"94","value":"Praia a Mare"},{"id":"93","value":"Prestieri"},{"id":"129","value":"Ripa D'Api"},{"id":"92","value":"Rotonda"},{"id":"91","value":"S. Nicola"},{"id":"216","value":"Sala Consilina"},{"id":"44","value":"Salandra"},{"id":"90","value":"Sasso di Castalda"},{"id":"89","value":"Sciffra"},{"id":"88","value":"Sellata"},{"id":"87","value":"Serrapotamo"},{"id":"86","value":"Spinazzola"},{"id":"130","value":"Taccone"},{"id":"85","value":"Taverna Foia"},{"id":"96","value":"Tiera"},{"id":"84","value":"Tinchi"},{"id":"83","value":"Tora"},{"id":"24","value":"Toritto"},{"id":"82","value":"Villa d'Agri"}]}]

def time_loop():
    times = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    for time in times:
        scrape(fermate,time)

def scrape(fermate):
    for fermata in fermate:
        pairs(fermata)

def pairs(fermate_mezzo):
    filen = 0
    for a in range(0,len(fermate_mezzo["list"])-1):
        print a
        for b in range(a+1,len(fermate_mezzo["list"])):
            print b
            tipo_mezzo = ''
            if fermate_mezzo["type"] == "treno":
                tipo_mezzo = '2'
                filepath = "./data/2treno/"
            if fermate_mezzo["type"] == "bus":
                tipo_mezzo = '1'
                filepath = "./data/bus/"
            payload = {'tipo_mezzo': tipo_mezzo, 'partenza': fermate_mezzo["list"][a]["id"], 'arrivo': fermate_mezzo["list"][b]["id"], 'data': '17/11/2014', 'ore':'00','minuti':'00'}
            print payload
            text = post(payload)
            
            filename = filepath+"andata/mhoo14_fal_"+str(filen)+".html"
            html_str = "\""+text.encode('utf-8')+"\""
            Html_file = open(filename,"w")
            Html_file.write(html_str)
            Html_file.close()
           
            payload = {'tipo_mezzo': tipo_mezzo, 'partenza': fermate_mezzo["list"][b]["id"], 'arrivo': fermate_mezzo["list"][a]["id"], 'data': '17/11/2014', 'ore':'00','minuti':'00'}
            print payload
            text = post(payload)
            
            filename = filepath+"ritorno/mhoo14_fal_"+str(filen)+".html"
            html_str = "\""+text.encode('utf-8')+"\""
            Html_file = open(filename,"w")
            Html_file.write(html_str)
            Html_file.close()
            
            filen += 1



def post(payload):
   
    r = requests.post("http://ferrovieappulolucane.it/ricerca-corse", data=payload)
    return r.text


scrape(fermate)

