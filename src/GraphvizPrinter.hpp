#ifndef GRAPHVIZ_PRINTER_HPP
#define GRAPHVIZ_PRINTER_HPP

#include <ostream>
#include "DFA.h"

class GraphvizPrinter {
public:
    static void print(DFA* dfa) {
        std::ostream& os = cerr;
        os << "digraph G {" << endl;
        os << "rankdir=LR" << endl;
        for (int i = 0; i < dfa->getStateSum(); ++i) {
            for (int j = 1; j<=dfa->getEClass()->getSum(); ++j) {
                int next = dfa->nextState(i, j);
                os << "\"#" << i << "\" -> \"" << "#"
                   << next << "\"[label=\"" << j << "\"]" << endl;
            }
        }
        os << "}" << endl;
    }


};


#endif /* end of include guard: GRAPHVIZ_PRINTER_HPP */
