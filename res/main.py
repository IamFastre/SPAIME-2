import os, sys
from os.path import dirname, join, abspath

if __name__ == "__main__":
    sys.path.insert(0, abspath(join(dirname(__file__), '..')))

########################################
# Importing important files & modules. #
########################################

# Importing the other py files.
from res.colors import *
from res.codes import *
from res.libs import *
from time import *

import apps.ttt as ttt
import apps.rps as rps
import apps.rnd as rnd
import apps.msp as msp

import os, sys, atexit, shutil, random

# Installing/importing other modules that are just as important.
# Hope you don't mind. :)
try:
    import yaml, keyboard
except:
    print(f"{x.YELLOW}>>{x.GRAY} Gonna do some PIP'ing for ya{c.END}")
    try:
        os.system('pip install pyyaml')
        os.system('pip install keyboard')
    except:
        os.system('sudo pip install pyyaml')
        os.system('sudo pip install keyboard')
    sleep(2)
finally:
    import yaml, keyboard



#================================================================================================================================#

###########################
# Reading the YAML files. #
###########################

# Updating the 'user.yml' file.
def user_update():
    with open('./data/user.yml', 'w') as user_yaml:
        yaml.safe_dump(user, user_yaml)

# Updating the 'settings.yml' file.
def settings_update():
    with open('./data/settings.yml', 'w') as settings_yaml:
        yaml.safe_dump(settings, settings_yaml)

# Updating the 'apps.yml' file.
def games_update():
    with open('./data/apps.yml', 'w') as apps_yaml:
        yaml.safe_dump(apps, apps_yaml)

# Resting the 'user.yml' file by copying the .old one.
def user_reset():
    global user

    shutil.copy('./data/.old/user.yml', './data/')
    with open('./data/user.yml', 'rb') as user_yaml:
        user = yaml.safe_load(user_yaml)

# Resting the 'settings.yml' file by copying the .old one.
def settings_reset():
    global settings
    shutil.copy('./data/.old/settings.yml', './data/')

    with open('./data/settings.yml', 'rb') as settings_yaml:
        settings = yaml.safe_load(settings_yaml)

# Resting the 'apps.yml' file by copying the .old one.
def games_reset():
    global apps
    shutil.copy('./data/.old/apps.yml', './data/')

    with open('./data/apps.yml', 'rb') as apps_yaml:
        apps = yaml.safe_load(apps_yaml)
        
def ttt_reset():
    global apps
    apps['ttt'] = {'last-board': '—————————', 'last-winner': '—', 'x-wins': 0, 'o-wins': 0, 'ties': 0}
    games_update()
    
def rps_reset():
    global apps
    apps['rps'] = {'p1': {'wins': 0, 'last-choice': '—'}, 'p2': {'wins': 0, 'last-choice': '—'}, 'cpu': {'wins': 0, 'last-choice': '—'}, 'ties': 0}
    games_update()
    
def rnd_reset():
    global apps
    apps['rnd'] = {'ties': 0, 'heads': 0, 'tails': 0, 'flips': 0, 'last-heads': 0, 'last-tails': 0, 'last-flips': 0, 'last-winner': '—'}
    games_update()

def msp_reset():
    global apps
# Resting all files by copying the .old ones.
def all_reset():
    user_reset()
    settings_reset()
    games_reset()

#######################################
# Checks for the YAML files presence. #
#######################################

# Checks if 'user.yml' is present.
try:
    with open('./data/user.yml', 'rb') as user_yaml:
        user = yaml.safe_load(user_yaml)
except:
    print(f"{x.YELLOW}>>{x.GRAY} Some YAML files are missing. {c.END}")
    sleep(1)
    user_reset()
finally:
    with open('./data/user.yml', 'rb') as user_yaml:
        user = yaml.safe_load(user_yaml)

# Checks if 'settings.yml' is present.
try:
    with open('./data/settings.yml','rb') as settings_yml:
        settings = yaml.safe_load(settings_yml)
except:
    print(f"{x.YELLOW}>>{x.GRAY} Some YAML files are missing. {c.END}")
    sleep(1)
    settings_reset()
finally:
    with open('./data/settings.yml','rb') as settings_yml:
        settings = yaml.safe_load(settings_yml)

# Checks if 'apps.yml' is present.
try:
    with open('./data/apps.yml', 'rb') as apps_yml:
        apps = yaml.safe_load(apps_yml)
except:
    print(f"{x.YELLOW}>>{x.GRAY} Some YAML files are missing. {c.END}")
    sleep(1)
    games_reset()
finally:
    with open('./data/apps.yml', 'rb') as apps_yml:
        apps = yaml.safe_load(apps_yml)

# Checks if 'user.yml' is OK.
try:
    print(f"{user['name']}, {user['age']}")
except:
    print("Reset")
    user_reset()
finally:
    clear()

# Checks if 'settings.yml' is OK
try:
    print(f"{settings['prefix']}, {settings['first-time']}")
except:
    print("Reset")
    settings_reset()
finally:
    clear()

# Checks if 'apps.yml' is OK
try:
    print(f"{apps}")
except:
    print("Reset")
    games_reset()
finally:
    clear()

# So I can debug happily.
admin = ("fastre", "mahmoud", "neria", "spaime")

window = None
exited = False

