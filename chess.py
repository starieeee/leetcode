def evaluateChessLocation(pos):
    letter = pos[0]
    number = pos[1]
    if (letter == 'a' or letter == 'h') and (number == '1' or number == '8'):
        return 'Corner'
    elif letter == 'a' or letter == 'h' or number == '1' or number == '8':
        return 'Border'
    else:
        return 'Inside'