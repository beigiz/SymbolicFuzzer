from fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer, SimpleSymbolicFuzzer
from inspect import getmembers, isfunction


for func in getmembers(mymodule, isfunction):

    advance_gcd = AdvancedSymbolicFuzzer(func[1],
                                        max_iter=10,
                                        max_tries=5,
                                        max_depth=10

    paths = advance_gcd.get_all_paths(advance_gcd.fnenter)

    print("------------------------------------------------------------")
    print("Function:",func[0],". Found total paths: ", len(paths))

    for i in range(len(paths)):
        print("Paths: ", i)
        print("Constraints:", advance_gcd.extract_constraints(paths[i].get_path_to_root()))