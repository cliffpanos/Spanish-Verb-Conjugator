raw_input = input

def Proc(TBP):
    AS = 0
    BS = len(TBP)-1
    CurSearch = 0
    length = len(TBP)
    Error = None
    A = 'AA'
    if TBP[AS:BS] == ' ' or TBP[AS:BS] == '  ' or TBP[AS:BS] == '':
        Error = 'False'
        return Error
    else: 
        while TBP[AS] == ' ' and AS < length - 1:
            AS += 1
        while TBP[BS] == ' 'and BS > 0:
            BS -= 1
        return TBP[AS:BS+1]

def createList(listA):
        Final = []
        word = ''
        Yes = 'NO'
        for c in listA:
            if c not in [',']:
                word = word + c
                Yes = 'YES'
            else:
                if Yes != 'NO':
                    Final.append(word)
                    Yes = 'NO'
                    word = ''
        if Yes != 'NO':
                Final.append(word)
                Yes = 'NO'
                word = ''
        Search = 0
        for a in Final:
            Final[Search] = Proc(a)
            Search +=1
        Search = 0
        return Final

def Wait(sec):
        b = 0
        Proc = 0
        while b < 45*sec:
                b = b + 0.00001
                Proc += 1
    
def Any(verb):
    S = 0
    A = 0
    pos = ['tener','estar','venir','haber','hacer','salir','caber','valer','querer','poner','traer','decir','poder','saber','abrir','cubrir','escribir','freir','morir','resolver','romper','volver']
    while pos[S] not in verb and S<len(pos)-1:
        S += 1
    B = len(pos[S])
    while verb[A:B] != pos[S] and B<len(verb) and pos[S] in verb:
        A += 1
        B += 1
    if verb[A:B] in pos:
        stem = verb[0:A]
        return stem
    return False

def Participle(verb):
    stem = ''
    S = 0
    Irreg = ['abrir','cubrir','decir','escribir','freir','hacer','morir','poner','resolver','romper','volver']
    Irreg2 = ['abierto','cubierto','dicho','escrito','frito','hecho','muerto','puesto','resuelto','roto','vuelto']
    if Any(verb) != False: stem = Any(verb)
    verb = verb[len(stem):len(verb)]
    if verb == 'ir': return 'ido'
    if verb == 'ver': return 'visto'
    if verb in Irreg:
        while S < len(Irreg):
            if Irreg[S] in verb:
                return stem + Irreg2[S]
            else: S +=1
    if verb[len(verb)-2:len(verb)] == 'ar': return verb[0:len(verb)-2] + 'ado'
    if verb[len(verb)-2:len(verb)] in ['er','ir']:
        verb = verb[0:len(verb)-2] + 'ido'
        if verb[len(verb)-4] in ['a','e','i','o','u']:
            verb = verb[0:len(verb)-3] + 'í' + verb[len(verb)-2:len(verb)]
        return verb
    