commands = {
    'help' : settings['prefix'] +  f'help' ,
    'exit' : settings['prefix'] +  f'exit' ,
    'home' : settings['prefix'] +  f'home' ,
    'dev1' : settings['prefix'] +  f'dev1' ,
    'dev2' : settings['prefix'] +  f'dev2' ,
    'reset': settings['prefix'] +  f'reset',
    
    '': settings['prefix'] + f''
}
placeholders = {
    'nl'            : '{' + 'nl' + '}',
    'br'            : '{' + 'br' + '}',
    
    'name'          : '{' + 'name' + '}',
    'age'           : '{' + 'age' + '}',
    
    'prefix'        : '{' + 'prefix' + '}',
    
    'lastTTTWinner' : '{' + 'lastTTTWinner' + '}',
    'lastTTTBoard'  : '{' + 'lastTTTBoard' + '}',
    'xWins'         : '{' + 'xWins' + '}',
    'oWins'         : '{' + 'oWins' + '}',
    'tttTies'       : '{' + 'tttTies' + '}',
    
    'g'             : '{' + 'g' + '}',
    'pi'            : '{' + 'pi' + '}',
    'e'             : '{' + 'e' + '}',
    'tau'           : '{' + 'tau' + '}',
    'phi'           : '{' + 'phi' + '}',
    
    'p1Last'   : '{' + 'p1Last' + '}',
    'p1Wins'   : '{' + 'p1Wins' + '}',
    'p2Last'   : '{' + 'p2Last' + '}',
    'p2Wins'   : '{' + 'p2Wins' + '}',
    'cpuLast'   : '{' + 'cpuLast' + '}',
    'cpuWins'   : '{' + 'cpuWins' + '}',
    'lastRPSWinner'   : '{' + 'lastRPSWinner' + '}',
    'rpsTies'   : '{' + 'rpsTies' + '}',
    
    'heads'   : '{' + 'heads' + '}',
    'tails'   : '{' + 'tails' + '}',
    'flips'   : '{' + 'flips' + '}',
    'rndTies'   : '{' + 'rndTies' + '}',
    'lastHeads'   : '{' + 'lastHeads' + '}',
    'lastTails'   : '{' + 'lastTails' + '}',
    'lastFlips'   : '{' + 'lastFlips' + '}',
    'lastRNDWinner'   : '{' + 'lastRNDWinner' + '}',
    
    ''   : '{' + '' + '}',
}
def is_command(thing):
    aller = []
    for cmd in commands:
        aller.append(commands[cmd])
    return thing in aller

def is_admin():
    return (user['name'].casefold() in admin and user['age'] == 576957)



#================================================================================================================================#
#=====================================================This is Important shit=====================================================#
#================================================================================================================================#


# Runs some checks before submitting your input.
def woosh_back():
    global window
    eval(window)


