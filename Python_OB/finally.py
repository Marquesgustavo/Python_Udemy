# Se uma cláusula finally estiver presente, 
# a cláusula finally será executada como a última tarefa 
# antes da conclusão da instrução try

def bool_return():
    try:
        return True
    finally:
        return False

c1 = bool_return()
print(c1)