#Author Zeinab Mahdavifar
#Published on Dec 5 2014

import numpy as np


"""
    This algorithm computes an approximate page rank vector of N pages to within
    some convergence factor. It follows the formula given at http://www.mathworks.com/moler/exm/chapters/pagerank.pdf.
    @param myPages represents the adjacency matrix corresponding to the pages graph. 
    @param p is a value between 0 and 1. Determines the relative
    importance of "stochastic" links. Commonly set to 0.85.
    @param convergence a relative convergence criterion. Smaller
    means better, but more expensive. Here set to 0.01
"""

def pageRank(myPages, p =0.85, convergence = 0.01):
  #if reading the matrix from a file add next two lines
  #f = open ( 'input.txt' , 'r')
  #myPages = [ map(int,line.split(',')) for line in f ]
  transitionMatrix = prepareMatrix(myPages, p)
  print('Transision Matrix is: ')
  print transitionMatrix
  pageRanks = pageRankCalculator(transitionMatrix, convergence)
  sortedPages = sorted(pageRanks, key=lambda x: x[0], reverse = True)
  print('Sorted Pages are: ')
  print sortedPages
  return sortedPages

  
#A function to build transition matrix
def prepareMatrix( inputMatrix, p ):
  transitionM = np.matrix(inputMatrix,float )
  transitionM = transitionM.transpose()
  print('Transposed Matrix is: ')
  print transitionM
  columnSum = transitionM.sum(0)
  n = transitionM.shape[0]
  sigma = (1-p)/ n
  for i in range(n):
    for j in range(n):
      if (columnSum[0,j] == 0):
        transitionM [i,j] = 1 / float(n)
      else:
        transitionM[i,j] = p*(transitionM[i,j] / float(columnSum[0,j])) + sigma
  return transitionM
  
#Power Method Convergence Theorem
def pageRankCalculator( trnsMatrix, convergence ):
  n = trnsMatrix.shape[0]
  vectorZ = np.ones((n,1), float) / n
  oldScore = trnsMatrix * vectorZ
  done = False
  while not done:
    newScore = trnsMatrix * oldScore
    diff = sum(abs(newScore - oldScore))
    done = (diff < convergence)
    oldScore = newScore
  print('unranked scores are: ')
  print newScore
  
  # Store scores and indices in tuples
  ranked = []
  for i in range(n):
    item = newScore[i,0]
    scoreIndexTuple = (item, i)
    ranked.append(scoreIndexTuple)  
  return ranked  
  
#The sample input from given graph
#This is the adjacency matrix corresponding to the graph given in ReadMe file.   
m = [[0, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 0],
[0, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 0],
[0, 1, 1, 1, 0, 1],
[0 ,0 ,0 ,0 ,0 ,0]]

pageRank(m)