def choice_check(thing):

    # Placeholders:
    if "{" in thing and "}" in thing:
        if placeholders['nl'] in thing:
            thing = thing.replace(placeholders['nl'], f"\n{x.YELLOW}>>{x.VIOLET}=============================={x.YELLOW}<<{c.END}\n{x.YELLOW}>>{x.VIOLET} ")
        if placeholders['br'] in thing:
            thing = thing.replace(placeholders['br'], f"\n{x.YELLOW}>>{x.VIOLET} ")
            
        if placeholders['name'] in thing:
            thing = thing.replace(placeholders['name'], str(user['name']))
        if placeholders['age'] in thing:
            thing = thing.replace(placeholders['age'], str(user['age']))
            
        if placeholders['prefix'] in thing:
            thing = thing.replace(placeholders['prefix'], str(settings['prefix']))
            
        if placeholders['lastTTTWinner'] in thing:
            thing = thing.replace(placeholders['lastTTTWinner'], str(apps['ttt']['last-winner'])) 
        if placeholders['xWins'] in thing:
            thing = thing.replace(placeholders['xWins'], str(apps['ttt']['x-wins']))
        if placeholders['oWins'] in thing:
            thing = thing.replace(placeholders['oWins'], str(apps['ttt']['o-wins']))
        if placeholders['tttTies'] in thing:
            thing = thing.replace(placeholders['tttTies'], str(apps['ttt']['ties']))
        if placeholders['lastTTTBoard'] in thing:
            thing = thing.replace(placeholders['lastTTTBoard'], f"\n{ttt.displayBoard(apps['ttt']['last-board'], True, left=f'{x.YELLOW}>>{c.END} ')}{x.YELLOW}>>{x.VIOLET} ")
        
        if placeholders['p1Last'] in thing:
            thing = thing.replace(placeholders['p1Last'], str(apps['rps']['p1']['last-choice']))
        if placeholders['p2Last'] in thing:
            thing = thing.replace(placeholders['p2Last'], str(apps['rps']['p2']['last-choice']))
        if placeholders['cpuLast'] in thing:
            thing = thing.replace(placeholders['cpuLast'], str(apps['rps']['cpu']['last-choice']))
        if placeholders['p1Wins'] in thing:
            thing = thing.replace(placeholders['p1Wins'], str(apps['rps']['p1']['wins']))
        if placeholders['p2Wins'] in thing:
            thing = thing.replace(placeholders['p2Wins'], str(apps['rps']['p2']['wins']))
        if placeholders['cpuWins'] in thing:
            thing = thing.replace(placeholders['cpuWins'], str(apps['rps']['cpu']['wins']))
        if placeholders['rpsTies'] in thing:
            thing = thing.replace(placeholders['rpsTies'], str(apps['rps']['ties']))
        if placeholders['lastRPSWinner'] in thing:
            thing = thing.replace(placeholders['lastRPSWinner'], str(apps['rps']['last-winner']))

        if placeholders['heads'] in thing:
            thing = thing.replace(placeholders['heads'], str(apps['rnd']['heads']))
        if placeholders['tails'] in thing:
            thing = thing.replace(placeholders['tails'], str(apps['rnd']['tails']))
        if placeholders['flips'] in thing:
            thing = thing.replace(placeholders['flips'], str(apps['rnd']['flips']))
        if placeholders['rndTies'] in thing:
            thing = thing.replace(placeholders['rndTies'], str(apps['rnd']['ties']))
        if placeholders['lastHeads'] in thing:
            thing = thing.replace(placeholders['lastHeads'], str(apps['rnd']['last-heads']))
        if placeholders['lastTails'] in thing:
            thing = thing.replace(placeholders['lastTails'], str(apps['rnd']['last-tails']))
        if placeholders['lastFlips'] in thing:
            thing = thing.replace(placeholders['lastFlips'], str(apps['rnd']['last-flips']))
        if placeholders['lastRNDWinner'] in thing:
            thing = thing.replace(placeholders['lastRNDWinner'], str(apps['rnd']['last-winner']))
            
        if placeholders['g'] in thing:
            thing = thing.replace(placeholders['g'], "9.8")
        if placeholders['e'] in thing:
            thing = thing.replace(placeholders['e'], "2.7182")
        if placeholders['pi'] in thing:
            thing = thing.replace(placeholders['pi'], "3.1415")
        if placeholders['tau'] in thing:
            thing = thing.replace(placeholders['tau'], "6.2830")
        if placeholders['phi'] in thing:
            thing = thing.replace(placeholders['phi'], "1.618")
        
        if placeholders[''] in thing:
            thing = thing.replace(placeholders[''], "")

    # Commands:


    if len(thing) > 0 and thing[0] == settings['prefix']:
        
        # Unknown command
        if thing[0] == settings['prefix'] and not is_command(thing):
            clear()
            print(f"{x.RED}>>{x.GRAY} Unknown Command.{c.END}")
            woosh_back()
        
        # CMD Template
        #if thing == commands['CMD_NAME_HERE']:
        #    pass

        # Help Command
        if thing == commands['help']:
            clear()
            help_menu()
            clear()

        # Exit Command
        if thing == commands['exit']:
            exit_app()

        # Home Command
        if thing == commands['home']:
            clear()
            print(f"{x.YELLOW}>>{x.GRAY} Wooshed back!{c.END}")
            main_menu()

        # Dev/Debug Command 1
        if thing == commands['dev1']:
            if is_admin():
                clear()
                def debug1():
                    print(f"\n{x.ORANGE}>>>{x.VIOLET} Hey boss! What do you wish to do?{c.END}")
                    dev = input(f"\n{x.ORANGE}1 >{x.LETTUCE} ")
                    print(c.END)
                    try:
                        print(eval(dev))
                        print("")
                    except:
                        output.invalid(f"IDK WTF You did, maybe {settings['prefix']}dev again.")
                        enterContinue()
                        clear()
                        output.invalid(f"IDK WTF You did, maybe {settings['prefix']}dev again.")
                        main_menu()
                    else:
                        debug1()
                debug1()
            else:
                clear()
                output.invalid("It's a dev-only commands, buddy.")
                woosh_back()
                
        # Dev/Debug Command 2
        if thing == commands['dev2']:
            if is_admin():
                clear()
                def debug2():
                    print(f"\n{x.ORANGE}>>>{x.VIOLET} Hey boss! What do you wish to do?{c.END}")
                    dev = input(f"\n{x.ORANGE}2 >{x.LETTUCE} ")
                    print(c.END)
                    try:
                        print(exec(dev))
                        print("")
                    except:
                        output.invalid(f"IDK WTF You did, maybe {settings['prefix']}dev again.")
                        enterContinue()
                        clear()
                        output.invalid(f"IDK WTF You did, maybe {settings['prefix']}dev again.")
                        main_menu()
                    else:
                        debug2()
                debug2()
            else:
                clear()
                output.invalid("It's a dev-only commands, buddy.")
                woosh_back()
                
    elif len(thing) == 0:
        clear()
        print(f"{x.RED}>>{x.GRAY} You gotta input something first, no? {c.END}")
        woosh_back()
        sleep(5)
    
    # End
    return thing

def last_check(choice):
    if not is_command(choice):
        output.invalid()
    woosh_back()



#================================================================================================================================#
#================================================================================================================================#
#================================================================================================================================#


###################################
# Defining objects and constants. #
###################################

# Some frequent outputs.
class output():

    def invalid(string=False):
        if not string:
            print(f"{x.RED}>>{x.GRAY} Invalid Input.{c.END}")
        else:
            print(f"{x.RED}>>{x.GRAY} {string}{c.END}")

    def note(num):
        if num == 1:
            print(f'''{x.WHITE}!!: {x.GRAY}Type {c.ITALIC}"{commands['help']}"{c.END}{x.GRAY} to get a list of available commands.{c.END}''')
            if is_admin():
                print(f'''{x.WHITE}!!: {x.GRAY}You're in dev mode.{c.END}''')
        else:
            print(f'''{x.WHITE}!!: {x.GRAY}{num}{c.END}''')    
        print(c.END)

# Decoding encoded messages.
class decoded():

    n69 = asciiToChar(encoded.n69)
    n70 = asciiToChar(encoded.n70)

    def f69():
        
        if random.randint(0,1) == 1:
            if user['name'] == '':
                print(f"\n{x.YELLOW}>> {x.VIOLETBG}{c.WHITE}{decoded.n69}{c.END}")
            else:
                print(f"\n{x.YELLOW}>>{x.GREEN} {user['name']}{c.END}, {x.VIOLETBG}{c.WHITE}{decoded.n69}{c.END}")
        else:
            if user['name'] == '':
                print(f"\n{x.YELLOW}>> {x.VIOLETBG}{c.WHITE}{decoded.n70}{c.END}")
            else:
                print(f"\n{x.YELLOW}>>{x.GREEN} {user['name']}{c.END}, {x.VIOLETBG}{c.WHITE}{decoded.n70}{c.END}")
        sleep(0.2)
        clear()

    def foo(force=False):
        if True or force:
            pass



