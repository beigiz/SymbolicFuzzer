from fuzzingbook.SymbolicFuzzer import SimpleSymbolicFuzzer, to_src, PNode, to_single_assignment_predicates
from fuzzingbook.ControlFlow import PyCFG


class SymbolicFuzzer(SimpleSymbolicFuzzer):
    def get_all_paths(self, fenter):
        path_array = [PNode(0, fenter)]
        paths_done = []
        for i in range(self.max_iter):
            temp_path = [PNode(0, fenter)]
            for path in path_array:
                if path.cfgnode.children:
                    path_node = path.explore()
                    for p in path_node:
                        if path.idx > self.max_depth:
                            break
                        temp_path.append(p)
                else:
                    paths_done.append(path)
            path_array = temp_path
        return completed + path_array
