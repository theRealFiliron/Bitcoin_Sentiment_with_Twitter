good_lines.txt: original_training.txt
        cat original_training.txt | sed 's/^"\(.\).*/\1/' | cat -n | egrep '[0-9]+\s[04]' | egrep -o '^[0-9]+' | sort -k 1,1 > $@

sorted_training.txt: original_training.txt
        cat -n original_training.txt | sed 's/ *//' | sort -k 1,1 > $@

new_training.txt: good_lines.txt sorted_training.txt
        join good_lines.txt sorted_training.txt > $@

neg.txt : new_training.txt
        cat new_training.txt | egrep '^"0' > $@

pos.txt: new_training.txt
        cat new_training.txt | egrep '^"4' > $@
        
clean:
        rm -f good_lines.txt sorted_training.txt new_training.txt neg.txt pos.txt
