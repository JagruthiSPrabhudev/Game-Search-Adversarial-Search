# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:14:54 2018

@author: Jagruthi Prabhudev
"""
import sys
from copy import deepcopy
import math
PATH = []
MOVESET = []
move_dict = []
Explored =[]
move_historyp = []
class Board(object):

    BLANK = 0
    NOT_MOVED = None

    def __init__(self, player_1, player_2, width, height):
        self.width = width
        self.height = height
        self.move_count = 0
        self.__player_1__ = player_1
        self.__player_2__ = player_2
        self.__active_player__ = player_1
        self.__inactive_player__ = player_2

    @property
    def active_player(self):

         return self.__active_player__


    @property
    def inactive_player(self):

        return self.__inactive_player__

    def get_opponent(self, player):

        if player == self.__active_player__:
            return self.__inactive_player__
        elif player == self.__inactive_player__:
            return self.__active_player__
        raise RuntimeError("`player` must be an object registered as a player in the current game.")



    def forecast_move(self, move,player = None):

        new_board = move_history
        new_board = board.apply_move(move,move_history,move_R1,move_R2,player = None)
        return new_board,move

    def get_legal_moves(self,move_history):
        return self.__get_moves__(move_history)

    def apply_move(self, move,move_history,move_R1,move_R2,player = None):

        nextplayer = player
        if player == None:
            nextplayer = self.__active_player__

        if move not in move_history:
                 move_history.append(move)

        if move_history[0] != "*":
                if nextplayer  == "R1":
                    if  move not in move_R1 and move not in move_R2:
                        move_R1.append(move)

                else:

                    if nextplayer == "R2":
                        if  move not in move_R2 and move not in move_R1:
                            move_R2.append(move)

        self.__active_player__, self.__inactive_player__ = self.__inactive_player__, self.__active_player__
        self.move_count += 1
        return move_history,self.__inactive_player__

    def apply_moveStatic(self, move,move_history,move_R1,move_R2,player = None):

        if MAX_DEPTH%2 == 0:
             nextplayer = player
        else:
            nextplayer = self.__active_player__

        if move not in move_history:
                 move_history.append(move)

        if move_history[0] != "*":
                if nextplayer  == "R1":
                    if  move not in move_R1 and move not in move_R2:
                        move_R1.append(move)

                else:

                    if nextplayer == "R2":
                        if  move not in move_R2 and move not in move_R1:
                            move_R2.append(move)

        #self.__active_player__, self.__inactive_player__ = self.__inactive_player__, self.__active_player__
        self.move_count += 1
        return move_history,self.__active_player__

    def check_if_adj_area(self,move,move_mat,ad):
        isAdj = True
        if move in move_mat:
            move_mat.remove(move)
        for i in range(len(move_mat)):
            if move_mat[i] in ad.keys():
                adj = ad.get(move_mat[i])
                adj = adj.replace("[", "")
                adj = adj.replace("]", "")
                adj = adj.split(",")
                adj = list(adj)
                index = board.get_indexMove(move)
                if adj[index] == "1":
                    return True
                else:
                   isAdj = False
        return isAdj

    def get_indexMove(self,move):
        val = value.keys()
        val = list(val)
        val.sort()
        for i in range(0,len(val)):
            if val[i] == move:
                return i


    def __get_moves__(self,move_history):
        """
        Generate the list of possible moves
        """
        valid_moves = []
        allPossiblemoves = value.keys()
        allPossiblemoves = list(allPossiblemoves)
        allPossiblemoves.sort()
        if move_history[0] == "*":
            return allPossiblemoves

        if self.move_count == 1:
            valid_moves = [move1 for move1 in allPossiblemoves if move1 not in move_history]
        else:
            if self.__active_player__ == "R1":
                for move1 in allPossiblemoves:
                    if move1 not in move_history:
                        if self.check_if_adj_area(move1,move_R1,adjM):
                            valid_moves.append(move1)
            else:
                for move1 in allPossiblemoves:
                    if move1 not in move_history:
                        if self.check_if_adj_area(move1,move_R2,adjM):
                            valid_moves.append(move1)

        return valid_moves


    def __get_movesInactive__(self,move_history,playerEnd):
            """
            Generate the list of possible moves
            """
            valid_moves = []
            allPossiblemoves = value.keys()
            allPossiblemoves = list(allPossiblemoves)
            allPossiblemoves.sort()
            if  move_history[0] == "*":
                return allPossiblemoves

            if self.move_count == 1:
                valid_moves = [move1 for move1 in allPossiblemoves if move1 not in move_history]
            else:
                if playerEnd == "R1":
                    playerEnd = "R2"
                    for move1 in allPossiblemoves:
                        if move1 not in move_history :
                            if self.check_if_adj_area(move1,move_R1,adjM):
                                valid_moves.append(move1)
                elif playerEnd == "R2":
                    playerEnd = "R1"
                    for move1 in allPossiblemoves:
                        if move1 not in move_history :
                            if self.check_if_adj_area(move1,move_R2,adjM):
                                valid_moves.append(move1)
            return valid_moves,playerEnd


class CustomPlayer:

    def custom_score(self,move,player):
        score = 0
        selectedArea = move
        if player == "R1":
            for i in range(len(move_R1)):
                if move_R1[i] in value.keys():
                    score = score + int(value.get(move_R1[i]))
        elif player == "R2":
            for i in range(len(move_R2)):
                if move_R2[i] in value.keys():
                    score = score + int(value.get(move_R2[i]))
        return score,player

    def __init__(self, search_depth, score_fn=custom_score):
        self.search_depth = search_depth
        self.score = score_fn


    def alpha_beta_search(self, move,sdepth):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity
        #legal_moves = board.get_legal_moves(move_history)
        #for state in move_history:
        sdepth = len(move_history) -1
        best_val,b_move = self.max_value(move, best_val, beta,sdepth)
        return best_val,b_move

    def max_value(self, node, alpha, beta,sdepth):
        nextplayer = None
        s_score = -9999
        b_move = " "
        if self.isTerminal(node,sdepth):
            score,playerEnd = self.custom_score(node,board.__inactive_player__)
            PATH.append(score)
            #print(move_R1)
            if playerEnd == "R1":
                if score > s_score:
                    MOVESET.append(move_R1[len(gmove_history)-1])
                    #print(score,move_R1[len(gmove_history)-1])
            elif playerEnd == "R2":
                if score > s_score:
                    MOVESET.append(move_R2[len(gmove_history)-1])

            for i in range(len(move_history)):
                temp =[""]
                if len(move_history) > 1:
                    temp = move_history[:-1]
                legal_moves,playert = board.__get_movesInactive__(temp,playerEnd)
                playerEnd = playert
                if(len(legal_moves) >1) :
                   Explored.append(legal_moves[0])
                   if(len(legal_moves) == len(Explored) and len(temp) >1):
                       Explored.clear()
                       temp = temp[:-1]
                   move_history.clear()
                   for move in temp:
                      move_history.append(move)
                   break;
                else:
                    move_history.clear()
                    for move in temp:
                        move_history.append(move)
            #move_history.clear()
            move_R1.clear()
            move_R2.clear()
            sdepth = len(gmove_history)-1

            for move in move_history:
                if move == gmove_history[0] and MAX_DEPTH%2 == 0:
                    board.apply_moveStatic(move,move_history,move_R1,move_R2,board.__inactive_player__)
                else:
                    board.apply_move(move,move_history,move_R1,move_R2)
            if score > s_score:
                s_score = score
                b_move = node
            return s_score,b_move

        if self.isPassFunc(node):
                allPossiblemoves = value.keys()
                allPossiblemoves = list(allPossiblemoves)
                allPossiblemoves.sort()
                if board.__active_player__ == "R1":
                    for move in allPossiblemoves:
                        if move not in move_history:
                             if board.check_if_adj_area(move,move_R2,adjM):
                                move_R2.append(move)
                elif board.__active_player__ == "R2":
                    for move in allPossiblemoves:
                        if move not in move_history:
                             if board.check_if_adj_area(move,move_R1,adjM):
                                move_R1.append(move)

                score,playerEnd = self.custom_score(node,board.__active_player__)
                PATH.append(score)
                if score > s_score:
                    s_score = score
                    b_move = node
                return  s_score,b_move

        successors = board.get_legal_moves(move_history)
        for state in successors:
            board.forecast_move(state)
            value1,moveSt = self.max_value(state, alpha, beta,sdepth+1)
            if value1 > s_score:
                    s_score = value1
                    b_move = moveSt

        return s_score,b_move


    def isTerminal(self, node,sdepth):
        assert node is not None
        mov = board.get_legal_moves(move_history)
        allposs = board.get_legal_moves("*")
        if sdepth == MAX_DEPTH or (not mov and len(allposs) == len(move_history)):
            return True
        else:
            return False

    def isPassFunc(self, node):
        mov = board.get_legal_moves(move_history)
        allposs = board.get_legal_moves("*")
        if not mov and len(allposs) != len(move_history):
            return True,board.__active_player__



inputfile = open("input11.txt", "r")
day = inputfile.readline()
day = day.replace("\n", "")
#print(day)
player = inputfile.readline()
player = player.replace("\n", "")
#print(player)

rcl = inputfile.readline()
rcl = rcl.replace("\n", "")
rcl = rcl.replace("\r", "")
rcl = rcl.replace("(", "")
rcl = rcl.replace(")", "")
# rcl = rcl.replace(",","")

d = rcl.split(",")
value = {}
myiter = iter(range(0, len(d)))
for i in myiter:
    value[d[i]] = d[i+1]
    next(myiter, None)
#print("value",value)
player1 = "R1"
player2 = "R2"
# print(len(value))
adjM = {}
ad = {}
areaList = value.keys()
areaList = list(areaList)
areaList.sort()
#print(areaList)
for i in range(0, len(value)):
    adjList = inputfile.readline()
    adjList = adjList.replace("\n", "")
    adjList = adjList.replace("\r", "")
    # print(adjList)
    adjM[areaList[i]] = adjList
#print(adjM)

move_history = inputfile.readline()
move_history = move_history.replace("\n", "")
move_history = move_history.replace("\r", "")
move_history = move_history.split(",")
move_history = list(move_history)
#print(move_history)
depth = inputfile.readline()
depth = int(depth)
#print(depth)

#print(player1)
#print(player2)
move_R1 =[]
move_R2 = []

gmove_history = deepcopy(move_history);
gmove_R1 = move_R1
gmove_R2 = move_R2

MAX_DEPTH = depth
if move_history[0] != "*" and MAX_DEPTH%2 == 0:
    player1 = player
    if player1 == "R1":
     player2 = "R2"
    else:
     player2 = "R1"

elif move_history[0] == "*":
    if player == "R1":
     player1 = "R1"
     player2 = "R2"
    elif player == "R2":
     player1 = "R2"
     player2 = "R1"

players = [player1, player2]
board = Board(player1, player2, len(value), len(value))
nextmove = None

if move_history[0] != "*":
  for move in move_history:
        if not move == "PASS":
            board.forecast_move(move)
            nextmove= move
        elif move == "PASS" and len(move_history) >1:
           for move in move_history:
               if move != "PASS":
                   move_historyp.append(move)
           move_history.clear()
           move_history.append("PASS")
           move_history.append("1")


def get_heuristicUtility(moveHeuristic,movep = None):
    score = 0.0
    #print(value)
    Hdixt = {}
    if movep == None:
        for move in moveHeuristic:
         if move in value.keys():
             score = score + (float(1/len(value))*float(value.get(move)))
        for move in movesHeuristic:
         if move in value.keys():
             Hdixt[move] = (score + float(value.get(move)))/2
    else:
        for move in movep:
         if move in value.keys():
             score = score + (float(1/len(value))*float(value.get(move)))
        for move in movesHeuristic:
         if move in value.keys():
             Hdixt[move] = (score + float(value.get(move)))/2
    #print(Hdixt)
    return Hdixt

if day == "Yesterday":
    my_dict = {}
    movep = []
    if gmove_history[0] == "*":
        movesHeuristic = board.get_legal_moves(gmove_history)
        my_dict = get_heuristicUtility(movesHeuristic,None)
    else:
        movesHeuristic = board.get_legal_moves(move_history)
        moves = board.get_legal_moves("*")
        for movve in moves :
            movep.append(movve)
        my_dict = get_heuristicUtility(movesHeuristic,movep)

    final = max(my_dict.values())
    finals = []
    for k in my_dict.keys():
        if (my_dict[k]) == final:
                finals.append((k))
    print(finals[0])
    finallist = []
    out = open('output.txt', 'w')
    out.write(finals[0])
    out.write("\n")
    for move in movesHeuristic:
        finallist.append(math.ceil(my_dict.get(move)))
    print(finallist)
    for i in range(0,len(finallist)-1):
        out.write(str(finallist[i])+",")
    out.write(str(finallist[-1]))
    out.close()


else:
    customplayer = CustomPlayer(depth,players)
    valueS = -9999
    Bstate = ""
    if move_history[0] == "*":
            legal_moves = board.get_legal_moves(move_history)
            for state in legal_moves:
                move_history.clear()
                board.forecast_move(state)
                gmove_history = deepcopy(move_history)
                value1,moveSt = customplayer.alpha_beta_search(move_history, 0)
                if value1 > valueS:
                    valueS = value1
                    Bstate = moveSt
                move_history.clear()
            final = max(PATH)
            finals = []
            for k in value.keys():
                if int(value[k]) == final:
                    finals.append((k))
            print(finals[0])
            out = open('output.txt', 'w')
            out.write(finals[0])
            out.write("\n")
            for i in range(0,len(PATH)-1):
                out.write(str(PATH[i])+",")

            out.write(str(PATH[-1]))
            out.close()


    elif move_history[0] == "PASS" and  move_history[1] == "1":
         move_R2p = []
         move_R1p = []
         legal_moves = board.get_legal_moves(move_historyp[-1])
         if board.__active_player__ == "R1":
            for move in legal_moves:
                if move not in move_historyp:
                  move_R2p.append(move)
         elif board.__active_player__ == "R2":
              for move in legal_moves:
                  if move not in move_historyp:
                     move_R1p.append(move)
         score = []
         scoredixt = {}
         val = move_historyp[-1]

         if  board.__active_player__ == "R1":
            for i in range(len(move_R2p)):
                if move_R2p[i] in value.keys():
                    score.append(int(value.get(val)) + int(value.get(move_R2p[i])))
                    scoredixt[move_R2p[i]] = int(value.get(val)) + int(value.get(move_R2p[i]))

         elif board.__active_player__ == "R2":
            for i in range(len(move_R1p)):
                if move_R1p[i] in value.keys():
                    score.append(int(value.get(val)) + int(value.get(move_R1p[i])))
                    scoredixt[move_R1p[i]] = int(value.get(val)) + int(value.get(move_R1p[i]))

         final = max(PATH)
         finals = []
         for k in scoredixt.keys():
            if int(scoredixt[k]) == final:
                finals.append((k))
         print(finals[0])
         out = open('output.txt', 'w')
         out.write(finals[0])
         out.write("\n")
         for i in range(0,len(score)-1):
            out.write(str(score[i])+",")
         out.write(str(score[-1]))
         out.close()

    else:
        value1,move = customplayer.alpha_beta_search(move_history, 0)
        valueS,Bstate = value1,move
        #print(valueS)
        #print(Bstate)
        print(PATH)
        print(MOVESET)
        #print(len(PATH))
        final = max(PATH)
        finals = []
        for k in value.keys():
            if int(value[k]) == final:
                finals.append((k))
        print(finals[0])
        out = open('output.txt', 'w')
        out.write(finals[0])
        out.write("\n")
        for i in range(0,len(PATH)-1):
            out.write(str(PATH[i])+",")

        out.write(str(PATH[-1]))
        out.close()
