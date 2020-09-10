import sys
from colorama import Fore
import scripts.buble as bub
import scripts.stars as star
import scripts.alpha as alf
import scripts.fender as dt
import scripts.doom as dm
import scripts.gothic as goth
import scripts.graffity as graf
import scripts.rammstein as ram
import scripts.avatar as ava
import scripts.subzero as sub
import scripts.binary as bi
import scripts.epic as epi
import scripts.jaccy as ja
import scripts.runic as run
import scripts.shadow as shad
import scripts.slant as sl
import scripts.heart as hea
import scripts.twisted as tw
import scripts.relief as re
import scripts.linux as lx
import scripts.allitems as al


def start_hello():
    menu_string = r'''
   _______                 _           ______ _  _____ _      _   
 |__   __|               | |         |  ____(_)/ ____| |    | |  
    | |_      _____ _ __ | |_ _   _  | |__   _| |  __| | ___| |_ 
    | \ \ /\ / / _ \ '_ \| __| | | | |  __| | | | |_ | |/ _ \ __|
    | |\ V  V /  __/ | | | |_| |_| | | |    | | |__| | |  __/ |_ 
    |_| \_/\_/ \___|_| |_|\__|\__, | |_|    |_|\_____|_|\___|\__|
                               __/ |                             
                              |___/                             
 
    '''

    print(Fore.GREEN + menu_string + Fore.RESET)
    help_string = f'''
 1. buble        2. star wars
 3. ntgreek      4. fender
 5. doom         6. gothic
 7. graffiti     8. rammstein
 9. avatar       10. speed
11. binary       12. epic
13. jacky        14. banner
15. shadow       16. slant
17. heartright   18. twisted
19. relief       20. linux
21. All items     0. exit

'''
    print(help_string)


def content():
    while True:
        try:
            number = int(input('Enter a design number: '))
            if 0 <= number <= 21:
                if number == 0:
                    sys.exit()
                else:
                    if number == 1:
                        bub.parse_font1()
                    elif number == 2:
                        star.parse_font2()
                    elif number == 3:
                        alf.parse_font3()
                    elif number == 4:
                        dt.parse_font4()
                    elif number == 5:
                        dm.parse_font5()
                    elif number == 6:
                        goth.parse_font6()
                    elif number == 7:
                        graf.parse_font7()
                    elif number == 8:
                        ram.parse_font8()
                    elif number == 9:
                        ava.parse_font9()
                    elif number == 10:
                        sub.parse_font10()
                    elif number == 11:
                        bi.parse_font11()
                    elif number == 12:
                        epi.parse_font12()
                    elif number == 13:
                        ja.parse_font13()
                    elif number == 14:
                        run.parse_font14()
                    elif number == 15:
                        shad.parse_font15()
                    elif number == 16:
                        sl.parse_font16()
                    elif number == 17:
                        hea.parse_font17()
                    elif number == 18:
                        tw.parse_font18()
                    elif number == 19:
                        re.parse_font19()
                    elif number == 20:
                        lx.parse_font20()
                    elif number == 21:
                        al.parse_font1()

            else:
                print('Enter right number!')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    start_hello()
    content()