#================================================================================================================================#
#================================================================================================================================#
#================================================================================================================================#

###########################
# Defining app menus etc. #
###########################
def msp_menu():
    
    global window
    window = "msp_menu()"

    def stats_reset():
        if confirm(f"{x.YELLOW}>>{x.VIOLET} Are you sure? {c.END}"):
            msp_reset()
            clear()
            print(f"{x.GREEN}>>{x.GRAY} All done, good as new. {c.END}")
def rnd_menu():

    global window
    window = "rnd_menu()"
    
    def stats_reset():
        if confirm(f"{x.YELLOW}>>{x.VIOLET} Are you sure? {c.END}"):
            rnd_reset()
            clear()
            print(f"{x.GREEN}>>{x.GRAY} All done, good as new. {c.END}")
            
    def stats_menu():
        print(f"\n{x.YELLOW}>>>{x.VIOLET} Randomeur Statistics:\n{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Total {rnd.headsStyle}{c.END}: {x.GRAY}{apps['rnd']['heads']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Total {rnd.tailsStyle}{c.END}: {x.GRAY}{apps['rnd']['tails']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Total {rnd.flipsStyle}{c.END}: {x.GRAY}{apps['rnd']['flips']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Total {rnd.tieStyle}{x.RED}s{c.END}:  {x.GRAY}{apps['rnd']['ties']}{c.END}")
        print("")
        print(f" {x.YELLOW}-{c.END} " + f"Last {rnd.headsStyle}{c.END}:  {x.GRAY}{apps['rnd']['last-heads']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Last {rnd.tailsStyle}{c.END}:  {x.GRAY}{apps['rnd']['last-tails']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Last {rnd.flipsStyle}{c.END}:  {x.GRAY}{apps['rnd']['last-flips']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Last Winner{c.END}: {x.GRAY}{apps['rnd']['last-winner']}{c.END}")
        enterContinue()
    
    print(f"\n{x.YELLOW}>>>{x.VIOLET} Welcome to Randomeur!")
    output.note(1)
    print(f"1: {x.GRAY}Coin Flipeur{c.END}")
    print(f"2: {x.GRAY}Game Stats{c.END}")
    print(f"9: {x.GRAY}Reset RND Statistics{c.END}")
    print(f"0: {x.GRAY}Home{c.END}")

    choice = intake.prompt()
    choice = choice_check(choice)
    
    if choice == "1" or choice.casefold() in ("flipeur", "coin flipeur", "coin"):
        clear()
        rnd.flipeur()
        
        apps['rnd']['heads']    += rnd.heads
        apps['rnd']['tails']    += rnd.tails
        apps['rnd']['flips']    += rnd.flips
        if rnd.heads == rnd.tails:
            apps['rnd']['ties'] += 1
        games_update()
        
        apps['rnd']['last-heads']       = rnd.heads  
        apps['rnd']['last-tails']       = rnd.tails
        apps['rnd']['last-flips']       = rnd.flips
        games_update()
        
        apps['rnd']['last-winner']      = rnd.winner
        games_update()
        
        woosh_back()
    elif choice == "2" or choice.casefold() == "stats":
        clear()
        stats_menu()
        rnd_menu()
    elif choice == "9" or choice.casefold() == "reset":
        clear()
        stats_reset()
        rnd_menu()
    elif choice == "0":
        clear()
        main_menu()
    else:
        clear()
        last_check(choice)

