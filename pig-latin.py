import sys

def igpay(word):
         result='';
         vowels = ['a', 'e', 'i', 'o', 'u']

         if word[0] in vowels:
             result = word + "way"
         else:
             index = 0
             consonentCluster = '';
             while word[index] not in vowels:
                 consonentCluster += word[index]
                 index += 1
             else:
                 result = word[index:] + consonentCluster + "ay"

         return result

if(len(sys.argv) > 1):
    print(igpay(str(sys.argv[1])))
    