import csv

with open('игроки Феклистов - игроки.csv') as file:
    ocenka_feklistov = [i.rstrip().split(',') for i in file.readlines()]


def atribs(a): #making a dict with all atributes of players and return player's stats_name and stats_value which was chosen
        players = {ocenka_feklistov[poisk_index(player_name)][0]:{ocenka_feklistov[0][i]:ocenka_feklistov[poisk_index(player_name)][i] for i in range(len(ocenka_feklistov[0]))}}
        keys_stats = ['скорость', 'удары','передачи','дриблинг','защита','физика']
        val_stats = [players[a][i] for i in keys_stats]
        print(keys_stats)
        print(val_stats)
        return keys_stats, val_stats


def poisk_index(a): # for searching player's index by name in list ocenka_feklistov
    for i in range(len(ocenka_feklistov)):
        for j in range(len(ocenka_feklistov[i])):
            if a == ocenka_feklistov[i][j] or a == ocenka_feklistov[i][j].lower():
                return i


player_name = (input())
poisk_index(player_name)
atribs(player_name)