def rps_menu():

    global window
    window = "rps_menu()"
    
    def whosBest():
        
        wins = [
            apps['rps']['cpu']['wins'], apps['rps']['p1']['wins'], apps['rps']['p2']['wins']
        ]
        name = [   
            rps.cpu['name'], rps.p1['name'], rps.p2['name']
        ]
        
        best = max(wins)
        bestIndex = wins.index(best)
        
        wins.remove(best)
        best2 = max(wins)
        
        if best == best2:
            return '—'
        
        #if len(set(wins)) < len(wins):
        #    return '—'
        
        return name[bestIndex]
    
    def stats_menu():
        print(f"\n{x.YELLOW}>>>{x.VIOLET} RockPaperScissors Statistics:\n{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"{rps.p1['name']} Wins        : {x.GRAY}{apps['rps']['p1']['wins']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"{rps.p1['name']} Last Choice : {x.GRAY}{apps['rps']['p1']['last-choice']}{c.END}")
        print("")
        print(f" {x.YELLOW}-{c.END} " + f"{rps.p2['name']} Wins        : {x.GRAY}{apps['rps']['p2']['wins']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"{rps.p2['name']} Last Choice : {x.GRAY}{apps['rps']['p2']['last-choice']}{c.END}")
        print("")
        print(f" {x.YELLOW}-{c.END} " + f"{rps.cpu['name']} Wins        : {x.GRAY}{apps['rps']['cpu']['wins']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"{rps.cpu['name']} Last Choice : {x.GRAY}{apps['rps']['cpu']['last-choice']}{c.END}")
        print("")
        print(f" {x.YELLOW}-{c.END} " + f"Ties : {x.GRAY}{apps['rps']['ties']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Best : {x.GRAY}{whosBest()}{c.END}")
        enterContinue()

    def stats_reset():
        if confirm(f"{x.YELLOW}>>{x.VIOLET} Are you sure? {c.END}"):
            rps_reset()
            clear()
            print(f"{x.GREEN}>>{x.GRAY} All done, good as new. {c.END}")
            
            
    print(f"\n{x.YELLOW}>>>{x.VIOLET} Welcome to RockPaperScissors!")
    output.note(1)
    print(f"1: {x.GRAY}Solo{c.END}")
    print(f"2: {x.GRAY}Duo{c.END}")
    print(f"3: {x.GRAY}Game Stats{c.END}")
    print(f"9: {x.GRAY}Reset RPS Statistics{c.END}")
    print(f"0: {x.GRAY}Home{c.END}")

    choice = intake.prompt()
    choice = choice_check(choice)

    if choice == "1" or choice.casefold() == "solo":
        rps.soloMode()

        pN = rps.pN
        p1 = rps.p1
        cpu = rps.cpu
        winner = rps.winner
        
        apps['rps']['p1']['last-choice']  = p1['input']
        apps['rps']['cpu']['last-choice'] = cpu['input']
        apps['rps']['last-winner']        = winner['name']
        games_update()

        if winner == p1:
            apps['rps']['p1']['wins'] += 1
        if winner == cpu:
            apps['rps']['cpu']['wins'] += 1
        if winner == pN:
            apps['rps']['ties'] += 1
        games_update()

        rps_menu()
        
    elif choice == "2" or choice.casefold() == "duo":
        rps.duoMode()
        
        pN = rps.pN
        p1 = rps.p1
        p2 = rps.p2
        winner = rps.winner
        
        apps['rps']['p1']['last-choice'] = p1['input']
        apps['rps']['p2']['last-choice'] = p2['input']
        apps['rps']['last-winner']       = winner['name']
        games_update()
    
        if winner == p1:
            apps['rps']['p1']['wins'] += 1
        if winner == p2:
            apps['rps']['p2']['wins'] += 1
        if winner == pN:
            apps['rps']['ties'] += 1
        games_update()

        rps_menu()
        
        
    elif choice == "3" or choice.casefold() == "stats":
        clear()
        stats_menu()
        rps_menu()
    elif choice == "9" or choice.casefold() == "reset":
        clear()
        stats_reset()
        rps_menu()
    elif choice == "0":
        clear()
        main_menu()
    else:
        clear()
        last_check(choice)

def ttt_menu():

    global window
    window = "ttt_menu()"

    def stats_menu():
        print(f"\n{x.YELLOW}>>>{x.VIOLET} TicTacToe Statistics:\n{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"X Wins     : {x.GRAY}{apps['ttt']['x-wins']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"O Wins     : {x.GRAY}{apps['ttt']['o-wins']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Ties       : {x.GRAY}{apps['ttt']['ties']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Last Winner: {x.GRAY}{apps['ttt']['last-winner']}{c.END}")
        print(f" {x.YELLOW}-{c.END} " + f"Last Board :-\n")
        print(ttt.displayBoard(apps['ttt']['last-board'], True, left=f' {x.YELLOW}-{c.END} '))
        enterContinue()
    def stats_reset():
        if confirm(f"{x.YELLOW}>>{x.VIOLET} Are you sure? {c.END}"):
            ttt_reset()
            clear()
            print(f"{x.GREEN}>>{x.GRAY} All done, good as new. {c.END}")
            ttt_menu()
        else:
            clear()
            print(f"{x.RED}>>{x.GRAY} Okay then.{c.END}")
            ttt_menu()

        
    print(f"\n{x.YELLOW}>>>{x.VIOLET} Welcome to TicTacToe!")
    output.note(1)
    print(f"1: {x.GRAY}Start Game{c.END}")
    print(f"2: {x.GRAY}Game Stats{c.END}")
    print(f"9: {x.GRAY}Reset TTT Statistics{c.END}")
    print(f"0: {x.GRAY}Home{c.END}")
    
    choice = intake.prompt()
    choice = choice_check(choice)

    if choice == "1" or choice.casefold() == "start":
        result = ttt.ttt_2p_start()

        winner = result[0]
        board = result[1]

        apps['ttt']['last-winner'] = winner
        apps['ttt']['last-board'] = board
        games_update()

        if winner == ttt.s.x:
            apps['ttt']['x-wins'] = int(apps['ttt']['x-wins']) + 1
        if winner == ttt.s.o:
            apps['ttt']['o-wins'] = int(apps['ttt']['o-wins']) + 1
        if winner == ttt.s.n:
            apps['ttt']['ties'] = int(apps['ttt']['ties']) + 1
        games_update()

        ttt_menu()

    elif choice == "2" or choice.casefold() == "stats":
        clear()
        stats_menu()
        ttt_menu()
    elif choice == "9" or choice.casefold() == "reset":
        clear()
        stats_reset()
        ttt_menu()
    elif choice == "0":
        clear()
        main_menu()
    else:
        clear()
        last_check(choice)


def help_menu():
    print(f"\n{x.YELLOW}>>>{x.VIOLET} Commands: {c.END}")
    print(f" {x.YELLOW}-{c.END} {settings['prefix']}help: {x.GRAY}Shows this menu.{c.END}")
    print(f" {x.YELLOW}-{c.END} {settings['prefix']}home: {x.GRAY}Returns you to home page.{c.END}")
    print(f" {x.YELLOW}-{c.END} {settings['prefix']}exit: {x.GRAY}To safely exit the app.{c.END}")
    print(f" {x.YELLOW}-{c.END} {settings['prefix']}dev1: {x.GRAY}Enters eval() mode. {x.RED}{c.DIM}(dev-only){c.END}")
    print(f" {x.YELLOW}-{c.END} {settings['prefix']}dev2: {x.GRAY}Enters exec() mode. {x.RED}{c.DIM}(dev-only){c.END}")

    print(f"\n{x.YELLOW}>>>{x.VIOLET} Placeholders: {c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['nl']}: " + f"           {x.GRAY}Makes a lovely line separator, not useful.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['br']}: " + f"           {x.GRAY}Makes a new line, useful in repeat, I guess.{c.END}")
    print("")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['e']}: " + f"            {x.GRAY}Returns Euler's number's value.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['g']}: " + f"            {x.GRAY}Returns gravitational acceleration constant's value.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['pi']}: " + f"           {x.GRAY}Returns pi's value.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['tau']}: " + f"          {x.GRAY}Returns tau's value.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['phi']}: " + f"          {x.GRAY}Returns the golden ratio's value.{c.END}")
    print("")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['name']}: " + f"         {x.GRAY}Returns your name.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['age']}: " + f"          {x.GRAY}Returns your age.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['prefix']}: " + f"       {x.GRAY}Returns set prefix{c.END}")
    print("")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastTTTWinner']}: " + f"{x.GRAY}Returns the last TTT winner.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastTTTBoard']}: " + f" {x.GRAY}Returns the last TTT board.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['xWins']}: " + f"        {x.GRAY}Returns how many times x won.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['oWins']}: " + f"        {x.GRAY}Returns how many times o won.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['tttTies']}: " + f"      {x.GRAY}Returns how many TTT ties happened.{c.END}")
    print("")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['p1Last']}: " + f"       {x.GRAY}Returns {rps.p1['name']}{x.GRAY} last move.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['p2Last']}: " + f"       {x.GRAY}Returns {rps.p2['name']}{x.GRAY} last move.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['cpuLast']}: " + f"      {x.GRAY}Returns {rps.cpu['name']}{x.GRAY} last move.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['p1Wins']}: " + f"       {x.GRAY}Returns how many times {rps.p1['name']}{x.GRAY} won.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['p2Wins']}: " + f"       {x.GRAY}Returns how many times {rps.p2['name']}{x.GRAY} won.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['cpuWins']}: " + f"      {x.GRAY}Returns how many times {rps.cpu['name']}{x.GRAY} won.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['rpsTies']}: " + f"      {x.GRAY}Returns how many times RPS ties happened.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastRPSWinner']}: " + f"{x.GRAY}Returns the last RPS winner.{c.END}")
    print("")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['heads']}: " + f"        {x.GRAY}Returns the total amount of {rnd.headsStyle}{x.GRAY}.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['tails']}: " + f"        {x.GRAY}Returns the total amount of {rnd.tailsStyle}{x.GRAY}.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['rndTies']}: " + f"      {x.GRAY}Returns the total amount of RND {rnd.tieStyle}{x.RED}s{x.GRAY}.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['flips']}: " + f"        {x.GRAY}Returns the total amount of RND {rnd.flipsStyle}{x.GRAY}.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastHeads']}: " + f"    {x.GRAY}Returns the last {rnd.headsStyle}{x.GRAY} count.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastTails']}: " + f"    {x.GRAY}Returns the last {rnd.tailsStyle}{x.GRAY} count.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastFlips']}: " + f"    {x.GRAY}Returns the last {rnd.flipsStyle}{x.GRAY} count.{c.END}")
    print(f" {x.YELLOW}-{c.END} " + f"{placeholders['lastRNDWinner']}: " + f"{x.GRAY}Returns the last RND winner.{c.END}")

    enterContinue()

