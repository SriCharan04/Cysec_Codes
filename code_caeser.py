string = "Nv'iv ef jkirexvij kf cfmv Pfl befn kyv ilcvj reu jf uf Z R wlcc tfddzkdvek'j nyrk Z'd kyzebzex fw Pfl nflcue'k xvk kyzj wifd rep fkyvi xlp Z aljk nrek kf kvcc pfl yfn Z'd wvvczex Xfkkr drbv pfl leuvijkreu Evmvi xfeer xzmv pfl lg, evmvi xfeer cvk pfl ufne Evmvi xfeer ile rifleu reu uvjvik pfl Evmvi xfeer drbv pfl tip, evmvi xfeer jrp xffuspv Evmvi xfeer kvcc r czv reu ylik pfl Nv'mv befne vrty fkyvi wfi jf cfex Pfli yvrik'j svve rtyzex slk pfl'iv kff jyp kf jrp zk Zejzuv nv sfky befn nyrk'j svve xfzex fe Nv befn kyv xrdv reu nv'iv xfeer gcrp zk Reu zw pfl rjb dv yfn Z'd wvvczex Ufe'k kvcc dv pfl'iv kff sczeu kf jvv Evmvi xfeer xzmv pfl lg, evmvi xfeer cvk pfl ufne Evmvi xfeer ile rifleu reu uvjvik pfl Evmvi xfeer drbv pfl tip, evmvi xfeer jrp xffuspv Evmvi xfeer kvcc r czv reu ylik pfl Evmvi xfeer xzmv pfl lg, evmvi xfeer cvk pfl ufne Evmvi xfeer ile rifleu reu uvjvik pfl Evmvi xfeer drbv pfl tip, evmvi xfeer jrp xffuspv Evmvi xfeer kvcc r czv reu ylik pfl Nv'mv befne vrty fkyvi wfi jf cfex Pfli yvrik'j svve rtyzex slk pfl'iv kff jyp kf jrp zk Zejzuv nv sfky befn nyrk'j svve xfzex fe Nv befn kyv xrdv reu nv'iv xfeer gcrp zk Z aljk nrek kf kvcc pfl yfn Z'd wvvczex Xfkkr drbv pfl leuvijkreu Evmvi xfeer xzmv pfl lg, evmvi xfeer cvk pfl ufne Evmvi xfeer ile rifleu reu uvjvik pfl Evmvi xfeer drbv pfl tip, evmvi xfeer jrp xffuspv Evmvi xfeer kvcc r czv reu ylik pfl"

for K in range(1,26):
    new_string = ''
    for i in range(0,len(string)):
        ascii_value = 0
        if string[i].isalpha():
            ascii_value = ord(string[i]) + K
            if string[i].islower():
                if (ascii_value >= ord('z')):
                    ascii_value -= 26
        
            elif string[i].isupper():
                if (ascii_value >= ord('Z')):
                    ascii_value -= 26
        else:
            ascii_value = ord(string[i])
        new_string += chr(ascii_value)
    print("K = {}\n".format(K))
    print(new_string)
    print("\n\n")

