
# def deals(cost):
#     if cost >50 and cost<=150:
#         respond='Good deal'
#     elif cost>150:
#         respond='very expensive'
#     else:
#         respond='Too cheap, can buy now'
#     return respond

# store=input('store name:')
# cost=float(input('cost:'))

# use=deals(cost)
# print(store, "---",cost)
# if use=="Good deal":
#     print('buy it now before the deal is over')
    
def points(scores):
    points=1
    while scores != 0:
        if scores >5 and scores <=10:
            points=points+2
        elif scores >10 and scores <=20:
            points=points+3
        else:
            points=points+5
        return points
point=int(input('Enter the points: '))
print(points(point))        
                

    