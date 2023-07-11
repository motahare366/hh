from brownie import Reputationcalculation, config, network
from scripts.helpful_scripts import get_account
import matplotlib.pyplot as plt
import math

def deploy():
    account = get_account()
    reputation = Reputationcalculation.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "publish_source", False
        ),
    )
    result = []
    a=    Eus = input('Please Enter a: ')
    B=    Eus = input('Please Enter B: ')
    reputation.setaB(a,B)
    Eus = input('Enter Evaluation End user: ')
    txDirect=reputation.DirectReputation("0xdD870fA1b7C4700F2BD7f44238821C26f7392148","0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",Eus,{"from": account})
    print(txDirect.events)
    print(txDirect.events[0]["_DRus"])
    result.append(txDirect.events[0]["_DRus"])
    txIndirect= reputation.IndirectReputation("0xdD870fA1b7C4700F2BD7f44238821C26f7392148","0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",{"from": account})
    print(txIndirect.events)
    print(txIndirect.events[0])
    Eus = input('Enter Evaluation End user: ')
    txDirect=reputation.DirectReputation("0xdD870fA1b7C4700F2BD7f44238821C26f7392148","0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",Eus,{"from": account})
    print(txDirect.events)
    print(txDirect.events[0]["_DRus"])
    result.append(txDirect.events[0]["_DRus"])

    txIndirect= reputation.IndirectReputation("0xdD870fA1b7C4700F2BD7f44238821C26f7392148","0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",{"from": account})
    print(txIndirect.events)
    print(txIndirect.events[0])
    Eus = input('Enter Evaluation End user: ')
    txDirect=reputation.DirectReputation("0xdD870fA1b7C4700F2BD7f44238821C26f7392148","0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",Eus,{"from": account})
    print(txDirect.events)
    print(txDirect.events[0]["_DRus"])
    result.append(txDirect.events[0]["_DRus"])

    txIndirect= reputation.IndirectReputation("0xdD870fA1b7C4700F2BD7f44238821C26f7392148","0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",{"from": account})
    print(txIndirect.events)
    print(txIndirect.events[0])
    print(result)
    #print(tx.events[0]["oldNumber"])
    #print(tx.events[0]["newNumber"])
    #print(tx.events[0]["addedNumber"])
    #print(tx.events[0]["sender"])
    ##AddressEdgeServers = input('Enter the server address: ')
    ##txReputationofEdgeServers=reputation. ReputationofEdgeServers(AddressEdgeServers)
    ##print(txReputationofEdgeServers.events)
    ##print(txReputationofEdgeServers.events[0])
    #print(tx.events[1])

  
def main():
    deploy()  