def options_menu():

    global window
    window = "options_menu()"

    def name_change(name):
        user['name'] = str(name)
        try:
            user_update()
        except:
            clear()
            print(f"{x.RED}>>{x.GRAY} Something went wrong. {c.END}")
        else:
            user_update()
            clear()
            print(f"{x.GREEN}>>{x.GRAY} Changes saved. {c.END}")

    def age_change(age):
        age_old = user['age']
        try:
            user['age'] = int(age)
        except:
            clear()
            print(f"{x.RED}>>{x.GRAY} Please input numbers only. {c.END}")
        else:
            if (user['age'] >= 100 or user['age'] < 0) and not (is_admin()):
                clear()
                print(f"{x.RED}>>{x.GRAY} How tf can you be {user['age']} years-old? {c.END}")
                print(f"{x.RED}>>{x.GRAY} I'll return it to {age_old}. {c.END}")
                user['age'] = age_old
                return
            try:
                user_update()
            except:
                clear()
                print(f"{x.RED}>>{x.GRAY} Something went wrong. {c.END}")
            else:
                user_update()
                clear()
                if user['age'] == 69:
                    print(f"{x.GREEN}>>{x.GRAY} Nice. {c.END}")
                else:
                    print(f"{x.GREEN}>>{x.GRAY} Changes saved. {c.END}")

    def prefix_change(thing):
        clear()
        settings['prefix'] = thing
        settings_update()


    print(f"\n{x.YELLOW}>>>{x.VIOLET} Options: {c.END}")
    output.note(1)
    print(f"1: {x.GRAY}Name: {x.LETTUCE}{user['name'] if user['name'] != '' else None}{c.END}")
    print(f"2: {x.GRAY}Age: {x.LETTUCE}{user['age']}{c.END}")
    print(f"3: {x.GRAY}Prefix: {x.LETTUCE}{settings['prefix']}{c.END}")
    print(f"8: {x.GRAY}Rest Games' Stats{c.END}")
    print(f"9: {x.GRAY}Rest Application{c.END}")
    print(f"0: {x.GRAY}Home{c.END}")

    choice = intake.prompt()
    choice = choice_check(choice)

    if choice == "1" or choice.casefold() == "name":

        clear()
        print(f"\n{x.YELLOW}>>>{x.VIOLET} What do you wanna be called? {c.END}")
        output.note(1)
        print(f"!!: {x.GRAY}Current is {x.GREEN}{user['name'] if user['name'] != '' else None}{c.END}")

        choice = intake.prompt()
        choice = choice_check(choice)

        name_change(choice)

        options_menu()

    elif choice == "2" or choice.casefold() == "age":

        clear()
        print(f"\n{x.YELLOW}>>>{x.VIOLET} How old are you? {c.END}")
        output.note(1)
        print(f"!!: {x.GRAY}Current is {x.GREEN}{user['age']}{c.END}")

        choice = intake.prompt()
        choice = choice_check(choice)

        age_change(choice)

        options_menu()
    elif choice == "3" or choice.casefold() == "prefix":

        clear()
        print(f"\n{x.YELLOW}>>>{x.VIOLET} Set prefix to what? {c.END}")
        output.note(1)
        print(f"!!: {x.GRAY}Current is {x.GREEN}{settings['prefix']}{c.END}")
        
        choice = intake.prompt()
        choice = choice_check(choice)
        
        prefix_change(choice)

        options_menu()
    elif choice == "8" or choice.casefold() == "reset stats":
        
        clear()
        print(f"\n{x.YELLOW}>>>{x.VIOLET} Continuing would mean you want to reset statistics to default.{c.END}")
        if confirm(f"{x.YELLOW}>>{x.VIOLET} Are you sure? {c.END}"):
            print(f"\n{x.YELLOW}>>{x.VIOLET} Please type {x.GRAY}{c.ITALIC}\"{settings['prefix']}reset\"{c.END}{x.VIOLET} to further confirm.{c.END}")

            choice = intake.prompt()
            choice = choice_check(choice)

            if choice == f"{settings['prefix']}reset":
                games_reset()
                clear()
                print(f"{x.GREEN}>>{x.GRAY} All done, good as new. {c.END}")
                main_menu()
            else:
                clear()
                print(f"{x.RED}>>{x.GRAY} I'll take that as a \"no\".{c.END}")
                options_menu()
        else:
            clear()
            print(f"{x.RED}>>{x.GRAY} Ready when you're sure.{c.END}")
            options_menu()

    elif choice == "9" or choice.casefold() == "reset all" or choice.casefold() == "reset app" or choice.casefold() == "reset application" :

        clear()
        print(f"\n{x.YELLOW}>>>{x.VIOLET} Continuing would mean you want to reset everything to default values.{c.END}")
        if confirm(f"{x.YELLOW}>>{x.VIOLET} Are you sure? {c.END}"):
            print(f"\n{x.YELLOW}>>{x.VIOLET} Please type {x.GRAY}{c.ITALIC}\"{settings['prefix']}reset\"{c.END}{x.VIOLET} to further confirm.{c.END}")

            choice = intake.prompt()
            choice = choice_check(choice)

            if choice == f"{settings['prefix']}reset":
                all_reset()
                clear()
                print(f"{x.GREEN}>>{x.GRAY} All done, good as new. {c.END}")
                main_menu()
            else:
                clear()
                print(f"{x.RED}>>{x.GRAY} I'll take that as a \"no\".{c.END}")
                options_menu()
        else:
            clear()
            print(f"{x.RED}>>{x.GRAY} Ready when you're sure.{c.END}")
            options_menu()
    elif choice == "0":
        clear()
        main_menu()
    else:
        clear()
        last_check(choice)

    