def StemChange(verb,sub,tense):
    CurSearch = 0
    ASearch = 0
    seq = 0
    Ex = 'in'
    length = len(verb)
    A = 'AA'
    eie = ['preferir','querer','cerrar','entender','comenzar','empezar','pensar','perder']
    oue = ['poder','costar','mover','dormir','almorzar','recordar','volver','encontrar','volar','whorer']
    ei = ['repetir','pedir','servir','competir','seguir','conseguir']
    if Any(verb) != False and verb not in eie: eie.append(verb)
    if verb in eie and tense == 'present': Stem = 0
    if verb in ei or tense == 'preterite': Stem = 1
    if verb in oue and tense == 'present': Stem2 = 'ue'
    if verb in oue and tense == 'preterite': Stem2 = 'u'
    if (tense == 'present' and (verb in eie or verb in ei)) or ((tense == 'preterite') and (verb[len(verb)-2:len(verb)] == 'ir') and (verb in eie or verb in ei)) and (verb in eie or verb in ei):
        SecE = None
        if verb[len(verb)-2:len(verb)] == 'er':
            CurSearch = len(verb) - 1
            while A == 'AA':
                if Ex == 'out': break
                while verb[CurSearch] != 'e' and CurSearch > 0:
                    CurSearch -= 1
                seq += 1
                if seq == 2:
                    verb = verb[0:CurSearch] +'i'+ verb[CurSearch:len(verb)]
                    Ex = 'out'
                    break
                else:
                    CurSearch -= 1
                    A = 'AA'
        else:
            CurSearch = 0
            while A == 'AA':
                if Ex == 'out': break
                seq += 1
                while CurSearch < len(verb) - 1 and verb[CurSearch] != 'e':
                    CurSearch += 1
                if seq == 1:
                    FirstE = CurSearch
                    CurSearch += 1
                    A = 'AA'
                if seq == 2:
                    if verb[CurSearch] == 'e':
                        if CurSearch + 1 == len(verb)-1:
                            Ex = 'out'
                            SecE = None
                            break
                        else:
                            SecE = CurSearch
                            Ex = 'out'
                            break
                    else: break
            if SecE == None: verb = verb[0:FirstE] +'i'+ verb[FirstE+Stem:len(verb)]
            else: verb = verb[0:SecE] +'i'+ verb[SecE+Stem:len(verb)]
    if (tense == 'present' and (verb in oue)) or (tense == 'preterite' and (verb[len(verb)-2:len(verb)] == 'ir') and (verb in oue)):
        CurSearch = 0
        SecE = None
        while A == 'AA':
            if Ex == 'out': break
            seq += 1
            while verb[CurSearch] != 'o' and CurSearch < len(verb) - 1:
                CurSearch += 1
            if seq == 1:
                FirstE = CurSearch
                CurSearch += 1
                A = 'AA'
            if seq == 2:
                if verb[CurSearch] == 'o':
                    if CurSearch + 1 == len(verb)-1:
                        Ex = 'out'
                        SecE = None
                        break
                    else:
                        SecE = CurSearch
                        Ex = 'out'
                        break
                else: break
        if SecE == None: verb = verb[0:FirstE] + Stem2 + verb[FirstE+1:len(verb)]
        else: verb = verb[0:SecE] + Stem2 + verb[SecE+1:len(verb)]
    return verb

