#include "LexInterface.h"
#include "Lex.h"

LexInterface* LexInterface::Create() {
    return new Lex();
}
