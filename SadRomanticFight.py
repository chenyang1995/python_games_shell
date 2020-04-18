import random

class Creature():
    def __init__(self,hp,name,attackPower,healPower = 0):
        self.hp = hp
        self.name = name
        self.attackPower = attackPower
        self.healPower = healPower

    def attack(self):
        attack_value = random.randint(0,self.attackPower)
        return attack_value

    def being_attacked(self, attack_value):
        self.hp = int(self.hp - attack_value)

    #Hannibal only
    def suckBlood(self):
        suck_value = random.randint(0,30)
        return suck_value

    def being_sucked(self, suck_value):
        self.hp = int(self.hp - suck_value)
    #Hannibal only

    #wizard only
    def heal(self):
        if random.random()>0.5:
            heal_value = random.randint(0, self.healPower)
        else:
            heal_value = 0
        return heal_value
    
    def being_healed(self, heal_value):
        self.hp = int(self.hp + heal_value)
    #wizard only

    def not_dead(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def show_status(self):
        print('{}\'s hp is {}.'.format(self.name,self.hp) )

#game setup
user = input("Hi! What's your name? ")

player = Creature(700, user,60)
wizard = Creature(100, "Wizard", 100, 70)

enemy1 = Creature(800, "Godzilla",50)
enemy2 = Creature(600, "Dracula",30)

#storytelling
print("------------------------------------------------------------------------------")
print("Hi {}!\nYou and the Wizard will fight against {} and {}. \nIf you protect the Wizard in one round, she will get less attacked while you get fully attacked, \notherwise one of you will get fully attacked. \nHowever, you may get healed through protecting her.".format(user,enemy1.name,enemy2.name))
print("Initial Status:")

#game
while enemy1.not_dead() or enemy2.not_dead():

    if not player.not_dead():
        break

    print("------------------------------------------------------------------------------")
    player.show_status()
    wizard.show_status()

    if enemy1.not_dead():
        enemy1.show_status()
    else:
        print("{} is dead.".format(enemy1.name))

    if enemy2.not_dead():
        enemy2.show_status()
    else:
        print("{} is dead.".format(enemy2.name))
        
    player_attack_value = player.attack()
    wizard_attack_value = wizard.attack()

    enemy1_attack_value = enemy1.attack()
    enemy2_attack_value = enemy2.attack()
    enemy2_suck_value = enemy2.suckBlood() 

    wizard_heal_value = wizard.heal()

    print("------------------------------------------------------------------------------") 
    print("------------------------------------------------------------------------------")  
    user_input = input ("Do you want to protect the Wizard in this round? (y/n) ")

    if user_input == "n":
        enemy1.being_attacked(player_attack_value)
        enemy2.being_attacked(player_attack_value)

        if wizard.not_dead():
            enemy1.being_attacked(wizard_attack_value)
            enemy2.being_attacked(wizard_attack_value)
        
        if random.random()<0.5:
            player.being_attacked(enemy1_attack_value)

            player.being_attacked(enemy2_attack_value)

            if random.random()<0.5:
                player.being_attacked(enemy2_suck_value)
                print("You got attacked and Hannibal sucked your blood! ")
            else:
                print("You got attacked! ")


        else:    
            wizard.being_attacked(enemy1_attack_value)
            wizard.being_attacked(enemy2_attack_value)

            if random.random()<0.5:
                wizard.being_attacked(enemy2_suck_value)
                print("The Wizard got attacked and Hannibal sucked her blood!!")
            else:
                print("The Wizard got attacked!")


    if user_input == "y":

        if wizard.not_dead():
            enemy1.being_attacked(wizard_attack_value)
            enemy2.being_attacked(wizard_attack_value)

        player.being_attacked(enemy1_attack_value)
        player.being_attacked(enemy2_attack_value)
        player.being_attacked(enemy2_suck_value)

        luckpercentage = int(random.random()*30)
        wizard.being_attacked(enemy1_attack_value*luckpercentage/100)
        wizard.being_attacked(enemy2_attack_value*luckpercentage/100)
        wizard.being_attacked(enemy2_suck_value*luckpercentage/100)

        player.being_healed(wizard_heal_value)

        print("You got attacked!")
        if wizard_heal_value > 0:
            print("You got healed by {}!".format(wizard_heal_value))

        if luckpercentage <= 0:
            print("The Wizard didn't get attacked!")
        else:
            print("The Wizard only got %.0f%% attacked!" %luckpercentage)

#game end
if player.not_dead():
    if player.not_dead() and wizard.not_dead():
        print("Congratulations! You and the Wizard won!")
    else:
        print("The monsters were beaten. But your partner died and her dead body is damaged.(degree {})".format(-wizard.hp))
else:
    print("You lost!!")