def Conj(verb,sub,tense):
    if tense == 'present':
        Ar = ['o','as','a','amos','áis','an']
        Er = ['o','es','e','emos','éis','en']
        Ir = ['o','es','e','imos','ís','en']
        ser = ['soy','eres','es','somos','sois','son']
        tener = ['tengo','tienes','tiene','tenemos','tenéis','tienen']
        estar = ['estoy','estás','está','estamos','estáis','están']
        ir = ['voy','vas','va','vamos','vais','van']
        jugar = ['juego','juegas','juega','jugamos','jugáis','juegan']
        ver = ['veo','ves','ve','vemos','véis','ven']
        venir = ['vengo','vienes','viene','venimos','venís','vienen']
        poner = ['pongo','pones','pone','ponemos','ponéis','ponen']
        traer = ['traigo','traes','trae','traemos','traéis','traen']
        decir = ['digo','dices','dice','decimos','decís','dicen']
        hacer = ['hago','haces','hace','hacemos','hacéis','hacen']
        conocer = ['conozco','conoces','conoce','conocemos','conocéis','conocen']
        saber = ['sé','sabes','sabe','sabems','sabéis','saben']
        dar = ['doy','das','da','damos','dais','dan']
        stem = ''
        if Any(verb) != False: stem = Any(verb)
        if verb == 'ser': return ser[sub-1]
        if 'tener' in verb: return stem + tener[sub-1]
        if 'estar' in verb: return stem + estar[sub-1]
        if 'venir' in verb: return stem + venir[sub-1]
        if 'poner' in verb: return stem + poner[sub-1]
        if 'traer' in verb: return stem + traer[sub-1]
        if 'decir' in verb: return stem + decir[sub-1]
        if 'hacer' in verb: return stem + hacer[sub-1]
        if 'conocer' in verb: return stem + conocer[sub-1]
        if 'saber' in verb: return stem + saber[sub-1]
        if verb == 'dar': return dar[sub-1]
        if verb == 'ir': return ir[sub-1]
        if verb == 'jugar': return jugar[sub-1]
        if verb == 'ver': return ver[sub-1]
        if verb == 'seguir' and sub == 1: return 'sigo'
        if sub in [1,2,3,6]: verb = StemChange(verb,sub,tense)
        if verb[len(verb)-2:len(verb)] == 'ar':
            Word = verb[0:len(verb)-2] + Ar[sub-1]
            return Word
        if verb[len(verb)-2:len(verb)] == 'er':
            Word = verb[0:len(verb)-2] + Er[sub-1]
            return Word
        if verb[len(verb)-2:len(verb)] == 'ir':
            Word = verb[0:len(verb)-2] + Ir[sub-1]
            return Word
    elif tense == 'preterite':
        Ar = ['é','aste','ó','amos','asteis','aron']
        Er = ['í','iste','ió','imos','isteis','ieron']
        OIEnding = ['e','iste','o','imos','isteis','ieron']
        dar_ver = ['i','iste','io','imos','isteis','ieron']
        VowelErIr = ['í','íste','yó','ímos','ísteis','yeron']
        OtherIrreg = ['super','puser','tuvir','estuvir','vinir','quisir','puder','cuper','anduvar','trajir','dijir','huber']
        ser_ir = ['fui','fuiste','fue','fuimos','fuisteis','fueron']
        hacer = ['hice','hiciste','hizo','hicimos','hicisteis','hicieron']
        stem = ''
        if Any(verb) != False:
            stem = Any(verb)
        if 'saber' in verb:
            verb = stem + 'super'
            OtherIrreg.append(verb)
        if 'poner' in verb:
            verb = stem + 'puser'
            OtherIrreg.append(verb)
        if 'tener' in verb:
            verb = stem + 'tuvir'
            OtherIrreg.append(verb)
        if 'estar' in verb:
            verb = stem + 'estuvir'
            OtherIrreg.append(verb)
        if 'venir' in verb:
            verb = stem + 'vinir'
            OtherIrreg.append(verb)
        if 'querer' in verb:
            verb = stem + 'quiser'
            OtherIrreg.append(verb)
        if 'poder' in verb:
            verb = stem + 'puder'
            OtherIrreg.append(verb)
        if 'caber' in verb:
            verb = stem + 'cuper'
            OtherIrreg.append(verb)
        if 'traer' in verb:
            verb = stem + 'trajir'
            OtherIrreg.append(verb)
        if 'andar' in verb:
            verb = stem + 'anduvar'
            OtherIrreg.append(verb)
        if 'decir' in verb:
            verb = stem + 'dijir'
            OtherIrreg.append(verb)
        if 'haber' in verb:
            verb = stem + 'huber'
            OtherIrreg.append(verb)
        if verb == 'ser' or verb == 'ir': return ser_ir[sub-1]
        if verb == 'dar' or verb == 'ver': return verb[0] + dar_ver[sub-1]
        if verb == 'hacer': return hacer[sub-1]
        if verb[len(verb)-4:len(verb)] == 'ucir': verb = verb[0:len(verb)-4] + 'ujir'
        if verb in OtherIrreg or verb[len(verb)-4:len(verb)] == 'ujir':
            if verb[len(verb)-3:len(verb)] == 'jir' and sub == 6:
                verb = verb[0:len(verb)-2] + 'eron'
            else: verb = verb[0:len(verb)-2] + OIEnding[sub-1]
            return verb
        if ((verb == 'leer' or verb == 'creer' or verb == 'caer' or verb == 'oir') or (verb[len(verb)-3] in ['a','e','i','o','u'])) and (verb[len(verb)-2:len(verb)] in ['er','ir']): return verb[0:len(verb)-2] + VowelErIr[sub-1]
        if sub == 3 or sub == 6: verb = StemChange(verb,sub,tense)
        if sub == 1:
            if verb[len(verb)-3:len(verb)] == 'car':
                Word = verb[0:len(verb)-3] + 'qué'
                return Word
            if verb[len(verb)-3:len(verb)] == 'gar':
                Word = verb[0:len(verb)-3] + 'gué'
                return Word
            if verb[len(verb)-3:len(verb)] == 'zar':
                Word = verb[0:len(verb)-3] + 'cé'
                return Word
        if verb[len(verb)-2:len(verb)] == 'ar':
            Word = verb[0:len(verb)-2] + Ar[sub-1]
        elif verb[len(verb)-2:len(verb)] == 'er' or verb[len(verb)-2:len(verb)] == 'ir':
            Word = verb[0:len(verb)-2] + Er[sub-1]
        return Word
    elif tense == 'future' or tense == 'conditional':
        FUT = ['é','ás','á','emos','éis','án']
        COND = ['ía','ías','ía','íamos','íais','ían']
        stem = ''
        if Any(verb) != False: stem = Any(verb)
        if 'caber' in verb: verb = stem + 'cabr'
        if 'poner' in verb: verb = stem + 'pondr'
        if 'tener' in verb: verb = stem + 'tendr'
        if 'decir' in verb: verb = stem + 'dir'
        if 'venir' in verb: verb = stem + 'vendr'
        if 'querer' in verb: verb = stem + 'querr'
        if 'poder' in verb: verb = stem + 'podr'
        if 'haber' in verb: verb = stem + 'habr'
        if 'salir' in verb: verb = stem + 'saldr'
        if 'hacer' in verb: verb = stem + 'har'
        if 'valer' in verb: verb = stem + 'valdr'
        if 'saber' in verb: verb = stem + 'sabr'
        if tense == 'conditional': return verb + COND[sub-1]
        if tense == 'future': return verb + FUT[sub-1]
    elif tense == 'imperfect':
        Ar = ['aba','abas','aba','ábamos','abais','aban']
        EIr = ['ía','ías','ía','íamos','íais','ían']
        Irreg = ['ser','ir','ver']
        ser = ['era','eras','era','éramos','erais','eran']
        ir = ['iba','ibas','iba','íbamos','ibais','iban']
        ver = ['veía','veías','veía','veíamos','veíais','veían']
        if verb in Irreg:
            if verb == 'ser':
                return ser[sub-1]
            if verb == 'ir':
                return ir[sub-1]
            if verb == 'ver':
                return ver[sub-1]
        else:
            if verb[len(verb)-2:len(verb)] == 'ar':
                Word = verb[0:len(verb)-2] + Ar[sub-1]
            if verb[len(verb)-2:len(verb)] == 'er' or verb[len(verb)-2:len(verb)] == 'ir':
                Word = verb[0:len(verb)-2] + EIr[sub-1]
            return Word
    elif tense == 'pluperfect' or tense == 'present perfect' or tense == 'future perfect' or tense == 'conditional perfect':
        Past = ['había','habías','había','habíamos','habíais','habían']
        Present = ['he','has','has','hemos','habéis','han']
        Future = ['habré','habrás','habrá','habremos','habréis','habrán']
        Conditional = ['habría','habrías','habría','habríamos','habríais','habrían']
        if tense == 'pluperfect': Prefix = Past[sub-1]
        if tense == 'present perfect': Prefix = Present[sub-1]
        if tense == 'future perfect': Prefix = Future[sub-1]
        if tense == 'conditional perfect': Prefix = Conditional[sub-1]
        return Prefix + ' ' + Participle(verb)
    elif tense == 'command':
        rEndings = ['me','te','se','nos','os','se']
        rEnding = ''
        if ending == 'se': rEnding = rEndings[sub-1]

 #       ü
        
        if sub == 1: return 'Really? You want a "yo" command??? No such thing, genius.'
        if sub == 2:
            Ar = ['a','es']
        if sub == 3:
            a
        if sub == 4:
            a
        if sub == 5:
            a
    elif tense == 'present progressive':
        rEndings = ['me','te','se','nos','os','se']
        rEnding = ''
        Ar = 'ando'
        ErIr = 'iendo'
        if verb == 'ir' or (verb[len(verb)-3] in ['a','e','i','o','u']): ErIr = 'yendo'
        if ending == 'se':
            rEnding = rEndings[sub-1]
            verb = verb[0:len(verb)-2]
        estar = ['estoy','estás','está','estamos','estáis','están']
        if verb[len(verb)-2:len(verb)] == 'ar': return estar[sub-1] + ' ' + verb[0:len(verb)-2] + Ar + rEnding
        if verb[len(verb)-2:len(verb)] in ['er','ir']: return estar[sub-1] + ' ' + verb[0:len(verb)-2] + ErIr + rEnding
