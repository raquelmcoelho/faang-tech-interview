'''
Passos para o entendimento do problema:
1. Ler o problema, a Complexidade Temporal a e Complexidade Espacial;
2. Executar a questão e ler a saída (garante 95% do entendimento);
3. Debugar a questão e entender linha a linha de execução
'''

import p01SlidingWindow as p01
import p02TwoPointers as p02
import p03FastAndSlowPointers as p03
import p04MergeIntervals as p04
import p05InPlaceReversalOfALinkedList as p05
import p06TwoHeaps as p06
import p07KWayMerge as p07
import p08TopKElements as p08
import p09ModifiedBinarySearch as p09
import p10Subsets as p10
import p11GreedyTechniques as p11
import p12Backtracking as p12
import P13DynamicProgramming as p13
import P14CyclicSort as p14
import P15TopologicalSort as p15
import P16Stacks as p16
import P17TreeDepthFirstSearch as p17
import P18TreeBreadthFirstSearch as p18
import P19Trie as p19
import P20HashMap as p20
import P21KnowingWhatToTrack as p21
import p22UnionFind as p22
import p220UnionFindWithoutComents as p220
import p23CustomDataStructures as p23
import p24BitwiseManipulation as p24

def main():
  escolha = int(input("Escolha o número do padrão de 1 a 24: "))
  
  if(escolha == 1): p01.main()
  elif(escolha == 2): p02.main()  
  elif(escolha == 3): p03.main()  
  elif(escolha == 4): p04.main()  
  elif(escolha == 5): p05.main()  
  elif(escolha == 6): p06.main()  
  elif(escolha == 7): p07.main()  
  elif(escolha == 8): p08.main()  
  elif(escolha == 9): p09.main()  
  elif(escolha == 10): p10.main()  
  elif(escolha == 11): p11.main()  
  elif(escolha == 12): p12.main()  
  elif(escolha == 13): p13.main()  
  elif(escolha == 14): p14.main()  
  elif(escolha == 15): p15.main()  
  elif(escolha == 16): p16.main()  
  elif(escolha == 17): p17.main()  
  elif(escolha == 18): p18.main()  
  elif(escolha == 19): p19.main()  
  elif(escolha == 20): p20.main()  
  elif(escolha == 21): p21.main()  
  elif(escolha == 22): p22.main()  
  elif(escolha == 220): p220.main()  
  elif(escolha == 23): p23.main()  
  elif(escolha == 24): p24.main()  
    
if __name__ == '__main__':
    main()