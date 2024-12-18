from sympy import mod_inverse, integer_nthroot


def chinese_remainder_theorem(c1, c2, c3, n1, n2, n3):
    """

    M ≡ c1 (mod n1)
    M ≡ c2 (mod n2)
    M ≡ c3 (mod n3)

    """
    N = n1 * n2 * n3
    N1 = N // n1
    N2 = N // n2
    N3 = N // n3

    y1 = mod_inverse(N1, n1)
    y2 = mod_inverse(N2, n2)
    y3 = mod_inverse(N3, n3)

    M = (c1 * N1 * y1 + c2 * N2 * y2 + c3 * N3 * y3) % N

    return M


def decrypt_rsa_cubic_root(M):
    """
    Извлекает кубический корень из M.
    """
    low, high = 0, M
    while low <= high:
        mid = (low + high) // 2
        mid_cubed = mid ** 3
        if mid_cubed == M:
            return mid
        elif mid_cubed < M:
            low = mid + 1
        else:
            high = mid - 1
    # Если не нашли точного куба, попробуем найти наименьший приближённый
    return low - 1  # возвращаем приближённое значение



c1 = int(
    "10496628254461648340400353576918276584265588739633426829664787233746822123151955928432679950585975015851519912212265624146745598259048870721529745090890890072310821985256945124130337221021881115934679642415679081448055464314021115615517068674414063576283468007299140926995768666750985254029495434328599088365366258794472198097746910722612218186822935960003584849560298234982776247945808805274188272475062757608404118412761051928877757311788890737023835958265851970556783585640242802367681439803951392413949075848449266804071916745945209760467308348250220913087914662884115347991806619236221580555645642094551129889193")
c2 = int(
    "5325107969226753777805517033883836794475940747336350861025825135184507960587711622209173123231563801659683714191995749162657754591253622472981943936308893296797013592882870993102273234220310598583625043039603191634141320489204198808415027676097788090031034516151827613780121054225176272563782391643371592616497819463907472731038908907926466968467115828731727205029960056065600794746035633192139002776031909893896429701534957344459542419311408305226714424888030367174802416197967438569742675429136046584949590005014053642166788386379672634097123305325733935630446311783028359452790982694241913095390657769316207093164")
c3 = int(
    "11602654195724091334873001374230683147976734599074669203411694526840065011292816269464715825694184041401745261297411723517696707853070581288762344386026219801841771247136545318065176712059193602787019592948865517415924122762611527673832631544174092208133069261365772205384455667183941503716743804829276835966140906858260088292605911060883463853864224872938178580804874736623533758006345825490845122110770148700761078128414024247120860054374493825601782174046252464599789763890269795265308848538333841939744453815037045335620579682505397386212195628244824008625910960433871964297563041448040879590693724605867166234775")
n1 = int(
    "19888234477955222354860256149591781307886469688980288373500759557082802958103637323668318975632166969249155857072258048697436072769765678313598693804584771622239646622996522488164173719417964296688831241165612106403576876704669789424050432413388415140416849526336109639679989658118201448601716804672660911458991326003068157032795222097435269413134934509574095191824164277158000378191123796831196626442891619371014543449425992347833310185483400955730698112743309962577484242971957321225000313606880539330129982067096054289247026443788034297892746286638838226438575078604073181809126216704646205183300176957591755711791")
n2 = int(
    "16462215426489255225892584869037735577619763065989519860838801637080030927591672226844790414815229663435863181005111799666920260910332819121433039150763750515154769844420707266778970735831472810257625518535836807256601353999321259708916065202776596105716120454204639632965057361687819538291514727126827446240669829780565688168788034697938631005194048897294742524061701686370222798273196840829198492346766492702634706034700325571901381056295047855586599795841707872997241637423827684066350760466732191625840178740396120227614690299232001875384085738536799340026547128897434438327999779135729401122861875632063844321783")
n3 = int(
    "13706215893654731867849926186816326043180524404836211090671709809873197884443497737673556860673377726630586800530419687011700462294352891834139335192288140383991294148062666799078243187205290125500344475784612048042018783840147805189788256081548629527787032118887683695511417278315450335037940540435410712689437267060177678208300217469465255211061531452977176264862598540523403966377169363580708875554706717418942792212352735934755899152509436458153866483097780580383865179801030968459321891492138603780329229423834885570959324321873058646530507287406083683889974262349678955039297154311099621888857849283747864955581")

# Восстановление исходного текста
M = chinese_remainder_theorem(c1, c2, c3, n1, n2, n3)
original_message = decrypt_rsa_cubic_root(M)
print("Восстановленное исходное сообщение:", original_message)