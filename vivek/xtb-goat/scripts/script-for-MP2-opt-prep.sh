for j in a c d e f g h i k l;do for num in 0 1 2 3 4 5; do mkdir MP2-opt/$j/$num; done; done

for j in a c d e f g h i k l;do for num in 0 1 2 3 4 5; do cp MP2/$j/$num/$num.inp MP2-opt/$j/$num/$num.inp; done; done

for j in a c d e f g h i k l;do for num in 0 1 2 3 4 5; do sed -i "1s/$/opt/" MP2-opt/$j/$num/$num.inp; done; done