def repeat():

    print(f"\n{x.YELLOW}>>>{x.VIOLET} What do you want me to repeat?{c.END}")
    output.note(1)

    choice = intake.prompt()
    choice = choice_check(choice)

    if choice.casefold() == "idk" or choice.casefold() == "not sure":
        clear()
        print(f"{x.RED}>>{x.GRAY} Well, Why even ask?!{c.END}")
    elif choice.casefold() == "fuck you":
        clear()
        print(f"{x.RED}>>{x.GRAY} No, you ↪.{c.END}")
    elif choice == "69" or ("sex" in choice.casefold()):
        decoded.f69()
        clear()
        print(f"{x.YELLOW}>>{x.VIOLET} {choice}{c.END}")
    else:
        clear()
        print(f"{x.YELLOW}>>{x.VIOLET} {choice}{c.END}")

def do_math():
    allowed = "0123456789+-*/.,() "
    print(f"\n{x.YELLOW}>>>{x.VIOLET} Oh wanna do some math'ing?{c.END}")
    output.note(1)

    choice = intake.prompt()
    choice = choice_check(choice)

    if goThro(choice,allowed):
        try:
            choice = eval(choice)
        except:
            clear()
            print(f"{x.RED}>>{x.GRAY} That's not really math...{c.END}")
        else:
            if choice == 69:
                decoded.f69()
            clear()
            print(f"{x.YELLOW}>>{x.VIOLET}" , choice, c.END)
    else:
        clear()
        print(f"{x.RED}>>{x.GRAY} That's not really math...{c.END}")

