b = [" " for _ in range(4)]
print(b)
print("\n")
c= [[" " for _ in range(4)] for _ in range(4)]
print(c)
#board =[[" " for _ in range(3)] for _ in range(3)]
#for row in board:
 #   print(" | ".join(row))
#    print(" " * 9)
#print(board)
def display_board(board):
    print("\n")
    for  row in board :
        print(" | ".join(row))
        print ("-" * 9)
board=[[" "for _ in range(3)] for _ in range(3)]
display_board(board)