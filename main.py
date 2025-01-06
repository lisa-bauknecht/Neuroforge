price = 8
discounts = [0, 1, 0.95, 0.9, 0.8, 0.75]

#calculates the discount from different discount groups (total) from current splitting
def discount(basket):
    for i in range(len(basket)):
        basket[i] = basket[i] * discounts[basket[i]] * price
    return sum(basket)

#copies list and increments entry at certain index by 1
def increase_by_one(basket, index):
    if 0 <= index < len(basket):
        new = basket[:index] + [basket[index] + 1] + basket[index+1:]
    else:
        new = basket
    return new

def bucket(basket):
    #sort out invalid baskets
    if len(basket) < 1 or len(basket) > 5:
        return 0
    
    basket.sort(reverse=True)
    result = [1] * basket[0]
    
    #distributes the books of a certain book part into seperate discount groups,
    #so that there is the biggest discount
    for i in range(1, len(basket)):
        free_positions = set(range(len(result)))
        
        while basket[i] != 0:
            #finds the best position (with maximal discount/minimal price) within the free positions
            bestposition = min(free_positions)
            bestdiscount = discount(increase_by_one(result, bestposition))
            
            for j in free_positions:
                temporalresult = increase_by_one(result, j)
                temporaldiscount = discount(temporalresult)
                
                if temporaldiscount < bestdiscount:
                    bestposition = j
                    bestdiscount = temporaldiscount

            result[bestposition] += 1
            free_positions.remove(bestposition)

            basket[i] -= 1

    return discount(result)

#UnitTests:
def test_discount():
    x = [4, 3, 1]
    result = discount(x)
    assert result == 55.2

def test_discount_empty():
    x = []
    result = discount(x)
    assert result == 0

def test_increase_by_one():
    x = [4, 3, 1]
    index = 2
    result = increase_by_one(x, index)
    assert result == [4, 3, 2]

def test_increase_by_one_empty():
    x = []
    index = 1
    result = increase_by_one(x, index)
    assert result == []

def test_bucket():
    x = [2, 2, 2, 1, 1]
    result = bucket(x)
    assert result == 51.2

def test2_bucket():
    x = [4, 3, 1, 1]
    result = bucket(x)
    assert result == 64

def test_bucket_empty():
    x = []
    result = bucket(x)
    assert result == 0

def test_bucket_unvalid():
    x = [1, 2, 1, 1, 2, 1, 2]
    result = bucket(x)
    assert result == 0
