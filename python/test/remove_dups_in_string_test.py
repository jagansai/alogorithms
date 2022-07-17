

from src.remove_dups_in_string import removeDuplicatesInString



def test_remove_dups_in_string():
    
    assert "" == removeDuplicatesInString("abbbaaccdddc", 3)
    
    assert "c" == removeDuplicatesInString("abbbaabaddc", 2)