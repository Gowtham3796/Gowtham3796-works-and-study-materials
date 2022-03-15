import random

cards = {
  "A": 1,
  "2":2,
  "3":3,
  "4":4,
  "5":5,
  "6":6,
  "7":7,
  "8":8,
  "9":9,
  "10":10,
  "J":10,
  "Q":10,
  "K":10,
  "C":0,
}

shallweendthegame=False

while not shallweendthegame:

    playerlist={}
    const=5


    print("Welcome to the game of five cards..")
    nop=int(input("Enter the No of players: "))
    exs=int(input("Enter the Exit score: "))
    print("Enter the player names. Player 1 will get the open card first..")

    for n in range(1,nop+1):
        pname=input(f"Name of Player {n}: ")
        playerlist[pname]=0
        
    print("Let's start the game")

    endofthematch=False

    while not endofthematch:
        
        print(playerlist)

        print("Distributing the cards")

        playercards={}

        for player in playerlist:
            cardsnow=['_','_','_','_','_']
            for m in range(const):
                cardsnow[m]=random.choice(list(cards))
            
            playercards[player]=cardsnow
                
        joker=random.choice(list(cards))
        opencard=random.choice(list(cards))
        roundfinish=False

        while not roundfinish:
            
            
            for player in playercards:
                
                if not roundfinish:
                        
                    print(f"{player}'s turn")
                    print(f"Your cards are {playercards[player]}")
                    print(f"The joker is {joker}. Don't forget")
                    opt=input("Do you want to Declare Dick with your cards now? Enter 'yes' or 'no'")
                
                    if opt=="no":
                        
                        print(f"Your open card was {opencard}")
                    
                        cpil=False
                    
                        while not cpil:
                            lastcard=input("Enter the card you're throwing: ").upper()
                        
                            if lastcard in playercards[player]:
                                removed=False
                                while not removed:
                                    if lastcard in playercards[player]:
                                        playercards[player].remove(lastcard)
                                    else:
                                        removed=True
                                
                                if opencard==lastcard:
                                    print("You don't need to pick a new card")
                                    opencard=lastcard
                                
                                else:
                                    opt2=input("Do you want to pick the open card? Enter 'yes' or 'no'")
                                    if opt2=="yes":
                                        playercards[player].append(opencard)
                                    
                                    else:
                                        closedcard=random.choice(list(cards))
                                        playercards[player].append(closedcard)
                                    
                                    opencard=lastcard
                        
                                cpil=True
                            
                            else:
                                print(f"You'dont have that card. Don't cheat {player}")
                
                    else:
                        roundfinish=True
                        pcardrealvalue={}
                        lowest=60
                        
                        for plyer in playercards:
                            i=0
                            newcards=[0,0,0,0,0]
                            
                            for x in playercards[plyer]:
                                
                                if x==joker:
                                    newcards[i]= 0
                                    
                                else:   
                                    newcards[i]= cards[x]
                                    
                                i+=1
                            
                            pcardrealvalue[plyer]=newcards

                            if sum(pcardrealvalue[plyer])<lowest:
                               lowest=sum(pcardrealvalue[plyer])
                               lowestmember=plyer
                               
                        if lowestmember==player:
                            print("You won this round. Cheers!!!")
                            
                        else:
                            print(f"Not you. {lowestmember} won this round")
                            
                        pcardsum={}
                        
                        for pleyer in pcardrealvalue:
                            
                            if lowestmember==pleyer:
                                pcardsum[pleyer]=0
                                
                            else:    
                                pcardsum[pleyer]=sum(pcardrealvalue[pleyer])

                            print(f"{pleyer}'s score this round is {pcardsum[pleyer]}")
                            
                        dummyplayerlist={}
                        
                        z=0
                            
                        for plyr in playerlist:
                            
                            playerlist[plyr]+=pcardsum[plyr]
                            dummyplayerlist[plyr]=playerlist[plyr]
                            if z==0:
                                ocn=plyr
                                ocv=playerlist[plyr]
                            z+=1
                            
                        for plr in dummyplayerlist:  
                            
                            if playerlist[plr]<exs:
                                print(f"{plr}'s total score is {playerlist[plr]} and still in the game..")
                                
                            else:
                                print(f"{plr}'s total score is {playerlist[plr]} and out of the game..")
                                playerlist.pop(plr)
                        
                        if ocn in playerlist:
                            playerlist.pop(ocn)
                            playerlist[ocn]=ocv
                        
                        nopn=len(playerlist)
                        
                        if nopn>1:
                            print("Next Round...")
                            
                        elif nopn==1:
                            for lastplayer in playerlist:
                                print(f"{lastplayer} is the winner of the match..")
                                
                            endofthematch=True
                            
                            cwetg=input("Ready to restart the game?? Type 'yes' or 'no'")
                        
                            if cwetg=="no":
                                shallweendthegame=True
                            
                            
                                
                        else:
                            print("No one wins the match..")
                            endofthematch=True
                            
                            cwetg=input("Ready to restart the game?? Type 'yes' or 'no'")
                        
                            if cwetg=="no":
                                shallweendthegame=True
