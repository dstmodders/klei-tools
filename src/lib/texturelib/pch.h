#pragma once

#pragma once

#include <assert.h>
#include <systemlib/types.h>

#include <stack>
#include <string>
#include <vector>

#define FREEIMAGE_LIB

#define Assert(cond) assert(cond)

class InputImage;

typedef std::vector<InputImage *> InputImages;
typedef std::vector<std::string> StringVec;