def app_info():
    with open('./res/extras/logo.txt', 'r') as file:
        logo = file.read().split("-sex-is-cool-")
        logo_art = logo[0]
        logo_text = logo[1]
        logo_motto = logo[2]

    print(
        x.LETTUCE + logo_art + c.END
        +
        x.VIOLET + logo_text + c.END
        +
        c.DIM
        +
        x.GRAY + logo_motto + c.END
        )
    print(f"\n{x.YELLOW}>>> {x.VIOLET}{c.BOLD}SPAIME²{c.END}")
    print(f"Version: {x.GRAY}0.1.3{c.END}")
    print(f"Author : {x.GRAY}Fastre{c.END}")
    print(f"Github : {x.GRAY}{c.URL}{c.ITALIC}https://github.com/IamFastre{c.END}")
    print(f"Discord: {x.GRAY}{c.URL}{c.ITALIC}https://discord.gg/kkzmxkG{c.END}")
    print(f"Note   : {x.GRAY}There was never a SPAIME¹{c.END}")
    choice = enterContinue()
    if choice.casefold() in admin:
        print(f"{x.GREEN}>> {x.GRAY}Yes, {x.RED}♥{x.GRAY}.{c.END}")
    main_menu()


def refresh():
    print(f"{x.YELLOW}>>{x.GRAY} Refreshing.{c.END}")

    settings_update()
    user_update()

    clear()
    print(f"{x.YELLOW}>>{x.GRAY} Done!{c.END}")
    sleep(0.5)
    clear()
    run_app()

def exit_app(sayBye=True):
    global user
    global exited
    exited = True
    
    if sayBye:
        print(f"{x.YELLOW}>>{x.GRAY} Okie!{c.END}")
        sleep(0.5)
        
    
        clear()
        if user['name'] == '':
            print(f"{x.YELLOW}>>{x.VIOLET} Bye Bye!{c.END}")
        else:
            print(f"{x.YELLOW}>>{x.VIOLET} Bye Bye, {x.GREEN}{user['name']}{x.VIOLET}!{c.END}")
        
    pause()
    
    if os.path.exists('./res/__pycache__'):
        shutil.rmtree('./res/__pycache__')
        
    if os.path.exists('./apps/__pycache__'):
        shutil.rmtree('./apps/__pycache__')
        
    if os.path.exists('./.exec/__pycache__'):
        shutil.rmtree('./.exec/__pycache__')
        
    if os.path.exists('./__pycache__'):
        shutil.rmtree('./__pycache__')
        
    #keyboard.press_and_release('ctrl+c')
    sys.exit(0)

def main_menu():

    global window
    window = "main_menu()"
    
    bricks = "{}"

    if user['name'] == '':
        print(f"\n{x.YELLOW}>>>{x.VIOLET}{c.BOLD} Hey, Whatcha wanna do?!{c.END}")
    else:
        print(f"\n{x.YELLOW}>>>{x.VIOLET}{c.BOLD} Hey {x.GREEN}{user['name']}{x.VIOLET}, Whatcha wanna do?!{c.END}")
    output.note(1)
    print(f"1: {x.GRAY}[{x.LETTUCE}↑↓{x.GRAY}]"      + f" Repeat{c.END}")
    print(f"2: {x.GRAY}[{x.LETTUCE}π*{x.GRAY}]"      + f" Basic Math{c.END}")
    print(f"3: {x.GRAY}[{ttt.s.x}{ttt.s.o}{x.GRAY}]" + f" TicTacToe{c.END}")
    print(f"4: {x.GRAY}[{x.LETTUCE}$${x.GRAY}]"      + f" RockPaperScissors{c.END}")
    print(f"5: {x.GRAY}[{x.LETTUCE}☘{x.YELLOW}%{x.GRAY}]"      + f" Randomeur{c.END}")
    print(f"7: {x.GRAY}[{x.ORANGE}{bricks}{x.GRAY}]"        + f" Options{c.END}")
    print(f"8: {x.GRAY}[{x.VIOLET}>>{x.GRAY}]"       + f" Credits{c.END}")
    print(f"9: {x.GRAY}[{x.RED}x{x.GREEN}✓{x.GRAY}]" + f" Refresh{c.END}")
    print(f"0: {x.GRAY}[{x.RED}xx{x.GRAY}]"          + f" Exit{c.END}")

    choice = intake.prompt()
    choice = choice_check(choice)

    if choice == "1" or choice.casefold() == "repeat":
        clear()
        repeat()
        main_menu()
    elif choice == "2" or choice.casefold() == "basic math":
        clear()
        do_math()
        main_menu()
    elif choice == "3" or choice.casefold() in ("ttt", "tictactoe"):
        clear()
        ttt_menu()
    elif choice == "4" or choice.casefold() in ("rps", "rockpaperscissors"):
        clear()
        rps_menu()
    elif choice == "5" or choice.casefold() in ("rnd", "randomeur"):
        clear()
        rnd_menu()
    elif choice == "7" or choice.casefold() in ("options", "option"):
        clear()
        options_menu()
    elif choice == "8" or choice.casefold() in ("credits", "info"):
        clear()
        app_info()
    elif choice == "9" or choice.casefold() == "refresh" or choice.casefold() == "rerun":
        refresh()
    elif choice == "0" or choice.casefold() == "end" or choice.casefold() == "exit":
        exit_app()
    else:
        clear()
        last_check(choice)



#================================================================================================================================#

#############################
# Actually running the app. #
#############################

def run_app():
    clear()

    if settings['first-time']:
            settings['first-time'] = False
            settings_update()
            
            app_info()
    else:
        main_menu()

    if not exited:
        print(f"{x.RED}>>{x.GRAY} Something wrong happened.{c.END}")
        print(f"{x.RED}>>{x.GRAY} Gonna rerun.{c.END}")
        pause()
        run_app()

if __name__ == '__main__':
    run_app()