start = 'go'
while start == 'go':
    restart = 'no'
    Entry = str(raw_input("Please enter one or more infinitives separated by commas: "))
    if ',' not in Entry:
        TBP = Entry
        if Entry == False:
            print (' ')
            print ('Sorry, but you must enter at least one infinitive')
            start = 'go'
        else:
            VerbList = []
            VerbList.append(Proc(TBP))
    else:
        VerbList = createList(Entry)
    for Verb in VerbList:
        ending = Verb[len(Verb)-2:len(Verb)]
        accEndings = ['ar','er','ir']
        if ending not in accEndings and ending != 'se':
            print (' ')
            print ("Sorry, but infinitives must end in either 'ar', 'er', or 'ir'.")
            print (' ')
            ask = 'no'
            start = 'go'
            Tensask = 'no'
        else:
            if ending in accEndings:
                Tensask = 'yes'
            else:
                if ending == 'se':
                    ending2 = Verb[len(Verb)-4:len(Verb)-2]
                    if ending2 in accEndings:
                        Tensask = 'yes'
                    else:
                        print (' ')
                        print ("Sorry, but infinitives must end in either 'ar', 'er', or 'ir'.")
                        print (' ')
                        ask = 'no'
                        start = 'go'
                        Tensask = 'no'
                else:
                    print (' ')
                    print ("Sorry, but infinitives must end in either 'ar', 'er', or 'ir'.")
                    print (' ')
                    ask = 'no'
                    start = 'go'
                    Tensask = 'no'
    while Tensask == 'yes':
        if restart == 'go':
            restart = 'no'
            break
        print (' ')
        S = ''
        if len(VerbList) > 1: S = 's'
        tense = str(raw_input('Please enter a tense to conjugate the verb for, or type all: '))
        TBP = tense
        TenseList = []
        if ',' not in tense:
            if Proc(TBP) != False: TenseList.append(Proc(TBP))
        else:
            TenseList = createList(tense)
        if tense == 'all':
            TenseList = ['pres','pret','imp','pres perf','past','fut','fut perf','cond','cond perf','pres prog']
        FinalTenseList = []
        for tense in TenseList:
            if tense in ['present','Present','pres','Pres']:
                tense = 'present'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['preterite','Preterite','pret','Pret']:
                tense = 'preterite'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['future','fut','Future','Fut']:
                tense = 'future'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['imp','Imp','imperfect','Imperfect']:
                tense = 'imperfect'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['Past','past','past perfect','Past Perfect','pluperfect','Pluperfect','plu']:
                tense = 'pluperfect'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['Pres Perf','pres perf','Present Perfect','present perfect']:
                tense = 'present perfect'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['Fut Perf','fut perf','Future Perfect','future perfect']:
                tense = 'future perfect'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['cond','Cond','conditional','Conditional']:
                tense = 'conditional'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['Cond Perf','cond perf','conditional perfect','Conditional Perfect']:
                tense = 'conditional perfect'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['command','Command','com','Com']:
                tense = 'command'
                FinalTenseList.append(tense)
                ask = 'yes'
            elif tense in ['Pres Prog','pres prog','present progressive','Present Progressive','Gerund','gerund']:
                tense = 'present progressive'
                FinalTenseList.append(tense)
                ask = 'yes'
            else:
                print (' ')
                print ('Sorry, but the', '"' + tense + '"', 'tense is not supported by this program.')
                ask = 'no'
                Tensask = 'yes'
        while ask == 'yes':
            if restart == 'go':
                print (' ')
                break
            print (' ')
            SS = ''
            if len(VerbList) > 1: SS = 's'
            end = str(raw_input("Please enter a subject to conjugate the verb for, or type all: "))
            TBP = end
            EndList = []
            if ',' not in end:
                if Proc(TBP) != False: EndList.append(Proc(TBP))
            else:
                EndList = createList(end)
            if end == 'all':
                EndList = ['yo','tu','el','nosotros','vosotros','ellos']
            FinalEndList = []
            for end in EndList:
                if end == 'all': break
                sub = 'Non'
                if end in ['Yo','yo']:
                    FinalEndList.append(1)
                elif end in ['Tu','tu']:
                    FinalEndList.append(2)
                elif end in ['el','El','ella','Ella','Ud','ud','usted','Usted']:
                    FinalEndList.append(3)
                elif end in ['Nos','nos','nosotros','Nosotros','nosotras','Nosotras']:
                    FinalEndList.append(4)
                elif end in ['vosotros','Vosotros','vos','Vos']:
                    FinalEndList.append(5)
                elif end in ['Ellos','ellos','Ellas','ellas','Usteded','ustedes','Uds','uds']:
                    FinalEndList.append(6)
                else:
                    print (' ')
                    print ('Sorry, but', '"' + end + '"', 'is not a real subject in spanish.')
                    ask = 'no'
                    ask = 'yes'
                    restart = 'no'
            if FinalEndList == []:
                ask = 'yes'
            else:
                for Verb in VerbList:
                    No = ''
                    if Verb[0:3] == 'no ' and tense != 'command':
                        No = 'no '
                        Verb = Verb[3:len(Verb)]
                    for tense in FinalTenseList:
                        print(' ')
                        print(tense.title(), 'form', 'of','"' + Verb + '"' + ':')
                        for sub in FinalEndList:
                            RefPro = Verb
                            ending = Verb[len(Verb)-2:len(Verb)]
                            if ending == 'se' and tense not in ['command','present progressive']: verb = Verb[0:len(Verb)-2]
                            else: verb = Verb
                            result = Conj(verb,sub,tense)
                            if ending == 'se' and tense not in ['command','present progressive']:
                                rEndings = ['me ','te ','se ','nos','os ','se ']
                                result = rEndings[sub-1] + ' ' + result
                            print((['yo       ','tú       ','él       ','nosotros ','vosotros ','ellos    '])[sub-1], No + result)
            Quest = 'ask'
            while Quest == 'ask':
                Wait(1)
                print (' ')
                quest = str(raw_input("Would you like to conjugate for another subject, another tense, or start over?: "))
                TBP = quest
                quest = Proc(TBP)
                if quest in ['start','Start','Start over','start over']:
                    restart = 'go'
                    break
                elif quest in ['conjugate','Conjugate','another subject','another']:
                    ask = 'yes'
                    break
                elif quest in ['tense','another tense','an tense','Tense','an t']:
                    ask = 'no'
                    Tensask = 'yes'
                    break
                else:
                    print (' ')
                    print ("Sorry, I didn't get that.")
                    Quest = 'ask'
    start = 'go'
